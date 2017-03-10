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
# LINKS = (
#     ('LinkedIn', 'https://www.linkedin.com/in/valentinascipione'),
#     )

# Social widget
SOCIAL = (('linkedin','https://www.linkedin.com/in/valentinascipione'),
          ('twitter', 'https://twitter.com/v_scipione'),
          ('github', 'https://github.com/astroVale'),
         )

DEFAULT_PAGINATION = 10
DEFAULT_CATEGORY = 'General'
DEFAULT_METADATA = {
    'status': 'draft',
}

# Display pages list on the top menu
DISPLAY_PAGES_ON_MENU = True

# PAGES = [('About', 'pages/about.html'),
#          ('CV', 'pages/cv.html'),
#          ('Archives', 'archives.html')
#         ]

# Display categories list on the top menu
DISPLAY_CATEGORIES_ON_MENU = False

# Display categories list as a submenu of the top menu
DISPLAY_CATEGORIES_ON_SUBMENU = False

# Display the category in the article's info
DISPLAY_CATEGORIES_ON_POSTINFO= False

# Display the author in the article's info
DISPLAY_AUTHOR_ON_POSTINFO= False

# Display the search form
DISPLAY_SEARCH_FORM= False

# Sort pages list by a given attribute
# PAGES_SORT_ATTRIBUTE = Title


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'

MENUITEMS = [('Home', ''),
             ('About', '/pages/about.html'),
             ('CV', '/pages/cv.html'),
             ('Archives', 'archives.html'),
             ]

NEWEST_FIRST_ARCHIVES = True

STATIC_PATHS = [
    'images'
]

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["render_math", "liquid_tags.notebook", "share_post", "embed_tweet"]
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.toc': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

THEME = 'themes/pelican-clean-blog'
SITEIMAGE = '/images/CV-2.png width=90 height=90'
HEADER_COVER = 'images/astro_sayner.jpg'

GITHUB_URL = 'https://github.com/astroVale'
TWITTER_URL = 'https://twitter.com/v_scipione'
COLOR_SCHEME_CSS = 'darkly.css'