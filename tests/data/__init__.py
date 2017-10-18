import os
import pathlib

curdir = pathlib.Path(os.path.dirname(__file__))


def get_path(name):
    return curdir.joinpath(name)


def load(name):
    with get_path(name).open() as fp:
        return fp.read()
