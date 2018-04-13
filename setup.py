#!/usr/bin/env python

from setuptools import setup, find_packages

desc = ''
with open('README.rst') as f:
    desc = f.read()

setup(
    name='falcon-lambda',
    version='0.1.12',
    description=('Falcon web framework extensions for building AWS Lambda Apps'),
    long_description=desc,
    url='https://github.com/jmvrbanac/falcon-lambda',
    author='John Vrbanac',
    author_email='john.vrbanac@linux.com',
    license='Apache v2',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='falcon framework AWS lambda',
    packages=find_packages(exclude=['contrib', 'docs', 'test*']),
    install_requires=[
        'falcon>=1.3.0'
    ],
    extras_require={
        'swagger': ['prance>=0.7.0', 'jsonschema>=2.6.0'],
        'aws': ['boto3>=1.4.7', 'aws-xray-sdk>=0.97'],
    },
    package_data={},
    data_files=[],
    entry_points={
        'console_scripts': [],
    },
)
