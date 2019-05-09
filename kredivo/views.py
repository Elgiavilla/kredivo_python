import json
import urllib.parse
from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class ViewWrapper(View):
    view_creator_func = None
    upload_picture_name = None

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ViewWrapper, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        kwargs.update(request.GET.dict())

        body, status = self.view_creator_func(request, **kwargs).get(**kwargs)
        return HttpResponse(json.dumps(body), status=status, content_type='application/json')
    
    def post(self, request, *args, **kwargs):
        kwargs.update(request.POST.dict())

        if self.upload_picture_name is not None:
            picture = request.FILES[self.upload_picture_name]
            body, status = self.view_creator_func(request, **kwargs).post(picture, **kwargs)
        else:
            body, status = self.view_creator_func(request, **kwargs).post(**kwargs)
        return HttpResponse(json.dumps(body), status=status, content_type='application/json')
    
    def put(self, request, *args, **kwargs):
        data = dict(urllib.parse.parse_qsl(request.body.decode("utf-8"), keep_blank_values=True))
        kwargs.update(data)


        body, status = self.view_creator_func(request, **kwargs).put(**kwargs)
        return HttpResponse(json.dumps(body), status=status, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        kwargs.update(request.GET.dict())

        body, status = self.view_creator_func(request, **kwargs).delete(**kwargs)
        return HttpResponse(json.dumps(body), status=status, content_type='application/json')