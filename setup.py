#!/usr/bin/env python

from distutils.core import setup

setup(name='pykwallet',
      version='0.1',
      description='Library for an easy access to kwallet over dbus-Interface.',
      author='Alexander Weigl',
      author_email='alexweigl@gmail.com',
      url='http://areku.kilu.de',
      download_url='',
      scripts=['src/kwallet_shell.py'],
      package_data={'':'src/'},
      packages=["kwallet"],
      provides=['kwallet (0.1)'],

      classifiers=[ # see http://pypi.python.org/pypi?%3Aaction=list_classifiers for all !
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Programming Language :: Python',
        ],      
      long_description="""""",
     )
