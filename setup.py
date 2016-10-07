#!/usr/bin/env python
# the python installer
from setuptools import setup

setup (name = 'lumi2d',
       version = '1.0.0',
       description = "Generate 2d luminosity histogram",
       author = 'S. Carrazza',
       author_email = 'stefano.carrazza@cern.ch',
       url = 'https://github.com/scarrazza/lumi2d',
       long_description = "See `lumi2d --help` for the full list of options",
       scripts = ['lumi2d'],
       install_requires=['numpy','argparse','lhapdf'],
       zip_safe = False,
       classifiers=[
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Operating System :: Unix',
            'Programming Language :: Python',
            'Topic :: Scientific/Engineering',
            'Topic :: Scientific/Engineering :: Physics'
            ],
       )
