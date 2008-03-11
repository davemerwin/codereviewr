from django.contrib.syndication.feeds import Feed, FeedDoesNotExist
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.contrib.comments.feeds import LatestCommentsFeed
from codereviewr.code.models import Code

class UserFeed(Feed):
	def get_object(self, bits):
		if len(bits) != 1:
			raise ObjectDoesNotExist
		username = User.objects.get(username = bits[0])
		return Code.objects.get(author=username.id)
	
	def link(self,obj):
		if not obj:
			raise FeedDoesNotExist
		return "http://localhost/"
		
	def title(self, obj):
		return "codereviewr.com: Latest submissions from %s" % obj.author
	
	def description(self, obj):
		return "codereviewr.com: Latest activity from %s" % obj.author
	def item_link(self,obj):
		return "/somelink/"
	def items(self,obj):
		return Code.objects.filter(pk=obj.id).order_by('updated')[:5]

class LatestComments(LatestCommentsFeed):
	
	def item_link(self):
		return "/somelink/"