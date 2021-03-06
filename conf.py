# -*- coding: utf-8 -*-

import time

# !! This is the configuration of Nikola. !! #
# !!  You should edit it to your liking.  !! #


# ! Some settings can be different in different languages.
# ! A comment stating (translatable) is used to denote those.
# ! There are two ways to specify a translatable setting:
# ! (a) BLOG_TITLE = "My Blog"
# ! (b) BLOG_TITLE = {"en": "My Blog", "es": "Mi Blog"}
# ! Option (a) is used when you don't want that setting translated.
# ! Option (b) is used for settings that are different in different languages.


# Data about this site
BLOG_AUTHOR = "Karl Lorey"  # (translatable)
BLOG_TITLE = "Karl Lorey"  # (translatable)
# This is the main URL for your site. It will be used
# in a prominent link. Don't forget the protocol (http/https)!
SITE_URL = "http://www.karllorey.de/"
# This is the URL where Nikola's output will be deployed.
# If not set, defaults to SITE_URL
# BASE_URL = "http://www.karllorey.de/"
BLOG_EMAIL = ""
BLOG_DESCRIPTION = "Archiv der deutschen Website von Karl Lorey"  # (translatable)

# Nikola is multilingual!
#
# Currently supported languages are:
#
# en        English
# af        Afrikaans
# ar        Arabic
# az        Azerbaijani
# bg        Bulgarian
# bs        Bosnian
# ca        Catalan
# cs        Czech [ALTERNATIVELY cz]
# da        Danish
# de        German
# el        Greek [NOT gr]
# eo        Esperanto
# es        Spanish
# et        Estonian
# eu        Basque
# fa        Persian
# fi        Finnish
# fr        French
# fur       Friulian
# gl        Galician
# he        Hebrew
# hi        Hindi
# hr        Croatian
# hu        Hungarian
# ia        Interlingua
# id        Indonesian
# it        Italian
# ja        Japanese [NOT jp]
# ko        Korean
# lt        Lithuanian
# ml        Malayalam
# nb        Norwegian (Bokmål)
# nl        Dutch
# pa        Punjabi
# pl        Polish
# pt        Portuguese
# pt_br     Portuguese (Brazil)
# ru        Russian
# sk        Slovak
# sl        Slovene
# sq        Albanian
# sr        Serbian (Cyrillic)
# sr_latin  Serbian (Latin)
# sv        Swedish
# te        Telugu
# th        Thai
# tr        Turkish [NOT tr_TR]
# uk        Ukrainian
# ur        Urdu
# vi        Vietnamese
# zh_cn     Chinese (Simplified)
# zh_tw     Chinese (Traditional)
#
# If you want to use Nikola with a non-supported language you have to provide
# a module containing the necessary translations
# (cf. the modules at nikola/data/themes/base/messages/).
# If a specific post is not translated to a language, then the version
# in the default language will be shown instead.

# What is the default language?
DEFAULT_LANG = "de"

# What other languages do you have?
# The format is {"translationcode" : "path/to/translation" }
# the path will be used as a prefix for the generated pages location
TRANSLATIONS = {
    DEFAULT_LANG: "",
    # Example for another language:
    # "es": "./es",
}

# What will translated input files be named like?

# If you have a page something.rst, then something.pl.rst will be considered
# its Polish translation.
#     (in the above example: path == "something", ext == "rst", lang == "pl")
# this pattern is also used for metadata:
#     something.meta -> something.pl.meta

TRANSLATIONS_PATTERN = "{path}.{lang}.{ext}"

# Links for the sidebar / navigation bar.  (translatable)
# This is a dict.  The keys are languages, and values are tuples.
#
# For regular links:
#     ('https://getnikola.com/', 'Nikola Homepage')
#
# For submenus:
#     (
#         (
#             ('https://apple.com/', 'Apple'),
#             ('https://orange.com/', 'Orange'),
#         ),
#         'Fruits'
#     )
#
# WARNING: Support for submenus is theme-dependent.
#          Only one level of submenus is supported.
# WARNING: Some themes, including the default Bootstrap 4 theme,
#          may present issues if the menu is too large.
#          (in Bootstrap, the navbar can grow too large and cover contents.)
# WARNING: If you link to directories, make sure to follow
#          ``STRIP_INDEXES``.  If it’s set to ``True``, end your links
#          with a ``/``, otherwise end them with ``/index.html`` — or
#          else they won’t be highlighted when active.

NAVIGATION_LINKS = {
    DEFAULT_LANG: (
        ("/", "Home"),
        ("/blog", "Blog"),
        ("/archive.html", "Blog-Archiv"),
        # ("/categories/index.html", "Tags"),
        # ("/rss.xml", "RSS feed"),
        ("/pages", "Seiten"),
        ("/impressum", "Impressum"),
    )
}

# Alternative navigation links. Works the same way NAVIGATION_LINKS does,
# although themes may not always support them. (translatable)
# (Bootstrap 4: right-side of navbar, Bootblog 4: right side of title)
NAVIGATION_ALT_LINKS = {DEFAULT_LANG: ()}

# Name of the theme to use.
THEME = "karllorey-de"

# Primary color of your theme. This will be used to customize your theme.
# Must be a HEX value.
THEME_COLOR = "#5670d4"

# Theme configuration. Fully theme-dependent. (translatable)
# Examples below are for bootblog4.
# bootblog4 supports: featured_large featured_small featured_on_mobile
#                     featured_large_image_on_mobile featured_strip_html sidebar
# bootstrap4 supports: navbar_light (defaults to False)
THEME_CONFIG = {
    DEFAULT_LANG: {
        # Show the latest featured post in a large box, with the previewimage as its background.
        "featured_large": False,
        # Show the first (remaining) two featured posts in small boxes.
        "featured_small": False,
        # Show featured posts on mobile.
        "featured_on_mobile": True,
        # Show image in `featured_large` on mobile.
        # `featured_small` displays them only on desktop.
        "featured_large_image_on_mobile": True,
        # Strip HTML from featured post text.
        "featured_strip_html": False,
        # Contents of the sidebar, If empty, the sidebar is not displayed.
        "sidebar": "",
    }
}

# POSTS and PAGES contains (wildcard, destination, template) tuples.
# (translatable)
#
# The wildcard is used to generate a list of source files
# (whatever/thing.rst, for example).
#
# That fragment could have an associated metadata file (whatever/thing.meta),
# and optionally translated files (example for Spanish, with code "es"):
#     whatever/thing.es.rst and whatever/thing.es.meta
#
#     This assumes you use the default TRANSLATIONS_PATTERN.
#
# From those files, a set of HTML fragment files will be generated:
# cache/whatever/thing.html (and maybe cache/whatever/thing.html.es)
#
# These files are combined with the template to produce rendered
# pages, which will be placed at
# output/TRANSLATIONS[lang]/destination/pagename.html
#
# where "pagename" is the "slug" specified in the metadata file.
# The page might also be placed in /destination/pagename/index.html
# if PRETTY_URLS are enabled.
#
# The difference between POSTS and PAGES is that POSTS are added
# to feeds, indexes, tag lists and archives and are considered part
# of a blog, while PAGES are just independent HTML pages.
#
# Finally, note that destination can be translated, i.e. you can
# specify a different translation folder per language. Example:
#     PAGES = (
#         ("pages/*.rst", {"en": "pages", "de": "seiten"}, "page.tmpl"),
#         ("pages/*.md", {"en": "pages", "de": "seiten"}, "page.tmpl"),
#     )

POSTS = (
    ("posts/*.rst", "posts", "post.tmpl"),
    ("posts/*.txt", "posts", "post.tmpl"),
    ("posts/*.md", "posts", "post.tmpl"),
    ("posts/*.html", "posts", "post.tmpl"),
)

PAGES = (
    ("pages/*.rst", "", "page.tmpl"),
    ("pages/*.txt", "", "page.tmpl"),
    ("pages/*.md", "", "page.tmpl"),
    ("pages/*.html", "", "page.tmpl"),
)
INDEX_PATH = "blog"


# Below this point, everything is optional

# Post's dates are considered in UTC by default, if you want to use
# another time zone, please set TIMEZONE to match. Check the available
# list from Wikipedia:
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# (e.g. 'Europe/Zurich')
# Also, if you want to use a different time zone in some of your posts,
# you can use the ISO 8601/RFC 3339 format (ex. 2012-03-30T23:00:00+02:00)
TIMEZONE = "UTC"

# If you want to use ISO 8601 (also valid RFC 3339) throughout Nikola
# (especially in new_post), set this to True.
# Note that this does not affect DATE_FORMAT.
# FORCE_ISO8601 = False

# Date format used to display post dates. (translatable)
# Used by babel.dates, CLDR style: http://cldr.unicode.org/translation/date-time
# You can also use 'full', 'long', 'medium', or 'short'
DATE_FORMAT = "yyyy-MM-dd"

# Date format used to display post dates, if local dates are used. (translatable)
# Used by moment.js: https://momentjs.com/docs/#/displaying/format/
# JS_DATE_FORMAT = 'YYYY-MM-DD HH:mm'

# Date fanciness.
#
# 0 = using DATE_FORMAT and TIMEZONE
# 1 = using JS_DATE_FORMAT and local user time (via moment.js)
# 2 = using a string like “2 days ago”
#
# Your theme must support it, Bootstrap already does.
# DATE_FANCINESS = 0

# Customize the locale/region used for a language.
# For example, to use British instead of US English: LOCALES = {'en': 'en_GB'}
# LOCALES = {}

# One or more folders containing files to be copied as-is into the output.
# The format is a dictionary of {source: relative destination}.
# Default is:
# FILES_FOLDERS = {'files': ''}
# Which means copy 'files' into 'output'

# One or more folders containing code listings to be processed and published on
# the site. The format is a dictionary of {source: relative destination}.
# Default is:
# LISTINGS_FOLDERS = {'listings': 'listings'}
# Which means process listings from 'listings' into 'output/listings'

# A mapping of languages to file-extensions that represent that language.
# Feel free to add or delete extensions to any list, but don't add any new
# compilers unless you write the interface for it yourself.
#
# The default compiler for `new_post` is the first entry in the POSTS tuple.
#
# 'rest' is reStructuredText
# 'markdown' is Markdown
# 'html' assumes the file is HTML and just copies it
COMPILERS = {
    "rest": (".txt", ".rst"),
    "markdown": (".md", ".mdown", ".markdown"),
    "html": (".html", ".htm"),
}

# Enable reST directives that insert the contents of external files such
# as "include" and "raw." This maps directly to the docutils file_insertion_enabled
# config. See: http://docutils.sourceforge.net/docs/user/config.html#file-insertion-enabled
# REST_FILE_INSERTION_ENABLED = True

# Create by default posts in one file format?
# Set to False for two-file posts, with separate metadata.
# ONE_FILE_POSTS = True

# Preferred metadata format for new posts
# "Nikola": reST comments, wrapped in a HTML comment if needed (default)
# "YAML": YAML wrapped in "---"
# "TOML": TOML wrapped in "+++"
# "Pelican": Native markdown metadata or reST docinfo fields. Nikola style for other formats.
# METADATA_FORMAT = "Nikola"

# Use date-based path when creating posts?
# Can be enabled on a per-post basis with `nikola new_post -d`.
# The setting is ignored when creating pages.
# NEW_POST_DATE_PATH = False

# What format to use when creating posts with date paths?
# Default is '%Y/%m/%d', other possibilities include '%Y' or '%Y/%m'.
# NEW_POST_DATE_PATH_FORMAT = '%Y/%m/%d'

# If this is set to True, the DEFAULT_LANG version will be displayed for
# untranslated posts.
# If this is set to False, then posts that are not translated to a language
# LANG will not be visible at all in the pages in that language.
# SHOW_UNTRANSLATED_POSTS = True

# Nikola supports logo display.  If you have one, you can put the URL here.
# Final output is <img src="LOGO_URL" id="logo" alt="BLOG_TITLE">.
# The URL may be relative to the site root.
# LOGO_URL = ''

# If you want to hide the title of your website (for example, if your logo
# already contains the text), set this to False.
# SHOW_BLOG_TITLE = True

# Paths for different autogenerated bits. These are combined with the
# translation paths.

# Final locations are:
# output / TRANSLATION[lang] / TAG_PATH / index.html (list of tags)
# output / TRANSLATION[lang] / TAG_PATH / tag.html (list of posts for a tag)
# output / TRANSLATION[lang] / TAG_PATH / tag RSS_EXTENSION (RSS feed for a tag)
# (translatable)
# TAG_PATH = "categories"

# By default, the list of tags is stored in
#     output / TRANSLATION[lang] / TAG_PATH / index.html
# (see explanation for TAG_PATH). This location can be changed to
#     output / TRANSLATION[lang] / TAGS_INDEX_PATH
# with an arbitrary relative path TAGS_INDEX_PATH.
# (translatable)
# TAGS_INDEX_PATH = "tags.html"

# If TAG_PAGES_ARE_INDEXES is set to True, each tag's page will contain
# the posts themselves. If set to False, it will be just a list of links.
# TAG_PAGES_ARE_INDEXES = False

# Set descriptions for tag pages to make them more interesting. The
# default is no description. The value is used in the meta description
# and displayed underneath the tag list or index page’s title.
# TAG_DESCRIPTIONS = {
#    DEFAULT_LANG: {
#        "blogging": "Meta-blog posts about blogging.",
#        "open source": "My contributions to my many, varied, ever-changing, and eternal libre software projects."
#    },
# }

# Set special titles for tag pages. The default is "Posts about TAG".
# TAG_TITLES = {
#    DEFAULT_LANG: {
#        "blogging": "Meta-posts about blogging",
#        "open source": "Posts about open source software"
#    },
# }

# If you do not want to display a tag publicly, you can mark it as hidden.
# The tag will not be displayed on the tag list page and posts.
# Tag pages will still be generated.
HIDDEN_TAGS = ["mathjax"]

# Only include tags on the tag list/overview page if there are at least
# TAGLIST_MINIMUM_POSTS number of posts or more with every tag. Every tag
# page is still generated, linked from posts, and included in the sitemap.
# However, more obscure tags can be hidden from the tag index page.
# TAGLIST_MINIMUM_POSTS = 1

# A list of dictionaries specifying tags which translate to each other.
# Format: a list of dicts {language: translation, language2: translation2, …}
# For example:
#   [
#     {'en': 'private', 'de': 'Privat'},
#     {'en': 'work', 'fr': 'travail', 'de': 'Arbeit'},
#   ]
# TAG_TRANSLATIONS = []

# If set to True, a tag in a language will be treated as a translation
# of the literally same tag in all other languages. Enable this if you
# do not translate tags, for example.
# TAG_TRANSLATIONS_ADD_DEFAULTS = True

# Final locations are:
# output / TRANSLATION[lang] / CATEGORY_PATH / index.html (list of categories)
# output / TRANSLATION[lang] / CATEGORY_PATH / CATEGORY_PREFIX category.html (list of posts for a category)
# output / TRANSLATION[lang] / CATEGORY_PATH / CATEGORY_PREFIX category RSS_EXTENSION (RSS feed for a category)
# (translatable)
# CATEGORY_PATH = "categories"
# CATEGORY_PREFIX = "cat_"

# By default, the list of categories is stored in
#     output / TRANSLATION[lang] / CATEGORY_PATH / index.html
# (see explanation for CATEGORY_PATH). This location can be changed to
#     output / TRANSLATION[lang] / CATEGORIES_INDEX_PATH
# with an arbitrary relative path CATEGORIES_INDEX_PATH.
# (translatable)
# CATEGORIES_INDEX_PATH = "categories.html"

# If CATEGORY_ALLOW_HIERARCHIES is set to True, categories can be organized in
# hierarchies. For a post, the whole path in the hierarchy must be specified,
# using a forward slash ('/') to separate paths. Use a backslash ('\') to escape
# a forward slash or a backslash (i.e. '\//\\' is a path specifying the
# subcategory called '\' of the top-level category called '/').
CATEGORY_ALLOW_HIERARCHIES = False
# If CATEGORY_OUTPUT_FLAT_HIERARCHY is set to True, the output written to output
# contains only the name of the leaf category and not the whole path.
CATEGORY_OUTPUT_FLAT_HIERARCHY = False

# If CATEGORY_PAGES_ARE_INDEXES is set to True, each category's page will contain
# the posts themselves. If set to False, it will be just a list of links.
# CATEGORY_PAGES_ARE_INDEXES = False

# Set descriptions for category pages to make them more interesting. The
# default is no description. The value is used in the meta description
# and displayed underneath the category list or index page’s title.
# CATEGORY_DESCRIPTIONS = {
#    DEFAULT_LANG: {
#        "blogging": "Meta-blog posts about blogging.",
#        "open source": "My contributions to my many, varied, ever-changing, and eternal libre software projects."
#    },
# }

# Set special titles for category pages. The default is "Posts about CATEGORY".
# CATEGORY_TITLES = {
#    DEFAULT_LANG: {
#        "blogging": "Meta-posts about blogging",
#        "open source": "Posts about open source software"
#    },
# }

# If you do not want to display a category publicly, you can mark it as hidden.
# The category will not be displayed on the category list page.
# Category pages will still be generated.
HIDDEN_CATEGORIES = []

# A list of dictionaries specifying categories which translate to each other.
# Format: a list of dicts {language: translation, language2: translation2, …}
# See TAG_TRANSLATIONS example above.
# CATEGORY_TRANSLATIONS = []

# If set to True, a category in a language will be treated as a translation
# of the literally same category in all other languages. Enable this if you
# do not translate categories, for example.
# CATEGORY_TRANSLATIONS_ADD_DEFAULTS = True

# If no category is specified in a post, the destination path of the post
# can be used in its place. This replaces the sections feature. Using
# category hierarchies is recommended.
# CATEGORY_DESTPATH_AS_DEFAULT = False

# If True, the prefix will be trimmed from the category name, eg. if the
# POSTS destination is "foo/bar", and the path is "foo/bar/baz/quux",
# the category will be "baz/quux" (or "baz" if only the first directory is considered).
# Note that prefixes coming from translations are always ignored.
# CATEGORY_DESTPATH_TRIM_PREFIX = False

# If True, only the first directory of a path will be used.
# CATEGORY_DESTPATH_FIRST_DIRECTORY_ONLY = True

# Map paths to prettier category names. (translatable)
# CATEGORY_DESTPATH_NAMES = {
#    DEFAULT_LANG: {
#        'webdev': 'Web Development',
#        'webdev/django': 'Web Development/Django',
#        'random': 'Odds and Ends',
#    },
# }

# By default, category indexes will appear in CATEGORY_PATH and use
# CATEGORY_PREFIX. If this is enabled, those settings will be ignored (except
# for the index) and instead, they will follow destination paths (eg. category
# 'foo' might appear in 'posts/foo'). If the category does not come from a
# destpath, first entry in POSTS followed by the category name will be used.
# For this setting, category hierarchies are required and cannot be flattened.
# CATEGORY_PAGES_FOLLOW_DESTPATH = False

# If ENABLE_AUTHOR_PAGES is set to True and there is more than one
# author, author pages are generated.
# ENABLE_AUTHOR_PAGES = True

# Path to author pages. Final locations are:
# output / TRANSLATION[lang] / AUTHOR_PATH / index.html (list of authors)
# output / TRANSLATION[lang] / AUTHOR_PATH / author.html (list of posts by an author)
# output / TRANSLATION[lang] / AUTHOR_PATH / author RSS_EXTENSION (RSS feed for an author)
# (translatable)
# AUTHOR_PATH = "authors"

# If AUTHOR_PAGES_ARE_INDEXES is set to True, each author's page will contain
# the posts themselves. If set to False, it will be just a list of links.
# AUTHOR_PAGES_ARE_INDEXES = False

# Set descriptions for author pages to make them more interesting. The
# default is no description. The value is used in the meta description
# and displayed underneath the author list or index page’s title.
# AUTHOR_PAGES_DESCRIPTIONS = {
#    DEFAULT_LANG: {
#        "Juanjo Conti": "Python coder and writer.",
#        "Roberto Alsina": "Nikola father."
#    },
# }


# If you do not want to display an author publicly, you can mark it as hidden.
# The author will not be displayed on the author list page and posts.
# Tag pages will still be generated.
HIDDEN_AUTHORS = ["Guest"]

# Final location for the main blog page and sibling paginated pages is
# output / TRANSLATION[lang] / INDEX_PATH / index-*.html
# (translatable)
# INDEX_PATH = ""

# Optional HTML that displayed on “main” blog index.html files.
# May be used for a greeting. (translatable)
FRONT_INDEX_HEADER = {DEFAULT_LANG: ""}

# Create per-month archives instead of per-year
# CREATE_MONTHLY_ARCHIVE = False
# Create one large archive instead of per-year
CREATE_SINGLE_ARCHIVE = True
# Create year, month, and day archives each with a (long) list of posts
# (overrides both CREATE_MONTHLY_ARCHIVE and CREATE_SINGLE_ARCHIVE)
# CREATE_FULL_ARCHIVES = False
# If monthly archives or full archives are created, adds also one archive per day
# CREATE_DAILY_ARCHIVE = False
# Create previous, up, next navigation links for archives
# CREATE_ARCHIVE_NAVIGATION = False
# Final locations for the archives are:
# output / TRANSLATION[lang] / ARCHIVE_PATH / ARCHIVE_FILENAME
# output / TRANSLATION[lang] / ARCHIVE_PATH / YEAR / index.html
# output / TRANSLATION[lang] / ARCHIVE_PATH / YEAR / MONTH / index.html
# output / TRANSLATION[lang] / ARCHIVE_PATH / YEAR / MONTH / DAY / index.html
# (translatable)
# ARCHIVE_PATH = ""
# ARCHIVE_FILENAME = "archive.html"

# If ARCHIVES_ARE_INDEXES is set to True, each archive page which contains a list
# of posts will contain the posts themselves. If set to False, it will be just a
# list of links.
# ARCHIVES_ARE_INDEXES = False

# URLs to other posts/pages can take 3 forms:
# rel_path: a relative URL to the current page/post (default)
# full_path: a URL with the full path from the root
# absolute: a complete URL (that includes the SITE_URL)
# URL_TYPE = 'rel_path'

# Extension for RSS feed files
# RSS_EXTENSION = ".xml"

# RSS filename base (without extension); used for indexes and galleries.
# (translatable)
# RSS_FILENAME_BASE = "rss"

# Final location for the blog main RSS feed is:
# output / TRANSLATION[lang] / RSS_PATH / RSS_FILENAME_BASE RSS_EXTENSION
# (translatable)
# RSS_PATH = ""

# Final location for the blog main Atom feed is:
# output / TRANSLATION[lang] / ATOM_PATH / ATOM_FILENAME_BASE ATOM_EXTENSION
# (translatable)
# ATOM_PATH = ""

# Atom filename base (without extension); used for indexes.
# (translatable)
ATOM_FILENAME_BASE = "feed"

# Extension for Atom feed files
# ATOM_EXTENSION = ".atom"

# Slug the Tag URL. Easier for users to type, special characters are
# often removed or replaced as well.
# SLUG_TAG_PATH = True

# Slug the Author URL. Easier for users to type, special characters are
# often removed or replaced as well.
# SLUG_AUTHOR_PATH = True

# A list of redirection tuples, [("foo/from.html", "/bar/to.html")].
#
# A HTML file will be created in output/foo/from.html that redirects
# to the "/bar/to.html" URL. notice that the "from" side MUST be a
# relative URL.
#
# If you don't need any of these, just set to []
REDIRECTIONS = [
    (
        "/2012/01/04/datenbanken-losung-fur-ubungsblatt-5-hinzugefugt/index.html",
        "/posts/2012-01-04-datenbanken-losung-fur-ubungsblatt-5-hinzugefugt",
    ),
    (
        "/2012/01/06/musterlosungen-der-ubungsblatter-fur-theoretische-informatik-und-datenbanken-neu-sortiert/index.html",
        "/posts/2012-01-06-musterlosungen-der-ubungsblatter-fur-theoretische-informatik-und-datenbanken-neu-sortiert",
    ),
    (
        "/2013/02/03/geheimnisse-der-chrome-developer-tools/index.html",
        "/posts/2013-02-03-geheimnisse-der-chrome-developer-tools",
    ),
    (
        "/2011/10/29/app-der-woche-school-helper-stundenplan-fur-studenten/index.html",
        "/posts/2011-10-29-app-der-woche-school-helper-stundenplan-fur-studenten",
    ),
    (
        "/2012/01/03/theme-wechsel-von-twenty-ten-auf-twenty-eleven/index.html",
        "/posts/2012-01-03-theme-wechsel-von-twenty-ten-auf-twenty-eleven",
    ),
    (
        "/2013/02/09/google-webmaster-tools-indexierungsstatus-nicht-ausgewahlt-mit-update-entfernt/index.html",
        "/posts/2013-02-09-google-webmaster-tools-indexierungsstatus-nicht-ausgewahlt-mit-update-entfernt",
    ),
    (
        "/2012/01/11/mehrwert-versionsverwaltung-mit-git/index.html",
        "/posts/2012-01-11-mehrwert-versionsverwaltung-mit-git",
    ),
    (
        "/2012/01/07/update-tasker-version-1-2-mit-neuen-features/index.html",
        "/posts/2012-01-07-update-tasker-version-1-2-mit-neuen-features",
    ),
    (
        "/2011/09/22/app-der-woche-my-tracks-tacho-ersatz-fuer-android/index.html",
        "/posts/2011-09-22-app-der-woche-my-tracks-tacho-ersatz-fuer-android",
    ),
    (
        "/2012/11/21/seo-bessere-analyse-der-keyword-dichte-mit-seoquake/index.html",
        "/posts/2012-11-21-seo-bessere-analyse-der-keyword-dichte-mit-seoquake",
    ),
    (
        "/2012/07/13/gedachtnisprotokoll-der-rechenanlagen-klausur/index.html",
        "/posts/2012-07-13-gedachtnisprotokoll-der-rechenanlagen-klausur",
    ),
    (
        "/2011/09/28/doubletwist-synchronisieren-mit-externer-sd-karte-per-workaround/index.html",
        "/posts/2011-09-28-doubletwist-synchronisieren-mit-externer-sd-karte-per-workaround",
    ),
    (
        "/2011/12/08/android-market-noch-mehr-apps-fur-10-cent-am-dritten-tag/index.html",
        "/posts/2011-12-08-android-market-noch-mehr-apps-fur-10-cent-am-dritten-tag",
    ),
    (
        "/2011/12/07/android-market-diverse-apps-fur-nur-10-cent/index.html",
        "/posts/2011-12-07-android-market-diverse-apps-fur-nur-10-cent",
    ),
    (
        "/2011/11/01/alle-artikel-uber-apps-jetzt-mit-qr-code-fur-den-android-market/index.html",
        "/posts/2011-11-01-alle-artikel-uber-apps-jetzt-mit-qr-code-fur-den-android-market",
    ),
    (
        "/2011/11/24/video-erstes-review-des-asus-transformer-prime-tf201/index.html",
        "/posts/2011-11-24-video-erstes-review-des-asus-transformer-prime-tf201",
    ),
    (
        "/2012/04/02/die-informatik-vorlesungsumfrage-an-der-universitat-wurzburg-im-ws-20112012/index.html",
        "/posts/2012-04-02-die-informatik-vorlesungsumfrage-an-der-universitat-wurzburg-im-ws-20112012",
    ),
    (
        "/2011/12/10/android-market-die-10-cent-apps-des-vierten-tags/index.html",
        "/posts/2011-12-10-android-market-die-10-cent-apps-des-vierten-tags",
    ),
    (
        "/2012/04/05/ringvorlesung-unternehmerische-kompetenzen-im-ss-2012/index.html",
        "/posts/2012-04-05-ringvorlesung-unternehmerische-kompetenzen-im-ss-2012",
    ),
    (
        "/2011/11/17/das-display-des-neuen-galaxy-nexus/index.html",
        "/posts/2011-11-17-das-display-des-neuen-galaxy-nexus",
    ),
    (
        "/2012/04/24/sms-backup-manager-0-1-alpha-ab-sofort-downloaden-und-testen/index.html",
        "/posts/2012-04-24-sms-backup-manager-0-1-alpha-ab-sofort-downloaden-und-testen",
    ),
    (
        "/2012/03/22/sms-backup-manager-veroffentlichung-der-ersten-alpha-version/index.html",
        "/posts/2012-03-22-sms-backup-manager-veroffentlichung-der-ersten-alpha-version",
    ),
    (
        "/2011/11/29/google-maps-update-auf-version-6-0/index.html",
        "/posts/2011-11-29-google-maps-update-auf-version-6-0",
    ),
    (
        "/2012/02/05/neue-seite-uber-projekte/index.html",
        "/posts/2012-02-05-neue-seite-uber-projekte",
    ),
    (
        "/2011/11/14/bitte-an-der-umfrage-uber-zukunftige-themen-teilnehmen/index.html",
        "/posts/2011-11-14-bitte-an-der-umfrage-uber-zukunftige-themen-teilnehmen",
    ),
    (
        "/2012/10/23/hardwarepraktikum-robotik-weiterhin-mangel-und-nachbesserungsbedarf/index.html",
        "/posts/2012-10-23-hardwarepraktikum-robotik-weiterhin-mangel-und-nachbesserungsbedarf",
    ),
    (
        "/2011/11/27/ice-cream-sandwich-auf-dem-samsung-galaxy-s-i9000/index.html",
        "/posts/2011-11-27-ice-cream-sandwich-auf-dem-samsung-galaxy-s-i9000",
    ),
    (
        "/2011/09/25/serverumzug-fur-die-wordpress-installation-bei-all-inkl/index.html",
        "/posts/2011-09-25-serverumzug-fur-die-wordpress-installation-bei-all-inkl",
    ),
    (
        "/2011/11/23/app-der-woche-die-ice-cream-sandwich-tastatur-schon-ab-android-version-2-2/index.html",
        "/posts/2011-11-23-app-der-woche-die-ice-cream-sandwich-tastatur-schon-ab-android-version-2-2",
    ),
    ("/2012/04/26/jetzt-mit-gravatar/index.html", "/posts/2012-04-26-jetzt-mit-gravatar"),
    (
        "/2011/12/07/android-market-neuer-tag-neue-apps-fur-10-cent/index.html",
        "/posts/2011-12-07-android-market-neuer-tag-neue-apps-fur-10-cent",
    ),
    (
        "/2013/03/28/java-8-features-und-anderungen-im-neuen-java/index.html",
        "/posts/2013-03-28-java-8-features-und-anderungen-im-neuen-java",
    ),
    (
        "/2011/11/24/angebot-beyondpod-bis-zum-27-11-fur-nur-149e/index.html",
        "/posts/2011-11-24-angebot-beyondpod-bis-zum-27-11-fur-nur-149e",
    ),
    (
        "/2014/10/27/zf2-pflicht-feld-eines-formulars-mit-stern-markieren/index.html",
        "/posts/2014-10-27-zf2-pflicht-feld-eines-formulars-mit-stern-markieren",
    ),
    (
        "/2012/10/17/informationen-uber-mein-funftes-semester-hinzugefugt/index.html",
        "/posts/2012-10-17-informationen-uber-mein-funftes-semester-hinzugefugt",
    ),
    (
        "/2012/10/07/seminar-anmeldung-fur-die-informatik-seminare-im-wintersemester-20122013/index.html",
        "/posts/2012-10-07-seminar-anmeldung-fur-die-informatik-seminare-im-wintersemester-20122013",
    ),
    (
        "/2012/02/11/das-softwarepraktikum-in-den-semesterferien-an-der-uni-wurzburg/index.html",
        "/posts/2012-02-11-das-softwarepraktikum-in-den-semesterferien-an-der-uni-wurzburg",
    ),
    (
        "/2014/08/03/bachelorarbeit-erstes-paper-uni-wechsel-und-master-das-letzte-jahr/index.html",
        "/posts/2014-08-03-bachelorarbeit-erstes-paper-uni-wechsel-und-master-das-letzte-jahr",
    ),
    (
        "/2011/12/14/tasker-android-sms-vorlesen-lassen/index.html",
        "/posts/2011-12-14-tasker-android-sms-vorlesen-lassen",
    ),
    (
        "/2016/01/25/internationale-webseite-von-karl-lorey/index.html",
        "/posts/2016-01-25-internationale-webseite-von-karl-lorey",
    ),
    (
        "/2013/02/06/fur-kommentare-ist-keine-e-mail-adresse-mehr-erforderlich/index.html",
        "/posts/2013-02-06-fur-kommentare-ist-keine-e-mail-adresse-mehr-erforderlich",
    ),
    (
        "/2012/02/29/der-diffie-hellman-schlusselaustausch-verstandlich-erklart/index.html",
        "/posts/2012-02-29-der-diffie-hellman-schlusselaustausch-verstandlich-erklart",
    ),
    (
        "/2012/11/27/indexierungsstatus-nicht-ausgewahlt-bei-google-webmaster-tools/index.html",
        "/posts/2012-11-27-indexierungsstatus-nicht-ausgewahlt-bei-google-webmaster-tools",
    ),
    (
        "/2012/12/12/theme-wechsel-von-tewnty-eleven-auf-twenty-twelve/index.html",
        "/posts/2012-12-12-theme-wechsel-von-tewnty-eleven-auf-twenty-twelve",
    ),
    (
        "/2012/09/12/weitere-informationen-zum-informatik-studium/index.html",
        "/posts/2012-09-12-weitere-informationen-zum-informatik-studium",
    ),
    (
        "/2011/11/18/swiftkey-x-startet-nach-update-nicht-mehr/index.html",
        "/posts/2011-11-18-swiftkey-x-startet-nach-update-nicht-mehr",
    ),
    (
        "/2013/02/23/hallo-ich-bin-ein-compiler/index.html",
        "/posts/2013-02-23-hallo-ich-bin-ein-compiler",
    ),
    (
        "/2011/11/30/amazon-cyber-monday-heute-drei-einsteiger-tablets-mit-android/index.html",
        "/posts/2011-11-30-amazon-cyber-monday-heute-drei-einsteiger-tablets-mit-android",
    ),
    (
        "/2012/10/06/klausur-checkliste-fur-die-betriebssysteme-vorlesung/index.html",
        "/posts/2012-10-06-klausur-checkliste-fur-die-betriebssysteme-vorlesung",
    ),
    (
        "/2013/02/07/komplexe-zahlen-in-java-als-klasse/index.html",
        "/posts/2013-02-07-komplexe-zahlen-in-java-als-klasse",
    ),
    (
        "/2011/12/04/ubungsblatter-losungen-fur-drei-vorlesungen-online/index.html",
        "/posts/2011-12-04-ubungsblatter-losungen-fur-drei-vorlesungen-online",
    ),
    (
        "/2012/04/11/erlebnisbericht-hardwarepraktikum-robotik/index.html",
        "/posts/2012-04-11-erlebnisbericht-hardwarepraktikum-robotik",
    ),
    (
        "/2012/05/16/ablauf-von-google-bewerbungsgesprachen/index.html",
        "/posts/2012-05-16-ablauf-von-google-bewerbungsgesprachen",
    ),
    ("/2011/09/21/es-kann-losgehen/index.html", "/posts/2011-09-21-es-kann-losgehen"),
    (
        "/2011/11/15/app-der-woche-dropbox-synchronisation-mit-der-cloud/index.html",
        "/posts/2011-11-15-app-der-woche-dropbox-synchronisation-mit-der-cloud",
    ),
    (
        "/2013/02/18/pflichtenheft-in-latex-version-0-2-verfugbar/index.html",
        "/posts/2013-02-18-pflichtenheft-in-latex-version-0-2-verfugbar",
    ),
    (
        "/2012/05/05/beim-wordpress-theme-yoko-unterseiten-der-aktuellen-seite-auflisten/index.html",
        "/posts/2012-05-05-beim-wordpress-theme-yoko-unterseiten-der-aktuellen-seite-auflisten",
    ),
    (
        "/2011/11/08/tasker-mit-3rd-party-apps-den-funktionsumfang-erweitern/index.html",
        "/posts/2011-11-08-tasker-mit-3rd-party-apps-den-funktionsumfang-erweitern",
    ),
    (
        "/2013/03/19/java-hello-world-verbluffend-statt-einfach/index.html",
        "/posts/2013-03-19-java-hello-world-verbluffend-statt-einfach",
    ),
    (
        "/2011/12/09/doubletwist-synchronisation-mit-sd-karte-immer-noch-fehlerhaft/index.html",
        "/posts/2011-12-09-doubletwist-synchronisation-mit-sd-karte-immer-noch-fehlerhaft",
    ),
    (
        "/2012/05/09/tasker-notfall-sms-mit-gps-position-versenden/index.html",
        "/posts/2012-05-09-tasker-notfall-sms-mit-gps-position-versenden",
    ),
    (
        "/2012/03/21/daten-zum-vierten-semester-hinzugefugt/index.html",
        "/posts/2012-03-21-daten-zum-vierten-semester-hinzugefugt",
    ),
    (
        "/2016/09/06/die-karlsruher-startup-szene-im-ueberblick-fuer-gruender-und-entrepreneure/index.html",
        "/posts/2016-09-06-die-karlsruher-startup-szene-im-ueberblick-fuer-gruender-und-entrepreneure",
    ),
    ("/tag/endomondo-sports-tacker/index.html", "/categories/endomondo-sports-tacker/"),
    ("/tag/kaloer-clock/index.html", "/categories/kaloer-clock/"),
    ("/tag/sommersemester-2012/index.html", "/categories/sommersemester-2012/"),
    ("/tag/synchronisation/index.html", "/categories/synchronisation/"),
    ("/tag/sleep-bot/index.html", "/categories/sleep-bot/"),
    ("/tag/zend-framework-2/index.html", "/categories/zend-framework-2/"),
    ("/tag/indexierungsstatus/index.html", "/categories/indexierungsstatus/"),
    ("/tag/cloud/index.html", "/categories/cloud/"),
    ("/tag/sport/index.html", "/categories/sport/"),
    (
        "/tag/einfuhrung-in-die-betriebswirtschaftslehre-fur-nichtwirtschaftswissenschaftler/index.html",
        "/categories/einfuhrung-in-die-betriebswirtschaftslehre-fur-nichtwirtschaftswissenschaftler/",
    ),
    ("/tag/podcast/index.html", "/categories/podcast/"),
    ("/tag/color-and-draw-for-kids/index.html", "/categories/color-and-draw-for-kids/"),
    ("/tag/astrid/index.html", "/categories/astrid/"),
    ("/tag/installation/index.html", "/categories/installation/"),
    ("/tag/google/index.html", "/categories/google/"),
    ("/tag/radardroid/index.html", "/categories/radardroid/"),
    ("/tag/hardwarepraktikum-robotik/index.html", "/categories/hardwarepraktikum-robotik/"),
    ("/tag/master/index.html", "/categories/master/"),
    ("/tag/pioniergarage/index.html", "/categories/pioniergarage/"),
    ("/tag/liste/index.html", "/categories/liste/"),
    ("/tag/kit/index.html", "/categories/kit/"),
    ("/tag/doubletwist/index.html", "/categories/doubletwist/"),
    ("/tag/organisation/index.html", "/categories/organisation/"),
    ("/tag/oop/index.html", "/categories/oop/"),
    (
        "/tag/objektorientiertes-programmieren/index.html",
        "/categories/objektorientiertes-programmieren/",
    ),
    ("/tag/bewerbung/index.html", "/categories/bewerbung/"),
    ("/tag/newsrob/index.html", "/categories/newsrob/"),
    ("/tag/office-talk/index.html", "/categories/office-talk/"),
    ("/tag/praktikum/index.html", "/categories/praktikum/"),
    ("/tag/theoretische-informatik/index.html", "/categories/theoretische-informatik/"),
    ("/tag/minecraft/index.html", "/categories/minecraft/"),
    ("/tag/php/index.html", "/categories/php/"),
    ("/tag/school-helper/index.html", "/categories/school-helper/"),
    ("/tag/anleitung/index.html", "/categories/anleitung/"),
    ("/tag/my-tracks/index.html", "/categories/my-tracks/"),
    ("/tag/sms-backup-manager/index.html", "/categories/sms-backup-manager/"),
    ("/tag/pomodroido-pro/index.html", "/categories/pomodroido-pro/"),
    ("/tag/fehler/index.html", "/categories/fehler/"),
    ("/tag/lenovo/index.html", "/categories/lenovo/"),
    ("/tag/odys-space/index.html", "/categories/odys-space/"),
    ("/tag/hardwarepraktikum/index.html", "/categories/hardwarepraktikum/"),
    ("/tag/great-little-war-game/index.html", "/categories/great-little-war-game/"),
    ("/tag/karlsruhe/index.html", "/categories/karlsruhe/"),
    ("/tag/kdd/index.html", "/categories/kdd/"),
    ("/tag/asphalt-6/index.html", "/categories/asphalt-6/"),
    ("/tag/flick-golf/index.html", "/categories/flick-golf/"),
    ("/tag/spam/index.html", "/categories/spam/"),
    ("/tag/unternehmerische-kompetenzen/index.html", "/categories/unternehmerische-kompetenzen/"),
    ("/tag/java/index.html", "/categories/java/"),
    ("/tag/code/index.html", "/categories/code/"),
    ("/tag/bug/index.html", "/categories/bug/"),
    ("/tag/angebot/index.html", "/categories/angebot/"),
    ("/tag/allgemein/index.html", "/categories/allgemein/"),
    ("/tag/anderung/index.html", "/categories/anderung/"),
    ("/tag/theme/index.html", "/categories/theme/"),
    ("/tag/changelog/index.html", "/categories/changelog/"),
    ("/tag/app/index.html", "/categories/app/"),
    ("/tag/seoquake/index.html", "/categories/seoquake/"),
    ("/tag/uni-wechsel/index.html", "/categories/uni-wechsel/"),
    ("/tag/paper-camera/index.html", "/categories/paper-camera/"),
    ("/tag/prinzipien/index.html", "/categories/prinzipien/"),
    ("/tag/adwlauncher-ex/index.html", "/categories/adwlauncher-ex/"),
    ("/tag/hello-world/index.html", "/categories/hello-world/"),
    ("/tag/entrepreneurship/index.html", "/categories/entrepreneurship/"),
    ("/tag/swiftkey-x/index.html", "/categories/swiftkey-x/"),
    ("/tag/monitoring/index.html", "/categories/monitoring/"),
    ("/tag/gravatar/index.html", "/categories/gravatar/"),
    ("/tag/ibm/index.html", "/categories/ibm/"),
    ("/tag/gigabyte-z87-d3hp/index.html", "/categories/gigabyte-z87-d3hp/"),
    ("/tag/nebenfach/index.html", "/categories/nebenfach/"),
    ("/tag/update/index.html", "/categories/update/"),
    ("/tag/stack-overflow/index.html", "/categories/stack-overflow/"),
    ("/tag/softwaretechnik/index.html", "/categories/softwaretechnik/"),
    ("/tag/due-today/index.html", "/categories/due-today/"),
    ("/tag/webhosting/index.html", "/categories/webhosting/"),
    ("/tag/ubersetzung/index.html", "/categories/ubersetzung/"),
    ("/tag/google-webmaster-tools/index.html", "/categories/google-webmaster-tools/"),
    ("/tag/hauptseiten/index.html", "/categories/hauptseiten/"),
    ("/tag/radfahren/index.html", "/categories/radfahren/"),
    ("/tag/formular/index.html", "/categories/formular/"),
    ("/tag/k-9-mail/index.html", "/categories/k-9-mail/"),
    ("/tag/tetris/index.html", "/categories/tetris/"),
    ("/tag/reckless-racing/index.html", "/categories/reckless-racing/"),
    ("/tag/christmas-hd/index.html", "/categories/christmas-hd/"),
    ("/tag/notfall-sms/index.html", "/categories/notfall-sms/"),
    ("/tag/wirschaftswissenschaften/index.html", "/categories/wirschaftswissenschaften/"),
    ("/tag/clean-code/index.html", "/categories/clean-code/"),
    ("/tag/softwarepraktikum/index.html", "/categories/softwarepraktikum/"),
    ("/tag/kurzmitteilung/index.html", "/categories/kurzmitteilung/"),
    ("/tag/airsync/index.html", "/categories/airsync/"),
    ("/tag/alice/index.html", "/categories/alice/"),
    ("/tag/studium/index.html", "/categories/studium/"),
    ("/tag/odys/index.html", "/categories/odys/"),
    ("/tag/ubungsblatt/index.html", "/categories/ubungsblatt/"),
    ("/tag/fieldrunners-hd/index.html", "/categories/fieldrunners-hd/"),
    ("/tag/kommentare/index.html", "/categories/kommentare/"),
    ("/tag/nfl-rivals/index.html", "/categories/nfl-rivals/"),
    ("/tag/informatik/index.html", "/categories/informatik/"),
    ("/tag/horenswert/index.html", "/categories/horenswert/"),
    ("/tag/tacho/index.html", "/categories/tacho/"),
    ("/tag/musik/index.html", "/categories/musik/"),
    ("/tag/meinung/index.html", "/categories/meinung/"),
    ("/tag/blog/index.html", "/categories/blog/"),
    ("/tag/chaosradio/index.html", "/categories/chaosradio/"),
    (
        "/tag/seminar-neue-dienste-und-applikationen-im-zukunftigen-internet/index.html",
        "/categories/seminar-neue-dienste-und-applikationen-im-zukunftigen-internet/",
    ),
    ("/tag/sms-backup-+/index.html", "/categories/sms-backup-%2B/"),
    ("/tag/widgetlocker/index.html", "/categories/widgetlocker/"),
    ("/tag/sommersemester-2013/index.html", "/categories/sommersemester-2013/"),
    ("/tag/kommentar/index.html", "/categories/kommentar/"),
    ("/tag/linux-mint/index.html", "/categories/linux-mint/"),
    ("/tag/stundenplan-timetable-spread/index.html", "/categories/stundenplan-timetable-spread/"),
    ("/tag/versionsverwaltung/index.html", "/categories/versionsverwaltung/"),
    ("/tag/teslaled/index.html", "/categories/teslaled/"),
    ("/tag/informatik-studium/index.html", "/categories/informatik-studium/"),
    ("/tag/zeitreihenanalyse/index.html", "/categories/zeitreihenanalyse/"),
    ("/tag/download/index.html", "/categories/download/"),
    ("/tag/samsung-galaxy-s/index.html", "/categories/samsung-galaxy-s/"),
    ("/tag/tasker/index.html", "/categories/tasker/"),
    ("/tag/start-chart/index.html", "/categories/start-chart/"),
    ("/tag/rabatt/index.html", "/categories/rabatt/"),
    ("/tag/a+-timetable/index.html", "/categories/a%2B-timetable/"),
    ("/tag/graphite/index.html", "/categories/graphite/"),
    ("/tag/wordpress/index.html", "/categories/wordpress/"),
    ("/tag/juicedefender/index.html", "/categories/juicedefender/"),
    ("/tag/projekte/index.html", "/categories/projekte/"),
    ("/tag/sql/index.html", "/categories/sql/"),
    ("/tag/boblingen/index.html", "/categories/boblingen/"),
    ("/tag/all-inkl/index.html", "/categories/all-inkl/"),
    ("/tag/statusmitteilung/index.html", "/categories/statusmitteilung/"),
    ("/tag/amazon/index.html", "/categories/amazon/"),
    ("/tag/google-maps/index.html", "/categories/google-maps/"),
    ("/tag/sms-backup-amp-restore/index.html", "/categories/sms-backup-amp-restore/"),
    ("/tag/yoko/index.html", "/categories/yoko/"),
    ("/tag/pflichtenheft/index.html", "/categories/pflichtenheft/"),
    ("/tag/openwatch/index.html", "/categories/openwatch/"),
    ("/tag/git/index.html", "/categories/git/"),
    ("/tag/vorlesungsumfrage/index.html", "/categories/vorlesungsumfrage/"),
    ("/tag/sms/index.html", "/categories/sms/"),
    ("/tag/vortrag/index.html", "/categories/vortrag/"),
    ("/tag/data-mining/index.html", "/categories/data-mining/"),
    ("/tag/samsung/index.html", "/categories/samsung/"),
    ("/tag/problem/index.html", "/categories/problem/"),
    ("/tag/betriebssysteme/index.html", "/categories/betriebssysteme/"),
    ("/tag/sommersemester-2011/index.html", "/categories/sommersemester-2011/"),
    ("/tag/latex/index.html", "/categories/latex/"),
    ("/tag/youtube/index.html", "/categories/youtube/"),
    ("/tag/wintersemester-20122013/index.html", "/categories/wintersemester-20122013/"),
    ("/tag/informationsubertragung/index.html", "/categories/informationsubertragung/"),
    ("/tag/samsung-galaxy-nexus/index.html", "/categories/samsung-galaxy-nexus/"),
    ("/tag/umfrage/index.html", "/categories/umfrage/"),
    ("/tag/statistiken/index.html", "/categories/statistiken/"),
    ("/tag/docker/index.html", "/categories/docker/"),
    ("/tag/startups/index.html", "/categories/startups/"),
    ("/tag/screebl/index.html", "/categories/screebl/"),
    (
        "/tag/algorithmen-und-datenstrukturen/index.html",
        "/categories/algorithmen-und-datenstrukturen/",
    ),
    ("/tag/chrome-developer-tools/index.html", "/categories/chrome-developer-tools/"),
    ("/tag/video/index.html", "/categories/video/"),
    ("/tag/tastatur/index.html", "/categories/tastatur/"),
    ("/tag/kryptografie/index.html", "/categories/kryptografie/"),
    ("/tag/beyondpod/index.html", "/categories/beyondpod/"),
    ("/tag/android/index.html", "/categories/android/"),
    ("/tag/zendform/index.html", "/categories/zendform/"),
    ("/tag/java-programmierpraktikum/index.html", "/categories/java-programmierpraktikum/"),
    ("/tag/redundanz/index.html", "/categories/redundanz/"),
    ("/tag/tm/index.html", "/categories/tm/"),
    ("/tag/sketchbook-mobile/index.html", "/categories/sketchbook-mobile/"),
    ("/tag/google-chrome/index.html", "/categories/google-chrome/"),
    ("/tag/knime/index.html", "/categories/knime/"),
    ("/tag/uni-wurzburg/index.html", "/categories/uni-wurzburg/"),
    ("/tag/java-8/index.html", "/categories/java-8/"),
    ("/tag/vorlesung/index.html", "/categories/vorlesung/"),
    ("/tag/bedtime-battle/index.html", "/categories/bedtime-battle/"),
    ("/tag/ice-cream-sandwich/index.html", "/categories/ice-cream-sandwich/"),
    ("/tag/coby-kyros-mid-7022/index.html", "/categories/coby-kyros-mid-7022/"),
    ("/tag/klausur/index.html", "/categories/klausur/"),
    ("/tag/coby/index.html", "/categories/coby/"),
    ("/tag/komplexe-zahlen/index.html", "/categories/komplexe-zahlen/"),
    ("/tag/data-mining-cup-2014/index.html", "/categories/data-mining-cup-2014/"),
    ("/tag/dont-repeat-yourself/index.html", "/categories/dont-repeat-yourself/"),
    ("/tag/soundhound/index.html", "/categories/soundhound/"),
    ("/tag/gentle-alarm/index.html", "/categories/gentle-alarm/"),
    ("/tag/lenovo-a1/index.html", "/categories/lenovo-a1/"),
    ("/tag/erlebnisbericht/index.html", "/categories/erlebnisbericht/"),
    ("/tag/compiler/index.html", "/categories/compiler/"),
    ("/tag/matlab/index.html", "/categories/matlab/"),
    ("/tag/seminar/index.html", "/categories/seminar/"),
    ("/tag/follow-up/index.html", "/categories/follow-up/"),
    ("/tag/timetable++/index.html", "/categories/timetable%2B%2B/"),
    (
        "/tag/rechnernetze-und-kommunikationssysteme/index.html",
        "/categories/rechnernetze-und-kommunikationssysteme/",
    ),
    ("/tag/opentsdb/index.html", "/categories/opentsdb/"),
    ("/tag/seo/index.html", "/categories/seo/"),
    ("/tag/rechenanlagen/index.html", "/categories/rechenanlagen/"),
    ("/tag/workaround/index.html", "/categories/workaround/"),
    ("/tag/bachelor/index.html", "/categories/bachelor/"),
    ("/tag/twenty-eleven/index.html", "/categories/twenty-eleven/"),
    ("/tag/datenbanken/index.html", "/categories/datenbanken/"),
    ("/tag/auswertung/index.html", "/categories/auswertung/"),
    ("/tag/app-der-woche/index.html", "/categories/app-der-woche/"),
    ("/tag/fruit-ninja/index.html", "/categories/fruit-ninja/"),
    ("/tag/twenty-twelve/index.html", "/categories/twenty-twelve/"),
    ("/tag/nachklausur/index.html", "/categories/nachklausur/"),
    ("/tag/lesenswert/index.html", "/categories/lesenswert/"),
    ("/tag/vimeo/index.html", "/categories/vimeo/"),
    ("/tag/glasser/index.html", "/categories/glasser/"),
    ("/tag/python/index.html", "/categories/python/"),
    ("/tag/spss-modeler/index.html", "/categories/spss-modeler/"),
    ("/tag/mehrwert/index.html", "/categories/mehrwert/"),
    (
        "/tag/einfuhrung-in-die-volkswirtschaftslehre-fur-nichtwirtschaftswissenschaftler/index.html",
        "/categories/einfuhrung-in-die-volkswirtschaftslehre-fur-nichtwirtschaftswissenschaftler/",
    ),
    ("/tag/review/index.html", "/categories/review/"),
    ("/tag/twenty-ten/index.html", "/categories/twenty-ten/"),
    ("/tag/ram/index.html", "/categories/ram/"),
    ("/tag/musterlosung/index.html", "/categories/musterlosung/"),
    ("/tag/link/index.html", "/categories/link/"),
    ("/tag/dropbox/index.html", "/categories/dropbox/"),
    ("/tag/in-eigener-sache/index.html", "/categories/in-eigener-sache/"),
    ("/tag/tablet/index.html", "/categories/tablet/"),
    ("/tag/vorlesungscharts/index.html", "/categories/vorlesungscharts/"),
    ("/tag/prometheus/index.html", "/categories/prometheus/"),
    ("/tag/isyncr/index.html", "/categories/isyncr/"),
    ("/tag/dry/index.html", "/categories/dry/"),
    ("/tag/remote-notifier/index.html", "/categories/remote-notifier/"),
    ("/tag/semesterferien/index.html", "/categories/semesterferien/"),
    ("/tag/gps/index.html", "/categories/gps/"),
    ("/tag/wintersemester-20112012/index.html", "/categories/wintersemester-20112012/"),
    ("/tag/beautiful-widgets/index.html", "/categories/beautiful-widgets/"),
    ("/tag/read-it-later/index.html", "/categories/read-it-later/"),
    ("/tag/influxdb/index.html", "/categories/influxdb/"),
]


# Presets of commands to execute to deploy. Can be anything, for
# example, you may use rsync:
# "rsync -rav --delete output/ joe@my.site:/srv/www/site"
# And then do a backup, or run `nikola ping` from the `ping`
# plugin (`nikola plugin -i ping`).  Or run `nikola check -l`.
# You may also want to use github_deploy (see below).
# You can define multiple presets and specify them as arguments
# to `nikola deploy`.  If no arguments are specified, a preset
# named `default` will be executed.  You can use as many presets
# in a `nikola deploy` command as you like.
# DEPLOY_COMMANDS = {
#     'default': [
#         "rsync -rav --delete output/ joe@my.site:/srv/www/site",
#     ]
# }

# github_deploy configuration
# For more details, read the manual:
# https://getnikola.com/handbook.html#deploying-to-github
# You will need to configure the deployment branch on GitHub.
GITHUB_SOURCE_BRANCH = "src"
GITHUB_DEPLOY_BRANCH = "master"

# The name of the remote where you wish to push to, using github_deploy.
GITHUB_REMOTE_NAME = "origin"

# Whether or not github_deploy should commit to the source branch automatically
# before deploying.
GITHUB_COMMIT_SOURCE = True

# Where the output site should be located
# If you don't use an absolute path, it will be considered as relative
# to the location of conf.py
# OUTPUT_FOLDER = 'output'

# where the "cache" of partial generated content should be located
# default: 'cache'
# CACHE_FOLDER = 'cache'

# Filters to apply to the output.
# A directory where the keys are either: a file extensions, or
# a tuple of file extensions.
#
# And the value is a list of commands to be applied in order.
#
# Each command must be either:
#
# A string containing a '%s' which will
# be replaced with a filename. The command *must* produce output
# in place.
#
# Or:
#
# A python callable, which will be called with the filename as
# argument.
#
# By default, only .php files uses filters to inject PHP into
# Nikola’s templates. All other filters must be enabled through FILTERS.
#
# Many filters are shipped with Nikola. A list is available in the manual:
# <https://getnikola.com/handbook.html#post-processing-filters>
#
# from nikola import filters
# FILTERS = {
#    ".html": [filters.typogrify],
#    ".js": [filters.closure_compiler],
#    ".jpg": ["jpegoptim --strip-all -m75 -v %s"],
# }

# Executable for the "yui_compressor" filter (defaults to 'yui-compressor').
# YUI_COMPRESSOR_EXECUTABLE = 'yui-compressor'

# Executable for the "closure_compiler" filter (defaults to 'closure-compiler').
# CLOSURE_COMPILER_EXECUTABLE = 'closure-compiler'

# Executable for the "optipng" filter (defaults to 'optipng').
# OPTIPNG_EXECUTABLE = 'optipng'

# Executable for the "jpegoptim" filter (defaults to 'jpegoptim').
# JPEGOPTIM_EXECUTABLE = 'jpegoptim'

# Executable for the "html_tidy_withconfig", "html_tidy_nowrap",
# "html_tidy_wrap", "html_tidy_wrap_attr" and "html_tidy_mini" filters
# (defaults to 'tidy5').
# HTML_TIDY_EXECUTABLE = 'tidy5'

# List of XPath expressions which should be used for finding headers
# ({hx} is replaced by headers h1 through h6).
# You must change this if you use a custom theme that does not use
# "e-content entry-content" as a class for post and page contents.
# HEADER_PERMALINKS_XPATH_LIST = ['*//div[@class="e-content entry-content"]//{hx}']
# Include *every* header (not recommended):
# HEADER_PERMALINKS_XPATH_LIST = ['*//{hx}']

# File blacklist for header permalinks. Contains output path
# (eg. 'output/index.html')
# HEADER_PERMALINKS_FILE_BLACKLIST = []

# Expert setting! Create a gzipped copy of each generated file. Cheap server-
# side optimization for very high traffic sites or low memory servers.
# GZIP_FILES = False
# File extensions that will be compressed
# GZIP_EXTENSIONS = ('.txt', '.htm', '.html', '.css', '.js', '.json', '.atom', '.xml')
# Use an external gzip command? None means no.
# Example: GZIP_COMMAND = "pigz -k {filename}"
# GZIP_COMMAND = None
# Make sure the server does not return a "Accept-Ranges: bytes" header for
# files compressed by this option! OR make sure that a ranged request does not
# return partial content of another representation for these resources. Do not
# use this feature if you do not understand what this means.

# #############################################################################
# Image Gallery Options
# #############################################################################

# One or more folders containing galleries. The format is a dictionary of
# {"source": "relative_destination"}, where galleries are looked for in
# "source/" and the results will be located in
# "OUTPUT_PATH/relative_destination/gallery_name"
# Default is:
# GALLERY_FOLDERS = {"galleries": "galleries"}
# More gallery options:
# THUMBNAIL_SIZE = 180
# MAX_IMAGE_SIZE = 1280
# USE_FILENAME_AS_TITLE = True
# EXTRA_IMAGE_EXTENSIONS = []
#
# If set to False, it will sort by filename instead. Defaults to True
# GALLERY_SORT_BY_DATE = True

# If set to True, EXIF data will be copied when an image is thumbnailed or
# resized. (See also EXIF_WHITELIST)
# PRESERVE_EXIF_DATA = False

# If you have enabled PRESERVE_EXIF_DATA, this option lets you choose EXIF
# fields you want to keep in images. (See also PRESERVE_EXIF_DATA)
#
# For a full list of field names, please see here:
# http://www.cipa.jp/std/documents/e/DC-008-2012_E.pdf
#
# This is a dictionary of lists. Each key in the dictionary is the
# name of a IDF, and each list item is a field you want to preserve.
# If you have a IDF with only a '*' item, *EVERY* item in it will be
# preserved. If you don't want to preserve anything in a IDF, remove it
# from the setting. By default, no EXIF information is kept.
# Setting the whitelist to anything other than {} implies
# PRESERVE_EXIF_DATA is set to True
# To preserve ALL EXIF data, set EXIF_WHITELIST to {"*": "*"}

# EXIF_WHITELIST = {}

# Some examples of EXIF_WHITELIST settings:

# Basic image information:
# EXIF_WHITELIST['0th'] = [
#    "Orientation",
#    "XResolution",
#    "YResolution",
# ]

# If you want to keep GPS data in the images:
# EXIF_WHITELIST['GPS'] = ["*"]

# Embedded thumbnail information:
# EXIF_WHITELIST['1st'] = ["*"]

# If set to True, any ICC profile will be copied when an image is thumbnailed or
# resized.
# PRESERVE_ICC_PROFILES = False

# Folders containing images to be used in normal posts or pages.
# IMAGE_FOLDERS is a dictionary of the form {"source": "destination"},
# where "source" is the folder containing the images to be published, and
# "destination" is the folder under OUTPUT_PATH containing the images copied
# to the site. Thumbnail images will be created there as well.

# To reference the images in your posts, include a leading slash in the path.
# For example, if IMAGE_FOLDERS = {'images': 'images'}, write
#
#   .. image:: /images/tesla.jpg
#
# See the Nikola Handbook for details (in the “Embedding Images” and
# “Thumbnails” sections)

# Images will be scaled down according to IMAGE_THUMBNAIL_SIZE and MAX_IMAGE_SIZE
# options, but will have to be referenced manually to be visible on the site
# (the thumbnail has ``.thumbnail`` added before the file extension by default,
# but a different naming template can be configured with IMAGE_THUMBNAIL_FORMAT).

IMAGE_FOLDERS = {"images": "images"}
# IMAGE_THUMBNAIL_SIZE = 400
# IMAGE_THUMBNAIL_FORMAT = '{name}.thumbnail{ext}'

# #############################################################################
# HTML fragments and diverse things that are used by the templates
# #############################################################################

# Data about post-per-page indexes.
# INDEXES_PAGES defaults to ' old posts, page %d' or ' page %d' (translated),
# depending on the value of INDEXES_PAGES_MAIN.
#
# (translatable) If the following is empty, defaults to BLOG_TITLE:
# INDEXES_TITLE = ""
#
# (translatable) If the following is empty, defaults to ' [old posts,] page %d' (see above):
# INDEXES_PAGES = ""
#
# If the following is True, INDEXES_PAGES is also displayed on the main (the
# newest) index page (index.html):
# INDEXES_PAGES_MAIN = False
#
# If the following is True, index-1.html has the oldest posts, index-2.html the
# second-oldest posts, etc., and index.html has the newest posts. This ensures
# that all posts on index-x.html will forever stay on that page, now matter how
# many new posts are added.
# If False, index-1.html has the second-newest posts, index-2.html the third-newest,
# and index-n.html the oldest posts. When this is active, old posts can be moved
# to other index pages when new posts are added.
# INDEXES_STATIC = True
#
# (translatable) If PRETTY_URLS is set to True, this setting will be used to create
# prettier URLs for index pages, such as page/2/index.html instead of index-2.html.
# Valid values for this settings are:
#   * False,
#   * a list or tuple, specifying the path to be generated,
#   * a dictionary mapping languages to lists or tuples.
# Every list or tuple must consist of strings which are used to combine the path;
# for example:
#     ['page', '{number}', '{index_file}']
# The replacements
#     {number}     --> (logical) page number;
#     {old_number} --> the page number inserted into index-n.html before (zero for
#                      the main page);
#     {index_file} --> value of option INDEX_FILE
# are made.
# Note that in case INDEXES_PAGES_MAIN is set to True, a redirection will be created
# for the full URL with the page number of the main page to the normal (shorter) main
# page URL.
# INDEXES_PRETTY_PAGE_URL = False
#
# If the following is true, a page range navigation will be inserted to indices.
# Please note that this will undo the effect of INDEXES_STATIC, as all index pages
# must be recreated whenever the number of pages changes.
# SHOW_INDEX_PAGE_NAVIGATION = False

# If the following is True, a meta name="generator" tag is added to pages. The
# generator tag is used to specify the software used to generate the page
# (it promotes Nikola).
# META_GENERATOR_TAG = True

# Color scheme to be used for code blocks. If your theme provides
# "assets/css/code.css" this is ignored. Set to None to disable.
# Can be any of:
# algol, algol_nu, autumn, borland, bw, colorful, default, emacs, friendly,
# fruity, igor, lovelace, manni, monokai, murphy, native, paraiso-dark,
# paraiso-light, pastie, perldoc, rrt, tango, trac, vim, vs, xcode
# This list MAY be incomplete since pygments adds styles every now and then.
# Check with list(pygments.styles.get_all_styles()) in an interpreter.
#
# CODE_COLOR_SCHEME = 'default'

# FAVICONS contains (name, file, size) tuples.
# Used to create favicon link like this:
# <link rel="name" href="file" sizes="size"/>
# FAVICONS = (
#     ("icon", "/favicon.ico", "16x16"),
#     ("icon", "/icon_128x128.png", "128x128"),
# )

# Show teasers (instead of full posts) in indexes? Defaults to False.
INDEX_TEASERS = False

# HTML fragments with the Read more... links.
# The following tags exist and are replaced for you:
# {link}                        A link to the full post page.
# {read_more}                   The string “Read more” in the current language.
# {reading_time}                An estimate of how long it will take to read the post.
# {remaining_reading_time}      An estimate of how long it will take to read the post, sans the teaser.
# {min_remaining_read}          The string “{remaining_reading_time} min remaining to read” in the current language.
# {paragraph_count}             The amount of paragraphs in the post.
# {remaining_paragraph_count}   The amount of paragraphs in the post, sans the teaser.
# {post_title}                  The title of the post.
# {{                            A literal { (U+007B LEFT CURLY BRACKET)
# }}                            A literal } (U+007D RIGHT CURLY BRACKET)

# 'Read more...' for the index page, if INDEX_TEASERS is True (translatable)
INDEX_READ_MORE_LINK = '<p class="more"><a href="{link}">{read_more}…</a></p>'
# 'Read more...' for the feeds, if FEED_TEASERS is True (translatable)
FEED_READ_MORE_LINK = '<p><a href="{link}">{read_more}…</a> ({min_remaining_read})</p>'

# Append a URL query to the FEED_READ_MORE_LINK in Atom and RSS feeds. Advanced
# option used for traffic source tracking.
# Minimum example for use with Piwik: "pk_campaign=feed"
# The following tags exist and are replaced for you:
# {feedRelUri}                  A relative link to the feed.
# {feedFormat}                  The name of the syndication format.
# Example using replacement for use with Google Analytics:
# "utm_source={feedRelUri}&utm_medium=nikola_feed&utm_campaign={feedFormat}_feed"
FEED_LINKS_APPEND_QUERY = False

# A HTML fragment describing the license, for the sidebar.
# (translatable)
LICENSE = ""
# I recommend using the Creative Commons' wizard:
# https://creativecommons.org/choose/
# LICENSE = """
# <a rel="license" href="https://creativecommons.org/licenses/by-nc-sa/4.0/">
# <img alt="Creative Commons License BY-NC-SA"
# style="border-width:0; margin-bottom:12px;"
# src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png"></a>"""

# A small copyright notice for the page footer (in HTML).
# (translatable)
CONTENT_FOOTER = '&copy; {date} by <a href="https://karllorey.com">{author}</a> - Powered by <a href="https://getnikola.com" rel="nofollow">Nikola</a> {license}'

# Things that will be passed to CONTENT_FOOTER.format().  This is done
# for translatability, as dicts are not formattable.  Nikola will
# intelligently format the setting properly.
# The setting takes a dict. The keys are languages. The values are
# tuples of tuples of positional arguments and dicts of keyword arguments
# to format().  For example, {'en': (('Hello'), {'target': 'World'})}
# results in CONTENT_FOOTER['en'].format('Hello', target='World').
# If you need to use the literal braces '{' and '}' in your footer text, use
# '{{' and '}}' to escape them (str.format is used)
# WARNING: If you do not use multiple languages with CONTENT_FOOTER, this
#          still needs to be a dict of this format.  (it can be empty if you
#          do not need formatting)
# (translatable)
CONTENT_FOOTER_FORMATS = {
    DEFAULT_LANG: (
        (),
        {
            "email": BLOG_EMAIL,
            "author": BLOG_AUTHOR,
            "date": time.gmtime().tm_year,
            "license": LICENSE,
        },
    )
}

# A simple copyright tag for inclusion in RSS feeds that works just
# like CONTENT_FOOTER and CONTENT_FOOTER_FORMATS
RSS_COPYRIGHT = 'Contents © {date} <a href="mailto:{email}">{author}</a> {license}'
RSS_COPYRIGHT_PLAIN = "Contents © {date} {author} {license}"
RSS_COPYRIGHT_FORMATS = CONTENT_FOOTER_FORMATS

# To use comments, you can choose between different third party comment
# systems.  The following comment systems are supported by Nikola:
#   disqus, facebook, intensedebate, isso, muut, commento
# You can leave this option blank to disable comments.
COMMENT_SYSTEM = ""
# And you also need to add your COMMENT_SYSTEM_ID which
# depends on what comment system you use. The default is
# "nikolademo" which is a test account for Disqus. More information
# is in the manual.
# COMMENT_SYSTEM_ID = "nikolademo"

# Create index.html for page folders?
# WARNING: if a page would conflict with the index file (usually
#          caused by setting slug to `index`), the PAGE_INDEX
#          will not be generated for that directory.
# PAGE_INDEX = False
# Enable comments on pages (i.e. not posts)?
# COMMENTS_IN_PAGES = False
# Enable comments on picture gallery pages?
# COMMENTS_IN_GALLERIES = False

# What file should be used for directory indexes?
# Defaults to index.html
# Common other alternatives: default.html for IIS, index.php
# INDEX_FILE = "index.html"

# If a link ends in /index.html,  drop the index.html part.
# http://mysite/foo/bar/index.html => http://mysite/foo/bar/
# (Uses the INDEX_FILE setting, so if that is, say, default.html,
# it will instead /foo/default.html => /foo)
STRIP_INDEXES = True

# List of files relative to the server root (!) that will be asked to be excluded
# from indexing and other robotic spidering. * is supported. Will only be effective
# if SITE_URL points to server root. The list is used to exclude resources from
# /robots.txt and /sitemap.xml, and to inform search engines about /sitemapindex.xml.
# ROBOTS_EXCLUSIONS = ["/archive.html", "/category/*.html"]

# Instead of putting files in <slug>.html, put them in <slug>/index.html.
# No web server configuration is required. Also enables STRIP_INDEXES.
# This can be disabled on a per-page/post basis by adding
#    .. pretty_url: False
# to the metadata.
PRETTY_URLS = True

# If True, publish future dated posts right away instead of scheduling them.
# Defaults to False.
# FUTURE_IS_NOW = False

# If True, future dated posts are allowed in deployed output
# Only the individual posts are published/deployed; not in indexes/sitemap
# Generally, you want FUTURE_IS_NOW and DEPLOY_FUTURE to be the same value.
# DEPLOY_FUTURE = False
# If False, draft posts will not be deployed
# DEPLOY_DRAFTS = True

# Allows scheduling of posts using the rule specified here (new_post -s)
# Specify an iCal Recurrence Rule: http://www.kanzaki.com/docs/ical/rrule.html
# SCHEDULE_RULE = ''
# If True, use the scheduling rule to all posts (not pages!) by default
# SCHEDULE_ALL = False

# Do you want a add a Mathjax config file?
# MATHJAX_CONFIG = ""

# If you want support for the $.$ syntax (which may conflict with running
# text!), just use this config:
# MATHJAX_CONFIG = """
# <script type="text/x-mathjax-config">
# MathJax.Hub.Config({
#     tex2jax: {
#         inlineMath: [ ['$','$'], ["\\\(","\\\)"] ],
#         displayMath: [ ['$$','$$'], ["\\\[","\\\]"] ],
#         processEscapes: true
#     },
#     displayAlign: 'center', // Change this to 'left' if you want left-aligned equations.
#     "HTML-CSS": {
#         styles: {'.MathJax_Display': {"margin": 0}}
#     }
# });
# </script>
# """

# Want to use KaTeX instead of MathJax? While KaTeX may not support every
# feature yet, it's faster and the output looks better.
# USE_KATEX = False

# KaTeX auto-render settings. If you want support for the $.$ syntax (which may
# conflict with running text!), just use this config:
# KATEX_AUTO_RENDER = """
# delimiters: [
#     {left: "$$", right: "$$", display: true},
#     {left: "\\\\[", right: "\\\\]", display: true},
#     {left: "\\\\begin{equation*}", right: "\\\\end{equation*}", display: true},
#     {left: "$", right: "$", display: false},
#     {left: "\\\\(", right: "\\\\)", display: false}
# ]
# """

# Do you want to customize the nbconversion of your IPython notebook?
# IPYNB_CONFIG = {}
# With the following example configuration you can use a custom jinja template
# called `toggle.tpl` which has to be located in your site/blog main folder:
# IPYNB_CONFIG = {'Exporter': {'template_file': 'toggle'}}

# What Markdown extensions to enable?
# You will also get gist, nikola and podcast because those are
# done in the code, hope you don't mind ;-)
# Note: most Nikola-specific extensions are done via the Nikola plugin system,
#       with the MarkdownExtension class and should not be added here.
# Defaults are markdown.extensions.(fenced_code|codehilite|extra)
# markdown.extensions.meta is required for Markdown metadata.
MARKDOWN_EXTENSIONS = [
    "markdown.extensions.fenced_code",
    "markdown.extensions.codehilite",
    "markdown.extensions.extra",
]

# Options to be passed to markdown extensions (See https://python-markdown.github.io/reference/)
# Default is {} (no config at all)
# MARKDOWN_EXTENSION_CONFIGS = {}


# Extra options to pass to the pandoc command.
# by default, it's empty, is a list of strings, for example
# ['-F', 'pandoc-citeproc', '--bibliography=/Users/foo/references.bib']
# Pandoc does not demote headers by default.  To enable this, you can use, for example
# ['--base-header-level=2']
# PANDOC_OPTIONS = []

# Social buttons. This is sample code for AddThis (which was the default for a
# long time). Insert anything you want here, or even make it empty (which is
# the default right now)
# (translatable)
# SOCIAL_BUTTONS_CODE = """
# <!-- Social buttons -->
# <div id="addthisbox" class="addthis_toolbox addthis_peekaboo_style addthis_default_style addthis_label_style addthis_32x32_style">
# <a class="addthis_button_more">Share</a>
# <ul><li><a class="addthis_button_facebook"></a>
# <li><a class="addthis_button_google_plusone_share"></a>
# <li><a class="addthis_button_linkedin"></a>
# <li><a class="addthis_button_twitter"></a>
# </ul>
# </div>
# <script src="https://s7.addthis.com/js/300/addthis_widget.js#pubid=ra-4f7088a56bb93798"></script>
# <!-- End of social buttons -->
# """

# Show link to source for the posts?
# SHOW_SOURCELINK = True
# Copy the source files for your pages?
# Setting it to False implies SHOW_SOURCELINK = False
# COPY_SOURCES = True

# Modify the number of Post per Index Page
# Defaults to 10
# INDEX_DISPLAY_POST_COUNT = 10

# By default, Nikola generates RSS files for the website and for tags, and
# links to it.  Set this to False to disable everything RSS-related.
# GENERATE_RSS = True

# By default, Nikola does not generates Atom files for indexes and links to
# them. Generate Atom for tags by setting TAG_PAGES_ARE_INDEXES to True.
# Atom feeds are built based on INDEX_DISPLAY_POST_COUNT and not FEED_LENGTH
# Switch between plain-text summaries and full HTML content using the
# FEED_TEASER option. FEED_LINKS_APPEND_QUERY is also respected. Atom feeds
# are generated even for old indexes and have pagination link relations
# between each other. Old Atom feeds with no changes are marked as archived.
# GENERATE_ATOM = False

# Only include teasers in Atom and RSS feeds. Disabling include the full
# content. Defaults to True.
# FEED_TEASERS = True

# Strip HTML from Atom and RSS feed summaries and content. Defaults to False.
# FEED_PLAIN = False

# Number of posts in Atom and RSS feeds.
# FEED_LENGTH = 10

# RSS_LINK is a HTML fragment to link the RSS or Atom feeds. If set to None,
# the base.tmpl will use the feed Nikola generates. However, you may want to
# change it for a FeedBurner feed or something else.
# RSS_LINK = None

# A search form to search this site, for the sidebar. You can use a Google
# custom search (https://www.google.com/cse/)
# Or a DuckDuckGo search: https://duckduckgo.com/search_box.html
# Default is no search form.
# (translatable)
# SEARCH_FORM = ""
#
# This search form works for any site and looks good in the "site" theme where
# it appears on the navigation bar:
#
# SEARCH_FORM = """
# <!-- DuckDuckGo custom search -->
# <form method="get" id="search" action="https://duckduckgo.com/"
#  class="navbar-form pull-left">
# <input type="hidden" name="sites" value="%s">
# <input type="hidden" name="k8" value="#444444">
# <input type="hidden" name="k9" value="#D51920">
# <input type="hidden" name="kt" value="h">
# <input type="text" name="q" maxlength="255"
#  placeholder="Search&hellip;" class="span2" style="margin-top: 4px;">
# <input type="submit" value="DuckDuckGo Search" style="visibility: hidden;">
# </form>
# <!-- End of custom search -->
# """ % SITE_URL
#
# If you prefer a Google search form, here's an example that should just work:
# SEARCH_FORM = """
# <!-- Google custom search -->
# <form method="get" action="https://www.google.com/search" class="navbar-form navbar-right" role="search">
# <div class="form-group">
# <input type="text" name="q" class="form-control" placeholder="Search">
# </div>
# <button type="submit" class="btn btn-primary">
# 	<span class="glyphicon glyphicon-search"></span>
# </button>
# <input type="hidden" name="sitesearch" value="%s">
# </form>
# <!-- End of custom search -->
# """ % SITE_URL

# Use content distribution networks for jQuery, twitter-bootstrap css and js,
# and html5shiv (for older versions of Internet Explorer)
# If this is True, jQuery and html5shiv are served from the Google CDN and
# Bootstrap is served from BootstrapCDN (provided by MaxCDN)
# Set this to False if you want to host your site without requiring access to
# external resources.
# USE_CDN = False

# Check for USE_CDN compatibility.
# If you are using custom themes, have configured the CSS properly and are
# receiving warnings about incompatibility but believe they are incorrect, you
# can set this to False.
# USE_CDN_WARNING = True

# Extra things you want in the pages HEAD tag. This will be added right
# before </head>
# (translatable)
# EXTRA_HEAD_DATA = ""
# Google Analytics or whatever else you use. Added to the bottom of <body>
# in the default template (base.tmpl).
# (translatable)
# BODY_END = ""

# The possibility to extract metadata from the filename by using a
# regular expression.
# To make it work you need to name parts of your regular expression.
# The following names will be used to extract metadata:
# - title
# - slug
# - date
# - tags
# - link
# - description
#
# An example re is the following:
# '.*\/(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)-(?P<title>.*)\.rst'
# (Note the '.*\/' in the beginning -- matches source paths relative to conf.py)
# FILE_METADATA_REGEXP = None

# Should titles fetched from file metadata be unslugified (made prettier?)
# FILE_METADATA_UNSLUGIFY_TITLES = True

# If enabled, extract metadata from docinfo fields in reST documents.
# If your text files start with a level 1 heading, it will be treated as the
# document title and will be removed from the text.
# USE_REST_DOCINFO_METADATA = False

# If enabled, hide docinfo fields in reST document output
# HIDE_REST_DOCINFO = False

# Map metadata from other formats to Nikola names.
# Supported formats: yaml, toml, rest_docinfo, markdown_metadata
# METADATA_MAPPING = {}
#
# Example for Pelican compatibility:
# METADATA_MAPPING = {
#     "rest_docinfo": {"summary": "description", "modified": "updated"},
#     "markdown_metadata": {"summary": "description", "modified": "updated"}
# }
# Other examples: https://getnikola.com/handbook.html#mapping-metadata-from-other-formats

# Map metadata between types/values. (Runs after METADATA_MAPPING.)
# Supported formats: nikola, yaml, toml, rest_docinfo, markdown_metadata
# The value on the right should be a dict of callables.
# METADATA_VALUE_MAPPING = {}
# Examples:
# METADATA_VALUE_MAPPING = {
#     "yaml": {"keywords": lambda value: ', '.join(value)},  # yaml: 'keywords' list -> str
#     "nikola": {
#         "widgets": lambda value: value.split(', '),  # nikola: 'widgets' comma-separated string -> list
#         "tags": str.lower  # nikola: force lowercase 'tags' (input would be string)
#      }
# }

# Additional metadata that is added to a post when creating a new_post
# ADDITIONAL_METADATA = {}

# Nikola supports Twitter Card summaries, but they are disabled by default.
# They make it possible for you to attach media to Tweets that link
# to your content.
#
# Uncomment and modify to following lines to match your accounts.
# Images displayed come from the `previewimage` meta tag.
# You can specify the card type by using the `card` parameter in TWITTER_CARD.
# TWITTER_CARD = {
#     # 'use_twitter_cards': True,  # enable Twitter Cards
#     # 'card': 'summary',          # Card type, you can also use 'summary_large_image',
#                                   # see https://dev.twitter.com/cards/types
#     # 'site': '@website',         # twitter nick for the website
#     # 'creator': '@username',     # Username for the content creator / author.
# }

# Bundle JS and CSS into single files to make site loading faster in a HTTP/1.1
# environment but is not recommended for HTTP/2.0 when caching is used.
# Defaults to True.
# USE_BUNDLES = True

# Plugins you don't want to use. Be careful :-)
# DISABLED_PLUGINS = ["render_galleries"]

# Special settings to disable only parts of the indexes plugin.
# Use with care.
# DISABLE_INDEXES = False
# DISABLE_MAIN_ATOM_FEED = False
# DISABLE_MAIN_RSS_FEED = False

# Add the absolute paths to directories containing plugins to use them.
# For example, the `plugins` directory of your clone of the Nikola plugins
# repository.
# EXTRA_PLUGINS_DIRS = []

# Add the absolute paths to directories containing themes to use them.
# For example, the `v7` directory of your clone of the Nikola themes
# repository.
# EXTRA_THEMES_DIRS = []

# List of regular expressions, links matching them will always be considered
# valid by "nikola check -l"
# LINK_CHECK_WHITELIST = []

# If set to True, enable optional hyphenation in your posts (requires pyphen)
# Enabling hyphenation has been shown to break math support in some cases,
# use with caution.
# HYPHENATE = False

# The <hN> tags in HTML generated by certain compilers (reST/Markdown)
# will be demoted by that much (1 → h1 will become h2 and so on)
# This was a hidden feature of the Markdown and reST compilers in the
# past.  Useful especially if your post titles are in <h1> tags too, for
# example.
# (defaults to 1.)
# DEMOTE_HEADERS = 1

# If you don’t like slugified file names ([a-z0-9] and a literal dash),
# and would prefer to use all the characters your file system allows.
# USE WITH CARE!  This is also not guaranteed to be perfect, and may
# sometimes crash Nikola, your web server, or eat your cat.
# USE_SLUGIFY = True

# If set to True, the tags 'draft', 'mathjax' and 'private' have special
# meaning. If set to False, these tags are handled like regular tags.
USE_TAG_METADATA = False

# If set to True, a warning is issued if one of the 'draft', 'mathjax'
# and 'private' tags are found in a post. Useful for checking that
# migration was successful.
WARN_ABOUT_TAG_METADATA = False

# Templates will use those filters, along with the defaults.
# Consult your engine's documentation on filters if you need help defining
# those.
# TEMPLATE_FILTERS = {}

# Put in global_context things you want available on all your templates.
# It can be anything, data, functions, modules, etc.
GLOBAL_CONTEXT = {}

# Add functions here and they will be called with template
# GLOBAL_CONTEXT as parameter when the template is about to be
# rendered
GLOBAL_CONTEXT_FILLER = []
