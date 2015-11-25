from django.template.loader import get_template
from django.shortcuts import redirect, render_to_response, render
from django.template import Context, RequestContext
from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hello world")

def about(request):
    return render_to_response('about.html', locals(), RequestContext(request))

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)
