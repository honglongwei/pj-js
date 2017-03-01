from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import Jobs
import salt.client
import json
from django.core import serializers


def jobs(request):
    return render_to_response('index.html')


def job_data(request):
    if request.method == 'POST':
        IP = request.POST['ip']
        CMD = request.POST['cmd']
        local = salt.client.LocalClient()
        tdata = local.cmd(IP, 'cmd.run', [CMD])
        t = Jobs.objects.create(IP=IP, CMD=CMD, RET=tdata)
        t.save()
        ret = json.dumps(tdata)
        return HttpResponse(ret, content_type="application/json")
    return render_to_response('history.html')

