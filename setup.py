#!/usr/bin/env python
from setuptools import setup

setup(
    name="pivotal2pdf",
    author="Christopher Strack",
    author_email="csk@ableton.com",
    description="A utility to generate PDFs from CSV exported from Pivotal",
    packages=["pivotal2pdf"],
    install_requires=['fpdf'],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'pivotal2pdf = pivotal2pdf:main',
        ],
    }
)
