#!/usr/bin/env python
from setuptools import setup, find_packages


with open('pritunl_api/__init__.py') as f:
    info = {}
    for line in f.readlines():
        if line.startswith('version'):
            exec(line, info)
            break

requirements = []
with open('requirements.txt', 'r') as fh:
    for line in fh:
        requirements.append(line.strip())

setup_info = dict(
    name='pritunl_api',
    version=info['version'],
    author='',
    author_email='',
    url='',
    download_url='',
    project_urls={
        'Documentation': '',
        'Source': '',
        'Tracker': '',
    },
    description='Pritunl API Client for Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: System :: Networking',
        'Topic :: System :: Systems Administration',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    # Package info
    packages=['pritunl_api'] + ['pritunl_api.' + pkg for pkg in find_packages('pritunl_api')],

    install_requires=requirements,
    zip_safe=False
)

setup(**setup_info)
