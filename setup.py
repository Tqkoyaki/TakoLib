from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

AUTHOR = 'Tqkoyaki (Nikhil Pandey)'
EMAIL = 'np768@scarletmail.rutgers.edu'

LIB_NAME = 'takolib'
VERSION = '0.0.1'
DESCRIPTION = 'Currently a test library'
LONG_DESCRIPTION = 'A deployment of a library with the hopes of adding utility functions to help with data science programming.'

KEYWORDS = ['python']
CLASSIFIERS = [
    "Development Status :: 1 - Planning",
    "Intended Audience :: Developers",
    "Programming Language :: Python :: 3"
]

LICENSE = 'MIT'
REQUIREMENTS = []


# Setting up
setup(
    name=LIB_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    license=LICENSE,
    packages=find_packages(),
    install_requires=REQUIREMENTS,
    keywords=KEYWORDS,
    classifiers=CLASSIFIERS
)