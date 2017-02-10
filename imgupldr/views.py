from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from .forms import ImageUploadForm

from .models import ImageSet


def upload_pic(request):
    template = loader.get_template('imgupldr/index.html')
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            m = Image.objects.get(pk=course_id)
            m.model_pic = form.cleaned_data['image']
            m.save()
            return HttpResponse('image upload success')
    return HttpResponseForbidden('allowed only via POST')

# Create your views here.
