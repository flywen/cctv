from django.shortcuts import render, render_to_response, RequestContext

# Create your views here.
def index(request):
    if not request.POST.get('datetime'):
        print "Datetime is null!"
    else:
        datetime = request.POST.get('datetime').split(' ')
        date = ''.join(datetime[0].split('/'))
        print date
        time = ''.join(datetime[1].split(':'))+'00'
        print time
        file_url = date+'/play'+(datetime[1].split(':'))[0]+'.m3u8'
        print file_url
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))