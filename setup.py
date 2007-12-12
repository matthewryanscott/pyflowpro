from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(
    name='PyFlowPro',
    version=version,
    description="Use Payflow Pro directly from Python",
    long_description="""\
    """,
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='',
    author_email='',
    url='',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
    ],
    tests_require=[
    'nose',
    ],
    test_suite='nose.collector',
    entry_points="""
    # -*- Entry points: -*-
    """,
    )
