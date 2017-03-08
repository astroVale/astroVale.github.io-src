#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Valentina Scipione'
SITENAME = u"Data Science's Tales"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('LinkedIn', 'https://www.linkedin.com/in/valentinascipione'),
    #('You can modify those links in your config file', '#'),
    )

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10
DEFAULT_CATEGORY = 'General'
DEFAULT_METADATA = {
    'status': 'draft',
}
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'

STATIC_PATHS = [
    'images',
    'files',
    'extra/favicon.ico'
]
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["render_math", "liquid_tags.notebook"]
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.toc': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

THEME = 'themes/pelican-alchemy/alchemy'
SITEIMAGE = '/images/NG1J2764.png width=90 height=90'

DISQUS_SITENAME = "DS Tales"
