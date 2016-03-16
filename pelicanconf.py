#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Daniel Bastos'
SITENAME = 'Daniel Bastos'
SITESUBTITLE = 'Web Developer - Python Programmer - Linux User'
SITEURL = 'http://www.daniellbastos.com.br'

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = 'themes'

MENUITEMS = [('Home', '/')]

DISQUS_SITENAME = 'daniellbastos'
GOOGLE_ANALYTICS = 'UA-39829332-1'

# NEST Template Config
NEST_CSS_MINIFY = True
NEST_HEADER_IMAGES = ''
NEST_HEADER_LOGO = '/theme/images/me.png'

NEST_INDEX_HEAD_TITLE = 'Página inicial'
NEST_INDEX_HEADER_TITLE = 'Meu Blog'
NEST_INDEX_HEADER_SUBTITLE = SITESUBTITLE
NEST_INDEX_CONTENT_TITLE = 'Últimos posts'

NEST_AUTHOR_CONTENT_TITLE = 'Meus posts'

NEST_PAGINATION_PREVIOUS = '<<'
NEST_PAGINATION_NEXT = '>>'

STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico']

SHOW_FOOTER = False
