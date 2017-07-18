from django.conf.urls import include, url
from django.views.generic import TemplateView

urlpatterns = [
    # Put index in views for consistency
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),

    url(r'', include('social.apps.django_app.urls', namespace='social')),

    # All urls in the practice subdirectory
    # url(r'^practice/', include('drchrono.practice.urls')),

    # All urls in the birthday_wisher subdirectory
    url(r'^birthday_wisher/', include('drchrono.birthday_wisher.urls'), name='birthday_wisher'),
]
