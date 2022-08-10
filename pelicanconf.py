# -*- coding: utf-8 -*- #

AUTHOR = 'Jim Read'
SITENAME = "#!/bin/bash it 'till it works"
SITESUBTITLE = "The blog of a Zsh user."
SITEURL = 'https://cannoncontraption.github.io'

PATH = 'content'

THEME = 'themes/bashworks'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('WindowTools', 'https://gitlab.com/CannonContraption/windowTools'),
         ('Desktop Site', 'desktop/'),
         ('Feeder for Android', 'https://gitlab.com/spacecowboy/Feeder'),
         ('Fluent Reader', 'https://hyliu.me/fluent-reader/'),
         ('Feedly for iOS', 'https://apps.apple.com/app/feedly-get-smarter/id396069556'),
         ('Archives', 'archives'),)

# Social widget
SOCIAL = (('GitLab', 'https://gitlab.com/CannonContraption'),
         ('GitHub', 'https://github.com/CannonContraption'),
         ('YouTube', 'https://www.youtube.com/channel/UC5Yt2D-FPphO4fjQix-S05Q'),
         ('SoundCloud', 'https://soundcloud.com/jimmydean886'),)

DEFAULT_PAGINATION = False

DISPLAY_CATEGORIES_ON_MENU = False

MENUITEMS = (('Archives', 'archives'),
             ('Categories/Tags', 'categories'))

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
