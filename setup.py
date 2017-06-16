from setuptools import setup

setup(
    name='falkonry-cli',
    version='1.0.0',
    py_modules=['falkonry'],
    install_requires=[
        'Click',
        'falkonryClient'
    ],
    entry_points='''
        [console_scripts]
        falkonry=falkonry:cli
    ''',
)