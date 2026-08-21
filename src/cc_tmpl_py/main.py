import argparse
import os.path
import sys

from .gen_docker import gen_docker
from .gen_module import gen_module
from .init import init
from .utils import ensure_dev_module, get_subcommands


def _argparse():

    parser = argparse.ArgumentParser(prog=os.path.basename(sys.argv[0]))
    singleton_flags = []

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
    singleton_flags = singleton_flags + ['-f', '--force']

    subparsers = parser.add_subparsers(dest="command", required=False)

    subparsers.add_parser("init", help='initialize a project.')

    dev_parser = subparsers.add_parser("dev", help='create a module.')
    dev_parser.add_argument(dest="module")

    docker_parser = subparsers.add_parser("docker", help='create docker scripts.')
    docker_parser.add_argument(
        '-r',
        '--registry',
        required=False,
        default='docker.io',
        help='docker registry.')

    known_commands = get_subcommands(parser)
    ensure_dev_module(known_commands, singleton_flags)

    args = parser.parse_args()

    return args


def main():
    args = _argparse()

    if args.command == 'init':
        init(args.dir, args.force)
    elif args.command == 'dev':
        gen_module(args.dir, args.module, args.force)
    elif args.command == 'docker':
        gen_docker(args.dir, args.registry, args.force)
