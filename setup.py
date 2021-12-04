from setuptools import setup, find_packages

setup(
    name="crysterm",
    version="0.1.0",
    author="mofuru",
    author_email="me@mofuru.is-a.dev",
    url="https://github.com/mofuru/crysterm",
    license="MIT",
    packages=find_packages(exclude=("tests", "docs"))
)
