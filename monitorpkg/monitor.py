# coding: utf-8
import hashlib
import json
import time
import copy
import data

from tornado import gen
from tornado.ioloop import IOLoop
from subprocess import Popen, PIPE, STDOUT
from tornado.httpclient import AsyncHTTPClient
from framework.util import config


def execute(cmd, wait=True, shell=True):
    p = Popen(cmd, shell=shell, stdout=PIPE, stderr=STDOUT)
    if wait:
        stdout, _ = p.communicate()
        return p.poll(), stdout
    return p


class MonitorClient(object):
    def __init__(self, ip):
        self.ip = ip
        self.io_loop = IOLoop.current()
        self.tenant = config.get('tenant', 'e10adc3949ba59abbe56e057f20f88dd')
        self.apikey = config.get('apikey', 'e10adc3949ba59abbe56e057f2gg88dd')
        self.network_domain = config.get('network_domain', '')
        self.id = \
            hashlib.md5('{}:{}:{}'.format(
                self.tenant, self.network_domain, self.ip)).hexdigest()
        self.base_url = config.get('upstream')
        self._info_url =\
            '{}monitor/api/v2/agent/info/intake?api_key={}'\
            .format(self.base_url, self.apikey)
        self._intake_url = \
            '{}monitor/api/v2/gateway/dd-agent/api/v1/series/?api_key={}'\
            .format(self.base_url, self.apikey)
        self._retry_interval = 30
        self._http_client = AsyncHTTPClient(max_clients=10000)
        self._app =\
            ['agent_metrics.yaml.default', 'disk.yaml.default',
             'network.yaml.default', 'ntp.yaml.default']
        self.data = copy.deepcopy(data)
        self.data.update({'apiKey': self.apikey, 'ip': self.ip, 'uuid': self.id})

    @gen.coroutine
    def send_info(self):
        while 1:
            returncode, hostname = execute('hostname', shell=True)
            if returncode != 0:
                hostname = 'unknown'
            try:
                message = {
                    "id": self.id,
                    "hostname": hostname,
                    "ip": self.ip,
                    "tags": [],
                    "apps": self._app,
                    "source": "agent",
                    "modified": int(time.time()),
                }
                yield self.send(self._info_url, message)
            except Exception as exc:
                print('Error while sending info: %s', exc)
            yield gen.sleep(30)

    @gen.coroutine
    def send_data(self):
        while 1:
            try:
                yield self.send(self._intake_url, self.data)
            except Exception as e:
                print('Error while sending data: %s', e)
            yield gen.sleep(30)

    @gen.coroutine
    def send(self, url, messages):
        try:
            response = yield self._http_client.fetch(
                url,
                method='POST',
                headers={'Content-Type': 'application/json'},
                validate_cert=False,
                connect_timeout=90,
                request_timeout=90,
                body=json.dumps({'messages': messages}))
        except Exception as exc:
            print('Error in http transfer: {},  {}'.format(str(exc), messages))
            if hasattr(exc, 'response') and exc.response:
                print('Error in http transfer:{},  {}'.format(str(exc), messages))
            raise gen.Return(False)
        else:
            raise gen.Return(response.code == 200)

    @gen.coroutine
    def start(self):
        self.io_loop.spawn_callback(self.send_info)
        self.io_loop.spawn_callback(self.send_data)

