from setuptools import setup

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
#     long_description = f.read()
long_description = None

for line in open(path.join(here, 'rglogger.py'), encoding=('utf-8')):
    if line.startswith("VERSION_INFO"):
        exec(line)


setup(
    name='rglogger',
    version=".".join(map(str, VERSION_INFO)),  # + ".dev2",  # noqa
    description="Use Python's standard logging library to send messages to Raygun (https://raygun.io/)",
    long_description=long_description,
    url='https://github.com/mirusresearch/raygun-logger',
    author='Don Spaulding',
    author_email='don@mirusresearch.com',
    license='MIT',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='raygun logging exceptions',
    packages=[],
    py_modules=["rglogger"],
    install_requires=['six', 'requests', 'jsonpickle'],
)
