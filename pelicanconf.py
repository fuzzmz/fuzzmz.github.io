#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'fuzzmz'
SITENAME = 'Fuzzmz | ramblings on tech, life, and randomness by Serban Constantin'
SITEURL = 'http://fuzz.me.uk'
SITESUBTITLE = 'ramblings on tech, life, and randomness'

PATH = 'content'

TIMEZONE = 'Europe/Bucharest'

DEFAULT_LANG = 'en'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

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
                'extra/CNAME',
                'extra/robots.txt']
EXTRA_PATH_METADATA = {
                        'extra/CNAME': {'path': 'CNAME'},
                        'extra/robots.txt': {'path': 'robots.txt'}
                      }

#Pagination
DEFAULT_PAGINATION = 8

#theme
THEME = "./static_deps/pelican-themes/pelican-twitchy"
BOOTSTRAP_THEME = 'sandstone'
PYGMENTS_STYLE = 'colorful'

#paths
#PAGE_SAVE_AS = ''
# ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
# ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'

#plugins
PLUGIN_PATHS = ['./static_deps/pelican-plugins', './static_deps/pelican-plugins-custom' ]
PLUGINS = ['render_math' , 'sort_tags' , 'bootstrapify', 'toc', 'pelicanfly', 'clean_summary']

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
          )

# Share
SHARE = True

#disqus
DISQUS_SITENAME = ''
DISQUS_LOAD_LATER = False

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
