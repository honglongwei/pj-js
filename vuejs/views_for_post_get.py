from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import CMDB_SALT
from django.core import serializers

def cmdb_add(request):
    if request.method == 'POST':
        wip = request.POST['wip']
        nip = request.POST['nip']
        tt = CMDB_SALT.objects.create(Wip=wip, Nip=nip)
        tt.save()
        tdata = CMDB_SALT.objects.all()
        #return render_to_response('cmdb/cmdb_add.html')
        json_data = serializers.serialize("json", tdata)
        return HttpResponse(json_data,content_type="application/json")
    return render_to_response('cmdb/cmdb_add.html')



def cmdb_edit(request):
    return render_to_response('cmdb/cmdb_list.html')



def cmdb_list(request):
    tdata = CMDB_SALT.objects.all()
    json_data = serializers.serialize("json", tdata)
    return HttpResponse(json_data,content_type="application/json")
    #return json_data


def cmdb_search(request):
    if request.method == 'POST':
        gip = request.POST['ip']
        tdata = CMDB_SALT.objects.filter(Wip__icontains=gip).all()
        #return render_to_response('cmdb/cmdb_add.html')
        json_data = serializers.serialize("json", tdata)
        return HttpResponse(json_data,content_type="application/json")
    return HttpResponse('null')


def cmdb_delete(request):
    if request.method == 'POST':
        gid = request.POST['id']
        tt = CMDB_SALT.objects.filter(id=gid).delete()
        tdata = CMDB_SALT.objects.all()
        json_data = serializers.serialize("json", tdata)
        return HttpResponse(json_data,content_type="application/json")
    return HttpResponse('null')


def cmdb_delall(request):
    CMDB_SALT.objects.all().delete()
    tdata = CMDB_SALT.objects.all()
    json_data = serializers.serialize("json", tdata)
    return HttpResponse(json_data,content_type="application/json")
