from django.contrib import admin
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from news.models import Uploads
from qalampir.settings import UPLOADS_ROOT, join_path, path_exists, basename


def home(request):
    return redirect('/news')


def file_download(request, code: str):
    file = Uploads.objects.filter(code=code).first()
    if file:
        file_path = join_path(UPLOADS_ROOT, file.new_name)
        if path_exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type=file.content_type)
                response['Content-Disposition'] = 'inline; filename=' + basename(file_path)
                return response
        raise Http404
    raise Http404


urlpatterns = [
    path('', home, name='main'),
    path('download/<code>', file_download, name='download'),
    path("news/", include('news.urls')),
    path("accounts/", include('accout.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
