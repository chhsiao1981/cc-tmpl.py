from .const import logger
from .gen import generate
from .utils import parse_tmpl_dir


def gen_docker(custom_tmpl_dir: str, registry: str, is_force: bool):
    docker_dir = parse_tmpl_dir(custom_tmpl_dir, "docker")

    generate(docker_dir, registry, is_force)

    logger.info('created docker scripts')
