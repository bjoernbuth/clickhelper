from setuptools import setup, find_packages

setup(
    name="clickhelper",
    version="2024.8.13.2",
    author="Bjoern",
    packages=find_packages(),
    install_requires=[
        "click",
    ],
    entry_points={
        "console_scripts": [
            "clickhelper = clickhelper.dumphelp_to_file.py:main",
            "clihe = clickhelper.dumphelp_to_file.py:main",
        ],
    },
)
