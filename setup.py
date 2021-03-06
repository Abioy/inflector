import sys

from setuptools import setup, find_packages

if not '2.5' <= sys.version:
    raise ImportError('Python version not supported')

tests_require = []

with open("LICENSE", 'r') as f:
    LICENSE = f.read()

setup(
    name="Inflector",
    version="2.0.7",
    description="A port of ROR's inflector class",
    classifiers=["Intended Audience :: Developers",
        "License :: OSI Approved :: Python Software Foundation License",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    author="Parnell Springmeyer",
    author_email="parnell@ixmat.us",
    url="https://github.com/ixmatus/inflector",
    license=LICENSE,
    test_suite='tests',
    data_files=[('', ["LICENSE", "README.md", "CHANGES", "DEBT"])],
    packages=["inflector"]
)
