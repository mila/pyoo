"""
PyOO - Pythonic interface to Apache OpenOffice API (UNO)

Copyright (c) 2016-2017 Seznam.cz, a.s.
Copyright (c) 2017-2019 Miloslav Pojman

"""


from setuptools import setup

setup(
    name='pyoo',
    version='1.4',
    description='Pythonic interface to Apache OpenOffice API (UNO)',
    long_description = open('README.rst').read(),
    author='Miloslav Pojman',
    author_email='miloslav.pojman@gmail.com',
    url='https://github.com/mila/pyoo',
    py_modules=['pyoo'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Office/Business :: Office Suites',
        'Topic :: Office/Business :: Financial :: Spreadsheet',
    ],
)
