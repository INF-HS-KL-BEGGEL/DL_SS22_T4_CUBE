# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='DeepLearningBabyCube',
    version='0.1.0',
    description='DL',
    long_description=readme,
    author='Stepp, Faas, Plautz',
    author_email='kapl001@stud.hs-kl.de',
    url='',
    license=license,
    package_dir={"": "src"},
    packages=find_packages(exclude=('test', 'docs'))
)