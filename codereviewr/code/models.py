from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from datetime import datetime
from pygments import formatters, highlight, lexers

class Language(models.Model):
    """
    Lookup table for languages
    To create these in the admin, see http://pygments.org/docs/lexers/
    """
    name = models.CharField(max_length=100)
    slug = models.SlugField(prepopulate_from=('name',))
    lexer_name = models.CharField(max_length=100, help_text="The name given to Pygment's get_lexer_by_name method.")
    file_extension = models.CharField(max_length=10, blank=True, help_text="The file extensions for downloads.  No dot.")
    mime_type = models.CharField(max_length=100, help_text="The HTTP content-type to use for downloads.")
    
    class Admin:
        list_display = ('name', 'slug', 'file_extension', 'mime_type')
        ordering = ('name',)
 
    def __unicode__(self):
        return self.name

    def get_lexer(self):
        """Returns a Pygments Lexer object using lexer_name"""
        return lexers.get_lexer_by_name(self.lexer_name)

class Code(models.Model):
    """
    Core code model for code snippets
    """
    title = models.CharField(max_length=200)
    code = models.TextField()
    code_html = models.TextField(editable=False)
    author = models.ForeignKey(User)
    description = models.TextField(blank=True)
    dependencies = models.CharField(blank=True, max_length=255)
    language = models.ForeignKey(Language, db_index=True)
    version = models.CharField(blank=True, max_length=100)
    is_public = models.BooleanField(default=True)
    created = models.DateTimeField(default=datetime.now)
    updated = models.DateTimeField(blank=True, default=datetime.now)
 
    def __unicode__(self):
        return "%s by %s" % (self.title, self.author.get_full_name())

    def get_absolute_url(self):
        return ('code_detail', [str(self.id)])
    get_absolute_url = models.permalink(get_absolute_url)

    def save(self):
        # TODO: Check if we need to add updated here or if the default takes care of it
        self.code_html = highlight(
            self.code,
            self.language.get_lexer(),
            formatters.HtmlFormatter(linenos=True)
        )
        super(Code, self).save()
        
    class Meta:
        verbose_name_plural = 'code'
 
    class Admin:
        list_display = ('title','author','is_public','created')
 
