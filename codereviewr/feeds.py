from django.contrib.syndication.feeds import Feed
from codereviewr.code.models import Code

class LatestEntries(Feed):
	title = "Codereviewr.com Latest Code Submissions."
	link = "/code/"
	description = "The latest code submissions to codereviewr.com. Please review the code and submit a suggested optimization."
	
	def items(self):
		return Code.objects.order_by('updated')[:5]