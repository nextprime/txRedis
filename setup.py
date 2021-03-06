#!/usr/bin/env python
sdict = {
    'name': 'txredis',
    'version': '2.4',
    'packages': ['txredis'],
    'description': 'Python/Twisted client for Redis key-value store',
    'author': 'Dorian Raymer',
    'author_email': 'deldotdr@gmail.com',
    'maintainer': 'Reza Lotun',
    'maintainer_email': 'rlotun@gmail.com',
    'keywords': ['Redis', 'key-value store', 'Twisted'],
    'classifiers': [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Framework :: Twisted'],
    'install_requires': ['six'],
}

from setuptools import setup
setup(**sdict)
