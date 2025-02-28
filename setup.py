# -*- coding: utf-8 -*-
try:
    import setuptools
except ImportError:
    import sys
    print('''\
Could not import `setuptools` module.

Please install it.

Under Ubuntu, it is in a package called `python-setuptools`.''', file=sys.stderr)
    sys.exit(1)

from setuptools import setup, find_packages
# execfile('pymorph/pymorph_version.py')
# long_description = file('README.rst').read()

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Scientific/Engineering :: Image Recognition',
    'Topic :: Software Development :: Libraries :: Python Modules',
    ]

setup(name='pymorph',
      version=0.95,
      description='Image Morphology Toolbox',
      long_description='https://github.com/luispedro/pymorph',
      author='Luis Pedro Coelho',
      author_email='lpc@cmu.edu',
      url='http://luispedro.org/software/pymorph/',
      license='BSD',
      packages=find_packages(),
      )


