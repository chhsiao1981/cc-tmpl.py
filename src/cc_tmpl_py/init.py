import os
import subprocess
import sys

from .const import logger
from .gen import generate
from .utils import parse_tmpl_dir


def init(custom_tmpl_dir: str, is_force: bool):
    tmpl_dir = parse_tmpl_dir(custom_tmpl_dir, 'project')

    project_dir = '.'
    generate(tmpl_dir, project_dir, is_force)

    _mark_python_version()

    the_project = os.path.basename(os.getcwd())
    err = _venv(the_project)
    if err is not None:
        return

    err = _init_git()
    if err is not None:
        return

    err = _lefthook()
    if err is not None:
        return

    logger.info('\033[1;36mremember to source .venv/bin/activate\033[m')


def _mark_python_version():
    the_str = f'{sys.version_info.major}.{sys.version_info.minor}\n'

    with open('.python-version', 'w') as f:
        f.write(the_str)


def _venv(project):
    cmd = ['uv', 'sync']
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out, err = p.communicate()

    if p.returncode == 0:
        logger.info('create .venv with uv.')
        return

    cmd = ['python3', '-m', 'venv', '--prompt', project, '.venv']
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out, err = p.communicate()

    if p.returncode != 0:
        logger.warning(f'unable to create .venv: out: {out} e: {err}')
        return Exception(f'unable to create .venv: out: {out} e: {err}')

    cmd = ['/bin/bash', '-c', 'source .venv/bin/activate && pip install --group dev']
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out, err = p.communicate()

    if p.returncode != 0:
        logger.warning(f'unable to install dev packages: out: {out} e: {err}')
        return Exception(f'unable to install dev packages: out: {out} e: {err}')

    logger.info('create .venv with python3 -m venv.')


def _lefthook():
    cmd = ['/bin/bash', '-c', 'source .venv/bin/activate && lefthook install']
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out, err = p.communicate()

    if p.returncode != 0:
        logger.warning(f'unable to lefthook: out: {out} e: {err}')
        return Exception(f'unable to lefthook: out: {out} e: {err}')


def _init_git():
    cmd = ['git', 'init']
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out, err = p.communicate()

    if p.returncode != 0:
        logger.warning(f'unable to git init: out: {out} e: {err}')
        return Exception(f'unable to git init: out: {out} e: {err}')

    cmd = ['git', 'add', '.']
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out, err = p.communicate()

    if p.returncode != 0:
        logger.warning(f'unable to git add: out: {out} e: {err}')
        return Exception(f'unable to git add: out: {out} e: {err}')

    cmd = ['git', 'commit', '-m', 'feat: init project.']
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out, err = p.communicate()

    if p.returncode != 0:
        logger.warning(f'unable to git commit: out: {out} e: {err}')
        return Exception(f'unable to git commit: out: {out} e: {err}')
