from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.list_detail import object_list, object_detail
from codereviewr.code.models import Code

def code_detail(request, code_id):
    """
    Displays a single piece of code.
    """
    try:
        code = Code.objects.get(pk=code_id)
    except Code.DoesNotExist:
        raise Http404, "Sorry, the code you requested was not found."
    
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
        template_object_name='code',
        paginate_by=50
    )
    