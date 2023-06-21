from setuptools import setup, find_packages
from PyExpansion import version

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="PyExpansion",
    version=version.version,
    package_dir={
        "common": "common",
        "application": "application",
    },
    packages=find_packages(),
    python_requires=">=3",
    long_description=long_description,
    long_description_content_type='text/markdown'
)
