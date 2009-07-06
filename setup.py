#!/usr/bin/env python

from distutils.core import setup

setup(name='pykwallet',
      version='0.1',
      description='Library for an easy access to kwallet over dbus-Interface.',
      author='Alexander Weigl',
      author_email='alexweigl@gmail.com',
      url='http://areku.kilu.de',
      license='Creative Commons 3.0 share-alike (http://creativecommons.org/licenses/by-sa/3.0/)',
      download_url='http://bitbucket.org/alex953/pykwallet',
      scripts=['src/kwallet_shell.py', 'src/kwalletcli'],
      package_dir={'':'src/'},
      packages=['kwallet'],
      py_modules = ['kwallet.dbus_api'],
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
