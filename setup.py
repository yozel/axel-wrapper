from distutils.core import setup

from setuptools import find_packages

setup(
    name='axel',
    version='0.0.1',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    url='https://github.com/yozel/python-axel',
    license='GPL3',
    author='Yasin Ozel',
    author_email='me@yozel.co',
    description='Python wrapper of axel, a light command line download accelerator'
)
