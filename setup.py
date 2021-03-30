#!/usr/bin/env python

from setuptools import setup

setup(
    name='target-s3',
    version='1.0.0',
    description='hotglue target for exporting data to AWS S3',
    author='hotglue',
    url='https://hotglue.xyz',
    classifiers=['Programming Language :: Python :: 3 :: Only'],
    py_modules=['target_s3'],
    install_requires=[
        'boto3==1.10.45',
        'argparse==1.4.0'
    ],
    entry_points='''
        [console_scripts]
        target-s3=target_s3:main
    ''',
    packages=['target_s3']
)
