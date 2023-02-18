from setuptools import setup
import os

VERSION = "0.2.0"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="telegram-cli",
    description="Python CLI tool and library for sending messages to Telegram",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Maurizio Branca",
    url="https://github.com/zmoog/telegram-cli",
    project_urls={
        "Issues": "https://github.com/zmoog/telegram-cli/issues",
        "CI": "https://github.com/zmoog/telegram-cli/actions",
        "Changelog": "https://github.com/zmoog/telegram-cli/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["telegram_cli"],
    entry_points="""
        [console_scripts]
        tgm=telegram_cli.cli:cli
    """,
    install_requires=[
        "click",
        "requests",
    ],
    extras_require={
        "test": ["pytest", "pytest-recording"]
    },
    python_requires=">=3.7",
)
