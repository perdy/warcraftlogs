# -*- coding: utf-8 -*-

import os
import sys
from setuptools import setup

import warcraftlogs

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

if sys.version_info[0] == 2:
    from codecs import open

# Read description
with open(os.path.join(BASE_DIR, "README.rst"), encoding="utf-8") as f:
    _LONG_DESCRIPTION = f.read()

setup(
    name="warcraftlogs",
    version=warcraftlogs.__version__,
    description=warcraftlogs.__description__,
    long_description=_LONG_DESCRIPTION,
    author=warcraftlogs.__author__,
    author_email=warcraftlogs.__email__,
    maintainer=warcraftlogs.__author__,
    maintainer_email=warcraftlogs.__email__,
    url=warcraftlogs.__url__,
    download_url=warcraftlogs.__url__,
    packages=["warcraftlogs"],
    include_package_data=True,
    install_requires=["requests", "pandas"],
    license=warcraftlogs.__license__,
    zip_safe=False,
    keywords="python api warcraft logs analysis",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
