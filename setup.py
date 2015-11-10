from setuptools import setup

setup(
    name='marisa',
    version='0.1.0',
    entry_points = {
        'console_scripts': ['marisa=marisa.cli:run'],
    },
    description='Command line tool for managing laser jobs',
    classifiers=[
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
    ],
    install_requires=[
        'requests'
    ],
    author='Dan Nixon',
    packages=['marisa'],
    include_package_data=True,
    zip_safe=True)
