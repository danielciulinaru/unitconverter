import os
import re
from setuptools import setup, find_packages


def get_info(*file_paths):
    """
    Retrieves the version and name from unitconverter/__init__.py
    :param file_paths: path to file.
    :return: returns __version__ and __app_name__
    """
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    base_info_file = open(filename).read()
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]", base_info_file, re.M
    )
    name_match = re.search(r"^__app_name__ = ['\"]([^'\"]*)['\"]", base_info_file, re.M)
    if version_match and name_match:
        return version_match.group(1), name_match.group(1)
    raise RuntimeError("Unable to find version string.")


version, app_name = get_info("unitconverter", "__init__.py")
requires = ["requests", "cryptography"]
tests_require = []

setup(
    name=app_name,
    version=version,
    description="Package that handles transformation of information units",
    author="",
    author_email="",
    packages=find_packages(exclude=["test"]),
    install_requires=requires,
    test_suite="test",
    tests_require=tests_require,
)
