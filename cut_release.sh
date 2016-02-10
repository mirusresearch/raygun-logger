#!/bin/bash
pandoc --from=markdown --to=rst --output=README.rst README.md

RGVER=`grep '^VERSION_INFO' rglogger.py | python2 -c 'exec(raw_input()); print ".".join(map(str, VERSION_INFO))'`

python setup.py sdist bdist_wheel --universal

twine upload dist/rglogger-$RGVER*
