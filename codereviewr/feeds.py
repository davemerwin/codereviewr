from django.contrib.syndication.feeds import Feed, FeedDoesNotExist
from codereviewr.code.models import Code
from django.contrib.auth.models import User

class CodeFeed(Feed):
	def get_object(self, bits):
		if len(bits) != 1:
			raise ObjectDoesNotExist
		username = User.objects.get(username = bits[0])
		
		return Code.objects.get(author=username.id)
	
	def link(self,obj):
		if not obj:
			raise FeedDoesNotExist
		return "http://localhost:8000/"
		
	def title(self, obj):
		return "codereviewr.com: Latest submissions from %s" % obj.author
	
	def description(self, obj):
		return "codereviewr.com: Latest activity for %s" % obj.author
	
	def item_link(self):
		return "http://localhost:8000/code/"
	
	def items(self,obj):
		return Code.objects.filter(pk=obj.id).order_by('updated')[:5]