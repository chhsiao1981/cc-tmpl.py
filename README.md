# cc-tmpl.py

An opinioned cookiecutter template for python development with the following features:

* [ruff](https://docs.astral.sh/ruff/) + [autopep8](https://github.com/hhatto/autopep8)
* [pytest](https://docs.pytest.org/en/stable/) + [pytest-cov](https://github.com/pytest-dev/pytest-cov)
* [lefthook](https://lefthook.dev/)
* [docker](https://www.docker.com/) build / push scripts.

## Breaking Changes

Starting v0.7.0:
* This repo is renamed as `cc-tmpl.py`.
* Major refactor of the underlying tools.
* As a pypi package.

## Install

`cc-tmpl.py` is considered as a global tool for python development.

To install with [`uv`](https://docs.astral.sh/uv/):

```sh
uv tool install cc-tmpl.py
```

To install with [`pipx`](https://pipx.pypa.io/stable/):

```sh
pipx install cc-tmpl.py
```

## Getting Started

* Initalizing a python development project:

```sh
cc-tmpl.py init
```

* Adding a module (ex: `a.b.c.d`):

```sh
cc-tmpl.py a.b.c.d
```

* Initializing docker scripts:

```sh
cc-tmpl.py docker
```
