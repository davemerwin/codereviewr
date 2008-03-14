from django.contrib.syndication.feeds import Feed, FeedDoesNotExist
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.contrib.comments.feeds import LatestCommentsFeed
from codereviewr.code.models import Code, Language
from codereviewr.settings import SITE_ID

class LatestFeed(Feed):
	"""
	Class: GenericFeed
	Author: Nate Anderson
	Slug: /feeds/latest
	Description: 
		Will generate feeds for the latest public code submissions. It will also be used
		by all other feed classes for link and title
	"""
	_site = Site.objects.get(pk=SITE_ID)
	content_type = Code
	title_template = 'feeds/feed_title.html'
	description_template = 'feeds/feed_description.html'
	def link(self):
		return "http://%s/" % self._site.domain
	
	def title(self):
		return "%s" % (self._site.name)
	
	def description(self):
		return "Latest code submissions.  Check out the code and make a suggested improvement."
	
	def get_query_set(self):
		return self.content_type.objects.filter(is_public=True).order_by('updated')[:40]
	
	def items(self):
		return self.get_query_set()

class UserFeed(LatestFeed):
	"""
	Class: UserFeed
	Author: Nate Anderson
	Slug: /feeds/user/uname
	Description: 
		This class will generate an RSS2.0 feed for the latest public activity of a the user given by uname in the slug.
	"""
	def get_object(self, bits):
		# bits = /slug/bit[0]  where slug = "user" and bit[0] = username
		if len(bits) != 1: # make sure there is only 1 bit after slug eg /user/admin/ NOT /user/admin/foo
			raise ObjectDoesNotExist
		return User.objects.get(username=bits[0])
	
	def description(self,obj):
		return "Latest activity on %s from user %s" % (LatestFeed._site.name,obj.username)
	
	def items(self,obj):
		return Code.objects.filter(author=obj.id, is_public=True).order_by('updated')[:40]

class CodeFeed(LatestFeed):
	"""
	Class: CodeFeed
	Author: Nate Anderson
	Slug: /feeds/code/id
	Description: 
		Will generate feeds for activity of the code snippet given as id.
	"""
class LanguageFeed(LatestFeed):
	"""
	Class: LanguageFeed
	Author: Nate Anderson
	Slug: /feeds/language/name
	Description: 
		Will generate feeds for the code snippets that are from the language .
	"""
	
	def get_object(self,bits):
		if len(bits) != 1:
			raise ObjectDoesNotExist
		return Language.objects.get(name=bits[0].capitalize())
	
	def description(self,obj):
		if not obj:
			raise FeedDoesNotExist
		return "Latest submission of code in %s" % obj.name

	def items(self,obj):
		return Code.objects.filter(language=obj.id).order_by('updated')[:40]