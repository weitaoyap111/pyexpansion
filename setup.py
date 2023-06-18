from setuptools import setup, find_packages
from PyExpansion import version

setup(
    name="PyExpansion",
    version=version.version,
    package_dir={
        "common": "common",
        "application": "application",
    },
    packages=find_packages(),
    python_requires=">=3",
)
