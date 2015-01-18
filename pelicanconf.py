#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'fuzzmz'
SITENAME = 'QWERTY'
SITEURL = 'http://fuzz.me.uk'
SITESUBTITLE = 'ramblings on tech, life, and randomness'

PATH = 'content'

TIMEZONE = 'Europe/Bucharest'

DEFAULT_LANG = 'en'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
FEED_ATOM = 'fuzzmeuk/main.xml'
FEED_DOMAIN = 'http://feeds.feedburner.com'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#static
STATIC_PATHS = ['images',
                'CNAME']
EXTRA_PATH_METADATA = {
                        'CNAME': {'path': 'CNAME'}
                      }

#Pagination
#DEFAULT_PAGINATION = 3
DEFAULT_PAGINATION = 8

#theme
THEME = "../pelican-themes/pelican-twitchy"
BOOTSTRAP_THEME = 'sandstone'
PYGMENTS_STYLE = 'colorful'

#paths
#PAGE_SAVE_AS = ''
# ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
# ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'

#plugins
PLUGIN_PATHS = ['../pelican-plugins', '../pelican-plugins-custom' ]
PLUGINS = ['render_math' , 'sort_tags' , 'bootstrapify', 'toc']

#dateformat
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DEFAULT_DATE = 'fs'

# Blogroll
# LINKS =  (('barely.sexy Blog', 'https://barely.sexy/'),
#           ('Archlinux', 'https://www.archlinux.org/'),
#           ('FreeDNS', 'http://freedns.afraid.org/'),
#           ('Rasperry Pi', 'http://www.raspberrypi.org/'),
#          )

# Social widget
SOCIAL = (
            ('Twitter', 'https://twitter.com/fuzzmz'),
            ('GitHub', 'https://github.com/fuzzmz'),
            ('Google+', 'https://plus.google.com/+serbanconstantin'),
            # ('RSS', SITEURL + '/' + FEED_ALL_ATOM),
            ('RSS', 'https://feeds.feedburner.com/fuzzmeuk'),
            ('EMAIL', 'mailto:serban.constantin@gmail.com'),
          )

# Share
SHARE = True

#disqus
DISQUS_SITENAME = 'fuzzmeuk'
DISQUS_LOAD_LATER = True

#typography
TYPOGRIFY = True

#sitelogo
# SITELOGO = '/sitelogo.png'
# SITELOGO_SIZE = '200'
HIDE_SITENAME = False

#menu
DISPLAY_RECENT_POSTS_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = False
DISPLAY_TAGS_ON_MENU = False
EXPAND_LATEST_ON_INDEX = True

#tag cloud
TAG_CLOUD_STEPS = 3
TAG_CLOUD_MAX_ITEMS = 20

#Google Analytics
# GOOGLE_ANALYTICS='UA-8040053-2'

#Markdown
#MD_EXTENSIONS = ['codehilite(css_class=highlight)','extra']
