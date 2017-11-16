#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='botbot_plugins',
    version='1.0',
    description="Plugins and service integrations for BotBot.me",
    author="Lincoln Loop",
    author_email='info@lincolnloop.com',
    url='https://github.com/lincolnloop/botbot_plugins',
    packages=find_packages(),
    install_requires=(
        'pytest==2.3.5',
        'mock==1.0.1',
        'requests==2.7.0',
        'defusedxml==0.4.1',
        'fakeredis==0.9.0',
    ),
    scripts=['bin/botbot-shell'],
)
