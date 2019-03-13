import os
import sysutil
from contextlib import nested
from functools import wraps
import logging
import subprocess
import tempfile

from p_platform import Platform

log = logging.getLogger(__name__)


if not sysutil.WINDOWS:
    bin_path = os.path.join(os.getcwd(), 'embedded', 'bin')
    os.environ['PATH'] = '{}:{}'.format(bin_path, os.environ['PATH'])


class SubprocessOutputEmptyError(Exception):
    pass


def get_subprocess_output(command, shell=False, stdin=None, output_expected=True, env_ignore=False):

    with nested(tempfile.TemporaryFile(), tempfile.TemporaryFile()) as (stdout_f, stderr_f):
        kwargs = {}
        if env_ignore:
            kwargs['env'] = {}
        proc = subprocess.Popen(command,
                                close_fds=not Platform.is_windows(),
                                shell=shell,
                                stdin=stdin,
                                stdout=stdout_f,
                                stderr=stderr_f,
                                **kwargs)
        proc.wait()
        stderr_f.seek(0)
        err = stderr_f.read()
        if err:
            log.debug("Error while running {0} : {1}".format(" ".join(command),
                                                             err))

        stdout_f.seek(0)
        output = stdout_f.read()

    if output_expected and output is None:
        raise SubprocessOutputEmptyError("get_subprocess_output expected output but had none.")

    return (output, err, proc.returncode)


def log_subprocess(func):
    @wraps(func)
    def wrapper(*params, **kwargs):
        fc = "%s(%s)" % (func.__name__, ', '.join(
            [a.__repr__() for a in params] +
            ["%s = %s" % (a, b) for a, b in kwargs.items()]
        ))
        log.debug("%s called" % fc)
        return func(*params, **kwargs)
    return wrapper

subprocess.Popen = log_subprocess(subprocess.Popen)
