# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 18:43:44 2019

@author: e1012466

To create a package use below command 
python setup.py develop
"""

from setuptools import setup

setup(name='datapeek',
      version='0.1',
      description='A simple library for dealing with raw data.',
      author='Venkatesh Reddy Madduri',
      author_email='maddurivenkys@gmail.com',
      license='MIT',
      packages=['datapeek'],
      install_requires=[
      'fuzzywuzzy',
      'pandas'
      ],
      zip_safe=False)