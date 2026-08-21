import argparse
import os.path
import sys

from .gen_module import gen_module
from .init import init
from .utils import ensure_command


def _argparse():
    parser = argparse.ArgumentParser(prog=os.path.basename(sys.argv[0]))

    parser.add_argument(
        '-d',
        '--dir',
        default='',
        type=str,
        required=False,
        help='customized cookiecutter template directory.')

    parser.add_argument(
        '-f',
        '--force',
        default=False,
        required=False,
        action='store_true',
        help='replace the file if it already exists.')

    subparsers = parser.add_subparsers(dest="command", required=False)

    subparsers.add_parser("init", help='initialize a project.')

    dev_parser = subparsers.add_parser("dev", help='create a module.')
    dev_parser.add_argument(dest="module")

    ensure_command()

    args = parser.parse_args()

    return args


def main():
    args = _argparse()

    if args.command == 'init':
        init(args.dir, args.force)
    elif args.command == 'dev':
        gen_module(args.dir, args.module, args.force)
