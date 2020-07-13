# -*- coding: utf-8 -*-
from setuptools import setup

from luqum import __version__


with open('README.rst', 'r') as f:
    long_description = f.read()
with open('CHANGELOG.rst', 'r') as f:
    long_description += "\n\n" + f.read()


setup(
    name='ebv-luqum',
    version=__version__,
    description="A Lucene query parser generating ElasticSearch queries and more !",
    long_description=long_description,
    author='Jurismarches',
    author_email='contact@jurismarches.com',
    url='https://github.com/yasinmeydan/luqum',
    packages=[
        'luqum',
        'luqum.elasticsearch'
    ],
    install_requires=[
        'ply>=3.11',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='luqum.tests'
)
