from .const import logger
from .gen import generate
from .utils import parse_tmpl_dir


def gen_module(custom_tmpl_dir: str, module_name: str, is_force: bool):
    pkg_dir = parse_tmpl_dir(custom_tmpl_dir, "pkg")
    module_dir = parse_tmpl_dir(custom_tmpl_dir, "module")

    pkg_module_list = module_name.split('.')
    pkgs = pkg_module_list[:-1]

    for idx in range(1, len(pkgs)):
        full_pkg = '.'.join(pkgs[:idx])

        generate(pkg_dir, full_pkg, is_force)

    generate(module_dir, module_name, is_force)

    logger.info(f'created {module_name}')
