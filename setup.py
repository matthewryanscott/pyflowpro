from setuptools import setup, find_packages
import sys, os

from pyflowpro import version

setup(
    name='PyFlowPro',
    version=version.NUMBER,
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
    [simplsale.commerce]
    pyflowpro-live = pyflowpro.plugins.simplsale:LiveCommerce
    pyflowpro-pilot = pyflowpro.plugins.simplsale:PilotCommerce
    """,
    )
