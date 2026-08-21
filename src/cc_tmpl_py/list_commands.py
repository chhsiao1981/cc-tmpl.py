from argparse import ArgumentParser

from .utils import get_subcommands


def list_commands(parser: ArgumentParser):
    commands = get_subcommands(parser)
    commands_str = ' '.join(commands)
    print(f'{commands_str}')
