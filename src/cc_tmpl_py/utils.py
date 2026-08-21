import argparse
import os
import sys
from argparse import ArgumentParser
from importlib import resources
from pathlib import Path

from .const import PROJECT, logger


def parse_tmpl_dir(tmpl_dir: str, module: str):
    if tmpl_dir and os.path.exists(tmpl_dir):
        return Path(tmpl_dir)

    root_path = resources.files(PROJECT) / 'cc_modules'
    path = root_path / module

    if tmpl_dir:
        logger.warning(f'{tmpl_dir} does not exist, use default {module}')

    return path


def get_subcommands(parser: ArgumentParser) -> list[str]:
    for action in parser._actions:
        if isinstance(action, argparse._SubParsersAction):
            return list(action.choices.keys())
    return []


def ensure_dev_module(known_commands: list[str], singleton_flags: list[str]):
    '''
    to deal with the args with only modules.

    CONTEXT:

    1. command is always the 1st positional argument.
    2. we may have --dir dev, as dev is a parameter, not a command.
    3. we may have dev init, as init is a parameter for dev, not a command.
    4. only dev is with positional arg, as module.
    5. for other commands: either singleton (init, docker), or optional args with --.

    STEPS (as state machine):

    is-to-skip
    is-to-insert-idx

    for loop the argv:
        if is-skip: reset is-skip and skip. (as the parameter of '-', '--').
        elif -h: return. (help, no need to do anything.)
        elif singleton-flags: continue (singleton flags).
        elif flags: set is-skip. (flags with 1 parameter).
        elif known-commands: return. (command already specified.)
        else: set is_to_insert_idx. (no command).
    '''
    is_skip = False
    is_to_insert_idx = -1
    for idx, each_argv in enumerate(sys.argv[1:]):
        if is_skip:
            is_skip = False
            continue
        elif each_argv == '-h' or each_argv == '--help':
            return
        elif each_argv in singleton_flags:
            continue
        elif each_argv.startswith('-'):
            is_skip = True
            continue
        elif each_argv in known_commands:
            return
        else:
            is_to_insert_idx = idx + 1
            break

    sys.argv.insert(is_to_insert_idx, 'dev')
