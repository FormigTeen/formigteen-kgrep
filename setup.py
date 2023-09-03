from setuptools import setup

setup(
    name='formigteen_kgrep',
    version='0.1.0',
    packages=['formigteen_kgrep'],
    entry_points={
        'console_scripts': [
            'formigteen-kgrep = formigteen_kgrep.main:app',
        ],
    },
)