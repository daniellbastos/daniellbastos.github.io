#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Daniel Bastos'
SITENAME = 'Daniel Bastos'
SITESUBTITLE = 'Web Developer / Python Programmer'
# SITEURL = '' # use local
SITEURL = 'https://daniellbastos.com.br'
HEADER_COVER = 'static/img/daniellbastos-banner.jpg'

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt'

THEME_STATIC_DIR = './theme'
THEME = 'attila'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_RSS = 'rss'

DEFAULT_PAGINATION = 5

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
        'cover': 'static/img/daniellbastos-banner.jpg',
    }
}

# plugins
DISQUS_SITENAME = 'daniellbastos'
GOOGLE_ANALYTICS = 'UA-39829332-1'
