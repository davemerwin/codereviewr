from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.list_detail import object_list, object_detail
from codereviewr.code.models import Code
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_for_filename

def code_detail(request, code_id):
    """
    Displays a single piece of code.
    """
    try:
        code = Code.objects.get(pk=code_id)
    except Code.DoesNotExist:
        raise Http404, "Sorry, the code you requested was not found."

    # Pygmentize code
    lexer = get_lexer_for_filename('test.py', stripall=True)
    formatter = HtmlFormatter(linenos=True, cssclass="source")
    
    code.highlight = highlight(code.code, lexer, formatter)
    
    return render_to_response(
        'code/detail.html',
        {'code': code},
        context_instance=RequestContext(request)
    )

def code_list(request):
    """
    Lists all code flagged as is_public.
    """
    codes = Code.objects.filter(is_public=True)
    
    return object_list(
        request,
        queryset=codes,
        template_name='code/list.html',
        template_object_name='code',
        paginate_by=50,
    )

def index(request):
    s = []
    if request.openid:
        s.append('<p>You are signed in as <strong>%s</strong>' % escape(
            str(request.openid)
        ))
        
        if request.openid.is_iname:
            s.append(' (an i-name)')
        s.append('</p>')
        
        if request.openid.sreg:
            s.append('<p>sreg data: %s</p>' % escape(str(request.openid.sreg)))
        
        if len(request.openids) > 1:
            s.append('<p>Also signed in as %s</p>' % ', '.join([
                escape(str(o)) for o in request.openids[:-1]
            ]))

    s.append('<a href="/openid/">Sign in with OpenID</a>')
    s.append(' | <a href="/openid/with-sreg/">')
    s.append('Sign in with OpenID using simple registration</a>')
    s.append(' | <a href="/openid/?next=/next-works/">')
    s.append('Sign in with OpenID, testing ?next= param</a>')
    
    if request.openid:
        s.append(' | <a href="/openid/signout/">Sign out</a>')
    
    s.append('</p>')
    return HttpResponse('\n'.join(s))

def next_works(request):
    return HttpResponse('?next= bit works. <a href="/">Home</a>')
