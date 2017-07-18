from django.conf.urls import url

urlpatterns = [
    # The one and only birthday information page
    url(r'^$', 'drchrono.birthday_wisher.views.birthday_wisher'),

]
