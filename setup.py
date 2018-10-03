"A library to capture sys.stdout and -err"

from setuptools import setup, find_packages
from os import path
from io import open
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
long_description = f.read()
setup(
    name='stdget',
    version='1.0',
    description="A library to capture sys.stdout and -err",
    long_description=long_description,
    long_description_content_type='text/markdown'
