from setuptools import setup, find_packages
import sys, os

from pyflowpro import version

setup(
    name='PyFlowPro',
    version=version.NUMBER,
    description="Perform transactions with PayPal's Payflow Pro service",
    long_description="""\
    PyFlowPro allows you to perform credit card sale transactions
    with PayPal's Payflow Pro service from within Python.

    PyFlowPro uses Payflow Pro's newer HTTPS interface.
    """,
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Matthew Scott',
    author_email='gldnspud@gmail.com',
    url='http://code.3purple.com/pyflowpro/',
    license='MIT',
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
