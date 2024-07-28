from setuptools import setup, find_packages
from pathlib import Path
import os

here = os.path.abspath(os.path.dirname(__file__))

VERSION = '0.1.1'
DESCRIPTION = 'A discord.py extension for command localization.'

# Setting up
setup(
    name="discord-localization",
    version=VERSION,
    author="Pearoo",
    author_email="<contact@pearoo.dev>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=Path("README.md").read_text(),
    packages=find_packages(),
    install_requires=[],
    keywords=['discord.py', 'i18n', 'translation', 'localisation', 'localization'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    project_urls={
        "Source": "https://github.com/PearooXD/discord-localization"
    }
)
# command: python setup.py sdist bdist_wheel