# coding=utf-8
import os
import yaml
import sys
from subprocess import Popen, PIPE, STDOUT

WINDOWS = os.name == "nt"

dirname, filename = os.path.split(os.path.abspath(__file__))
ROOT_DIR = dirname.split('modules')[0]
BASE_URL = upstream.split('ant')[0]

MODE = ["framework", "local-monitor*"]


def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    stdout, _ = p.communicate()
    return p.returncode, stdout.strip()


config_yaml_path = os.path.join(ROOT_DIR, 'config.yaml')
circlectl_path = os.path.join(ROOT_DIR, os.path.normpath('bin/circlectl'))

if WINDOWS:
    datamonitor_path = os.path.join(ROOT_DIR,
                                    'modules\\local-monitor\\datamonitor.conf')
else:
    datamonitor_path = os.path.join(ROOT_DIR,
                                    'modules/local-monitor/conf/datamonitor.conf')

if not os.path.exists(config_yaml_path):
    print('ERROR: {} not found'.format(config_yaml_path))
    sys.exit(1)


def modify_yaml():
    with open(config_yaml_path) as f:
        content = yaml.load(f)
    content["upstream"] = upstream
    content["network_domain"] = network_domain
    with open(config_yaml_path, 'w') as f:
        yaml.dump(content, f, default_flow_style=False)
    print "modify_yaml success"


def modify_datamonitor():
    file_data = ""
    m_url = 'm_url: {}monitor/api/v2/gateway/dd-agent\n'.format(BASE_URL)
    with open(datamonitor_path, 'r') as f:
        for line in f:
            if line.startswith('m_url'):
                line = line.replace(line, m_url)
            file_data += line

    with open(datamonitor_path, 'w') as f:
        f.write(file_data)
    print "modify_datamonitor success"


def circlectl_restart():
    for mode in MODE:
        cmd = '{} {} restart {}'.format(sys.executable, circlectl_path, mode)
        code, ret = run_cmd(cmd)
        if code:
            print 'ERROR: code: {}, ret: {}, cmd:{}'.format(code, ret, cmd)
            sys.exit(1)
        print "circlectl restart {} success".format(mode)


modify_yaml()
if os.path.exists(datamonitor_path):
    modify_datamonitor()
circlectl_restart()