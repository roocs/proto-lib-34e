# -*- coding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup


version = '1.0.0'
description = 'ROCCS data operations demo library.'
long_description = 'Prototype for 34e libraries and interfaces'

requirements = [line.strip() for line in open('requirements.txt')]
dev_requirements = [line.strip() for line in open('requirements_dev.txt')]

classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Science/Research',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX',
    'Programming Language :: Python',
    'Topic :: Scientific/Engineering :: Atmospheric Science',
    'License :: OSI Approved :: Apache Software License',
]

setup(name='daops',
      version=version,
      description=description,
      long_description=long_description,
      classifiers=classifiers,
      keywords='roocs daops demo',
      author='Ag Stephens',
      author_email="ag.stephens@stfc.ac.uk",
      python_requires='>=3.7',
      url='https://github.com/roocs/proto-lib-34e',
      license="Apache License v2.0",
      packages=find_packages(),
      include_package_data=True,
      install_requires=requirements,
      extras_require={
          "dev": dev_requirements,      # pip install ".[dev]"
      },
      entry_points={},
      )
