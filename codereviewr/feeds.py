from django.contrib.syndication.feeds import Feed, FeedDoesNotExist
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.contrib.comments.feeds import LatestCommentsFeed
from codereviewr.code.models import Code
from codereviewr.settings import SITE_ID

class UserFeed(Feed):
	"""Feed for activity of a certain user"""
	def get_object(self, bits):
		# bits = /slug/bit[0]  where slug = "user" and bit[0] = username
		if len(bits) != 1: # make sure there is only 1 bit after slug eg /user/admin/ NOT /user/admin/foo
			raise ObjectDoesNotExist
		return User.objects.get(username=bits[0])
	
	def title(self,obj):
		if not hasattr(self,'_site'):
			self._site = Site.objects.get(pk=SITE_ID)
		return "%s: Latest submissions from %s" % (self._site.name,obj.username)
	
	def link(self,obj):
		if not hasattr(self,'_site'):
			self._site = Site.objects.get(pk=SITE_ID)
		if not obj:
			raise FeedDoesNotExist
		return "http://%s/" % self._site.domain
	
	def description(self,obj):
		return "%s: Latest activity from %s" % (self._site.name,obj.username)
	
	def items(self,obj):
		return Code.objects.filter(author=obj.id, is_public=True).order_by('updated')[:5]

class CodeFeed(Feed):
	"""Feed for latest activity on a particular piece of code"""
class LatestFeed(Feed):
	"""Feed for latest site activity"""
class LanguageFeed(Feed):
	"""Feed for the latest submissions of a particular language"""