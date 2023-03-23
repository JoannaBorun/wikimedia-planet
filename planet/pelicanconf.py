#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Wikimedia Foundation'
SITENAME = 'Wikimedia Planet'
SITEURL = ''

PATH = '../docs'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
)

# Social widget
SOCIAL = (
)

DEFAULT_PAGINATION = 10

# RSS planet
PLUGINS = [
	'pelican_planet',
]

# https://pypi.org/project/pelican-planet/
PLANET_FEEDS = {
    "brionv.com": "https://brionv.com/log/feed/",
    "arnomane.wordpress.com": "https://arnomane.wordpress.com/category/wiki-en/feed/atom/",
    "davidgerard.co.uk": "https://davidgerard.co.uk/notes/category/wiki/feed/",
    "dom.as": "https://dom.as/category/wikitech/feed/",
    "original-research.blogspot.com": "https://original-research.blogspot.com/feeds/posts/default/-/wikipedia",
    "ragesoss.com": "https://ragesoss.com/category/wikipedia/feed/",
    "titoxd.blogspot.com": "https://titoxd.blogspot.com/feeds/posts/default/-/wiki",
    "wikinewsreports.blogspot.com": "https://wikinewsreports.blogspot.com/feeds/posts/default",
    "thoughtsfordeletion.blogspot.com": "https://thoughtsfordeletion.blogspot.com/feeds/posts/default",
    "bookcraft.blogspot.com": "https://bookcraft.blogspot.com/feeds/posts/default",
    "gpollard.wordpress.com": "https://gpollard.wordpress.com/category/wiki/feed/atom/",
    "reagle.org": "https://reagle.org/joseph/pelican/feeds/all.atom.xml",
    "feeds.feedburner.com": "https://feeds.feedburner.com/WikipediaNotesFromWwwwolf",
    "moononastick.com": "https://moononastick.com/blog/feed/?cat=4",
    "mako.cc": "https://mako.cc/copyrighteous/tags/planetwikimedia/feed/atom",
    "dialogicality.blogspot.com": "https://dialogicality.blogspot.com/feeds/posts/default/-/wiki",
    "rauterkus.blogspot.com": "https://rauterkus.blogspot.com/feeds/posts/default/-/wiki",
    "ultimategerardm.blogspot.com": "https://ultimategerardm.blogspot.com/feeds/posts/default/",
    "millosh.wordpress.com": "https://millosh.wordpress.com/tag/wikimedia/feed/atom/",
    "feeds.feedburner.com": "https://feeds.feedburner.com/remotewiki",
    "wikibooks.blogspot.com": "https://wikibooks.blogspot.com/feeds/posts/default",
    "wikinortheast.blogspot.com": "https://wikinortheast.blogspot.com/feeds/posts/default",
    "guillaumepaumier.com": "https://guillaumepaumier.com/category/wikimedia/feed/",
    "mikeswikidev.wordpress.com": "https://mikeswikidev.wordpress.com/category/technical-on-topic/feed/atom/",
    "lunasantin.blogspot.com": "https://lunasantin.blogspot.com/feeds/posts/default/-/wikimedia",
    "blog.sebmol.me": "https://blog.sebmol.me/category/wikimedia-en/feed/",
    "www.nointrigue.com": "https://www.nointrigue.com/blog/category/wikipedia/feed/",
    "brianna.modernthings.org": "http://brianna.modernthings.org/atom/?section=article",
    "majorlyhot.blogspot.com": "https://majorlyhot.blogspot.com/feeds/posts/default/-/wikipedia",
    "writingwithintherules.blogspot.com": "https://writingwithintherules.blogspot.com/feeds/posts/default/-/Wikipedia",
    "chriswaterguy.livejournal.com": "https://chriswaterguy.livejournal.com/data/rss?tag=wikis,wikitech,freecontent",
    "nonnotablenatterings.blogspot.com": "https://nonnotablenatterings.blogspot.com/feeds/posts/default/-/Wikimedia%20Foundation",
    "laxstrom.name": "https://laxstrom.name/blag/category/mediawiki/feed/",
    "wikimediafoundation.org": "https://wikimediafoundation.org/feed/",
    "techblog.wikimedia.org": "https://techblog.wikimedia.org/feed/",
    "ournewmind.wordpress.com": "https://ournewmind.wordpress.com/tag/wiki/feed/atom/",
    "durova.blogspot.com": "https://durova.blogspot.com/feeds/posts/default",
    "wikiprojectoregon.wordpress.com": "https://wikiprojectoregon.wordpress.com/feed/atom/",
    "anondiss.blogspot.com": "https://anondiss.blogspot.com/feeds/posts/default/-/Wikimedia%20Foundation",
    "jamesonwiki.blogspot.com": "https://jamesonwiki.blogspot.com/feeds/posts/default/-/Wikimedia",
    "jhsoby-en.blogspot.com": "https://jhsoby-en.blogspot.com/feeds/posts/default/-/Wikimedia",
    "politicalbiasonwikipedia.blogspot.com": "https://politicalbiasonwikipedia.blogspot.com/feeds/posts/default",
    "extensiontesting.blogspot.com": "https://extensiontesting.blogspot.com/feeds/posts/default",
    "tstarling.com": "https://tstarling.com/blog/category/wikimedia/feed/",
    "cometstyles.blogspot.com": "https://cometstyles.blogspot.com/feeds/posts/default/-/wikipedia",
    "wingphilopp.blogspot.com": "https://wingphilopp.blogspot.com/feeds/posts/default?alt=rss",
    "feeds.feedburner.com": "https://feeds.feedburner.com/RyanLanesBlog_mediawiki",
    "wittylama.com": "https://wittylama.com/category/wikimedia/feed/",
    "www.greenman.co.za": "http://www.greenman.co.za/blog/?tag=wikimedia&feed=rss2",
    "zikoblog.wordpress.com": "https://zikoblog.wordpress.com/category/wiki/feed/atom/",
    "ad.huikeshoven.org": "http://ad.huikeshoven.org/feeds/posts/default/-/wiki",
    "blog.wikiwix.com": "https://blog.wikiwix.com/en/feed/",
    "blogs.harvard.edu": "https://blogs.harvard.edu/sj/category/wikipedia/feed/",
    "www.phoebeayers.info": "http://www.phoebeayers.info/phlog/?cat=10&feed=rss2",
    "blog.pediapress.com": "http://blog.pediapress.com/feeds/posts/default/-/wiki",
    "blog.bawolff.net": "https://blog.bawolff.net/feeds/posts/default/-/wiki",
    "blog.wikimedia.org.uk": "https://blog.wikimedia.org.uk/feed/",
    "thomas-dalton.com": "https://thomas-dalton.com/blog/tag/wikimedia/feed/",
    "www.generalist.org.uk": "https://www.generalist.org.uk/blog/tags/wikipedia/feed/",
    "nihiltres.blogspot.com": "https://nihiltres.blogspot.com/feeds/posts/default",
    "stu.blog": "https://stu.blog/category/wiki/feed/",
    "thedjwrites.blogspot.com": "https://thedjwrites.blogspot.com/feeds/posts/default/-/wikipedia?alt=rss",
    "www.entropywins.wtf": "https://www.entropywins.wtf/blog/tag/planet-wikimedia/feed/atom/",
    "aharoni.wordpress.com": "https://aharoni.wordpress.com/category/wikipedia/feed/atom/",
    "suegardner.org": "https://suegardner.org/feed/atom/",
    "feeds.feedburner.com": "https://feeds.feedburner.com/paolognuband",
    "www.semantic-mediawiki.org": "https://www.semantic-mediawiki.org/wiki/Special:Ask/format%3Drss/sort%3DNews-20date/order%3Ddesc/searchlabel%3DRSS/type%3Datom/title%3DSemantic-20MediaWiki-20%E2%80%93-20news/description%3DLat-5Fest-20news-20from-20semantic-2Dmediawiki.org/page%3Dfull/offset%3D0/limit%3D50/-5B-5BNews-20date::%2B-5D-5D-20-5B-5BLanguage-20code::en-5D-5D/mainlabel%3D/prettyprint%3Dtrue/unescape%3Dtrue",
    "shijualex.in": "https://shijualex.in/category/wikimedia/feed/",
    "blog.openmeetings.org": "https://blog.openmeetings.org/category/planet-wikimedia/feed/atom/",
    "wizardist.wordpress.com": "https://wizardist.wordpress.com/tag/wikipedia/feed/atom/",
    "thottingal.in": "https://thottingal.in/blog/index.xml",
    "glamwiki.wordpress.com": "https://glamwiki.wordpress.com/feed/atom/",
    "hexmode.com": "https://hexmode.com/category/wmf/feed/atom/",
    "rockdrum.wordpress.com": "https://rockdrum.wordpress.com/feed/atom/",
    "endami.blogspot.com": "https://endami.blogspot.com/feeds/posts/default/-/Wikimedia",
    "www.harihareswara.net": "https://www.harihareswara.net/rss/wikimedia/",
    "magnusmanske.de": "http://magnusmanske.de/wordpress/?feed=rss2",
    "faenwp.blogspot.com": "https://faenwp.blogspot.com/feeds/posts/default/-/Wikimedia",
    "feeds.feedburner.com": "https://feeds.feedburner.com/EinsteinUniversity",
    "www.wikilovesmonuments.org": "https://www.wikilovesmonuments.org/feed/",
    "blog.robinpepermans.be": "http://blog.robinpepermans.be/feeds/posts/default/-/PlanetWM",
    "whatisgoingonineurope.blogspot.com": "https://whatisgoingonineurope.blogspot.com/feeds/posts/default",
    "internationalwikitrekk.blogspot.com": "https://internationalwikitrekk.blogspot.com/feeds/posts/default",
    "blog.wikimediadc.org": "https://blog.wikimediadc.org/feed/",
    "pigsonthewing.org.uk": "https://pigsonthewing.org.uk/category/wikipedia-2/feed/atom/",
    "wikistrategies.net": "https://wikistrategies.net/category/wiki/feed/atom/",
    "www.harryburt.co.uk": "https://www.harryburt.co.uk/blog/category/interests/mediawiki-and-wikimedia/feed/atom/",
    "apergos.wordpress.com": "https://apergos.wordpress.com/category/wikimedia/feed/",
    "greensmw.wordpress.com": "https://greensmw.wordpress.com/feed/",
    "bitterscotch.wordpress.com": "https://bitterscotch.wordpress.com/tag/wikimedia/feed/",
    "logic10.tumblr.com": "https://logic10.tumblr.com/tagged/planet/rss",
    "pauginer.com": "https://pauginer.com/tagged/wikimedia/rss",
    "wikisorcery.wordpress.com": "https://wikisorcery.wordpress.com/feed/",
    "blog.wikimedia.de": "https://blog.wikimedia.de/tag/Wikidata+English/feed/",
    "blogs.gnome.org": "https://blogs.gnome.org/aklapper/category/computer/wikimedia/feed/",
    "wikimedia.fi": "https://wikimedia.fi/category/in-english/feed/",
    "okinokynko.blogspot.com": "https://okinokynko.blogspot.com/feeds/posts/default/-/en-wiki",
    "valmj.wordpress.com": "https://valmj.wordpress.com/category/technology/foss/feed/",
    "lu.is": "https://lu.is/wikimedia/feed/",
    "nethahussain.com": "https://nethahussain.com/category/wikipedia/feed/",
    "pblog.ebaker.me.uk": "https://pblog.ebaker.me.uk/feeds/posts/default/-/wikipedia",
    "addshore.com": "https://addshore.com/feed/atom/?tag=mediawiki%2Cwikimedia%2Cwikibase%2Cwikidata%2Cwikipedia%2Cwikidatacon",
    "moriel.smarterthanthat.com": "http://moriel.smarterthanthat.com/tag/mediawiki/feed/",
    "bleededge.blogspot.com": "https://bleededge.blogspot.com/feeds/posts/default",
    "alexstinson.wordpress.com": "https://alexstinson.wordpress.com/feed/",
    "kothariharsh.wordpress.com": "https://kothariharsh.wordpress.com/tag/wikimedia/feed/",
    "wikistaycation.wordpress.com": "https://wikistaycation.wordpress.com/feed/",
    "mariapacana.tumblr.com": "https://mariapacana.tumblr.com/tagged/parsoid/rss",
    "www.wikiphotographer.net": "https://www.wikiphotographer.net/category/wikimedia-commons/feed/",
    "designatwikipedia.tumblr.com": "https://designatwikipedia.tumblr.com/rss",
    "wikinewsreporter.wordpress.com": "https://wikinewsreporter.wordpress.com/feed/",
    "meta.wikimedia.org": "https://meta.wikimedia.org/w/api.php?action=featuredfeed&feed=technews&feedformat=atom",
    "gondwanaland.com": "https://gondwanaland.com/mlog/category/wikipedia/feed/",
    "terrychay.com": "http://terrychay.com/category/work/wikimedia/feed",
    "timotijhof.net": "https://timotijhof.net/feed.xml",
    "wllm.com": "https://wllm.com/tag/wikipedia/feed/",
    "wikiedu.org": "https://wikiedu.org/feed/",
    "geniice.wordpress.com": "https://geniice.wordpress.com/feed/",
    "pigsonthewing.org.uk": "https://pigsonthewing.org.uk/feed/",
    "bluerasberry.com": "http://bluerasberry.com/feed/",
    "www.weeklyosm.eu": "https://www.weeklyosm.eu/feed",
    "jonatanglad.wordpress.com": "https://jonatanglad.wordpress.com/category/wiki/feed/",
    "cxupdate.wordpress.com": "https://cxupdate.wordpress.com/feed/",
    "blog.legoktm.com": "https://blog.legoktm.com/feeds/mediawiki.atom.xml",
    "thewikipedian.net": "https://thewikipedian.net/feed/",
    "www.generalist.org.uk": "https://www.generalist.org.uk/blog/tags/wikipedia/feed/",
    "blog.kevinpayravi.com": "https://blog.kevinpayravi.com/tag/wikimedia/feed/",
    "opensourceexile.blogspot.com": "https://opensourceexile.blogspot.com/feeds/posts/default/-/wikipedia/",
    "medbachounda.blogspot.be": "https://medbachounda.blogspot.be/feeds/posts/default/-/Wiki-en/",
    "www.dereckson.be": "https://www.dereckson.be/blog/category/wikimedia/feed/",
    "www.residentmar.io": "https://www.residentmar.io/feed",
    "blog.hatnote.com": "https://blog.hatnote.com/rss",
    "muscicapa.blogspot.com": "https://muscicapa.blogspot.com/feeds/posts/default/-/wikimedia?alt=rss",
    "wikipediaweekly.org": "http://wikipediaweekly.org/feed/podcast",
    "wirforgenderequity.wordpress.com": "https://wirforgenderequity.wordpress.com/feed/",
    "allthingslinguistic.com": "https://allthingslinguistic.com/tagged/wikipedia/rss",
    "gapfindingproject.wordpress.com": "https://gapfindingproject.wordpress.com/feed/",
    "phabricator.wikimedia.org": "https://phabricator.wikimedia.org/phame/blog/feed/1/",
    "lornamcampbell.org": "https://lornamcampbell.org/tag/wikimedia/feed/",
    "samwilson.id.au": "https://samwilson.id.au/tag/Wikimedia/feed/",
    "blog.ash.bzh": "https://blog.ash.bzh/en/feed/",
    "phabricator.wikimedia.org": "https://phabricator.wikimedia.org/phame/blog/feed/5/",
    "goinggnu.wordpress.com": "https://goinggnu.wordpress.com/category/wikipedia/feed/",
    "blog.bluespice.com": "https://blog.bluespice.com/tag/mediawiki/feed/",
    "tttwrites.wordpress.com": "https://tttwrites.wordpress.com/category/wikimedia/feed/",
    "phabricator.wikimedia.org": "https://phabricator.wikimedia.org/phame/blog/feed/7/",
    "phabricator.wikimedia.org": "https://phabricator.wikimedia.org/phame/blog/feed/8/",
    "medium.com": "https://medium.com/feed/wiki-playtime",
    "goinggnu.wordpress.com": "https://goinggnu.wordpress.com/category/wikipedia/feed/",
    "clkoerner.com": "https://clkoerner.com/feed/?cat=197%2C205",
    "cookiesandcodeblog.wordpress.com": "https://cookiesandcodeblog.wordpress.com/feed/",
    "phabricator.wikimedia.org": "https://phabricator.wikimedia.org/phame/blog/feed/9/",
    "anna.flourishing.stream": "https://anna.flourishing.stream/index.xml",
    "blog.maudite.cc": "http://blog.maudite.cc/comments/feed",
    "outreachy-17.blogspot.com": "https://outreachy-17.blogspot.com/feeds/posts/default?alt=rss",
    "vinithavs.wordpress.com": "https://vinithavs.wordpress.com/feed/",
    "medium.com": "https://medium.com/feed/@nehajha",
    "medium.com": "https://medium.com/feed/@meghasharma4910",
    "phabricator.wikimedia.org": "https://phabricator.wikimedia.org/phame/blog/feed/13/",
    "wandacode.com": "https://wandacode.com/category/outreachy-internship/feed/",
    "professional.wiki": "https://professional.wiki/blog/feed",
    "wikimedia.brussels": "https://wikimedia.brussels/feed/",
    "blog.atagar.com": "https://blog.atagar.com/feed/",
    "commonists.wordpress.com": "https://commonists.wordpress.com/feed/",
    "tylercipriani.com": "https://tylercipriani.com/blog/index.rss",
    "words.theresnotime.co.uk": "https://words.theresnotime.co.uk/category/wikimedia/feed/",
    "taavi.wtf": "https://taavi.wtf/tags/wikimedia/index.xml",
    "diff.wikimedia.org": "https://diff.wikimedia.org/feed/",
    "feeds.libsyn.com": "https://feeds.libsyn.com/115190/rss",
    "hexmode.com": "https://hexmode.com/category/mediawiki/feed/",
    "www.pro.wiki": "https://www.pro.wiki/blog/feed",
    "design.wikimedia.org": "https://design.wikimedia.org/blog/feed.xml",
    "www.kostaharlan.net": "https://www.kostaharlan.net/tags/wikimedia/index.xml",
}

PLANET_TEMPLATE = 'planet.html.tmpl'
PLANET_PAGE = '../docs/index.html'

PLANET_MAX_ARTICLES = 50
PLANET_MAX_ARTICLES_PER_FEED = 5

# set up logging
import logging; logging.basicConfig(level=logging.DEBUG)

for name, url in PLANET_FEEDS.items():
	print('1. [{}]({})'.format(name, url))

