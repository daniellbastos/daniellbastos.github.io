#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Daniel Bastos'
SITENAME = 'Daniel Bastos'
SITESUBTITLE = 'Web Developer - Python Programmer - Linux User'
SITEURL = 'https://daniellbastos.com.br'

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 20

SUMMARY_MAX_LENGTH = 250

RELATIVE_URLS = False

STATIC_PATHS = ['static/', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}
CSS_OVERRIDE = ['static/css/custom.css']


# bio
AUTHORS_BIO = {
    'daniellbastos': {
        'name': 'Daniel Bastos',
        'image': 'static/img/me.png',
        'linkedin': 'daniellbastos',
        'github': 'daniellbastos',
        'location': 'Esteio/RS',
        'bio': ''
    }
}

# plugins
DISQUS_SITENAME = 'daniellbastos'
GOOGLE_ANALYTICS = 'UA-39829332-1'
