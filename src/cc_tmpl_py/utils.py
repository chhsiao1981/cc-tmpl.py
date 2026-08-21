import os
import sys
from importlib import resources
from pathlib import Path

from .const import COMMANDS, PROJECT, logger


def parse_tmpl_dir(tmpl_dir: str, module: str):
    if tmpl_dir and os.path.exists(tmpl_dir):
        return Path(tmpl_dir)

    root_path = resources.files(PROJECT) / 'cc_modules'
    path = root_path / module

    if tmpl_dir:
        logger.warning(f'{tmpl_dir} does not exist, use default {module}')

    return path


def ensure_command():
    is_skip = False
    is_to_insert_idx = -1
    for idx, each_argv in enumerate(sys.argv[1:]):
        if is_skip:
            is_skip = False
            continue
        if each_argv == '-h' or each_argv == '--help':
            return
        elif each_argv == '-f' or each_argv == '--force':
            continue
        elif each_argv.startswith('-'):
            is_skip = True
            continue
        elif each_argv in COMMANDS:
            return
        else:
            is_to_insert_idx = idx + 1
            break

    sys.argv.insert(is_to_insert_idx, 'dev')
