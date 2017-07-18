from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from social.apps.django_app.default.models import UserSocialAuth

from drchrono.birthday_wisher import modules


# Create your views here.


@login_required()
def birthday_wisher(request):
    # Get the token needed to receive data from the api
    social = UserSocialAuth.objects.get()

    # Get all patients whos birthday it is
    patients = modules.get_birthday_patients(social)
    messages = [modules.make_birthday_message(patient, request.user) for patient in patients]
    # Send all patients selected an email wishing them a happy birthday
    return render_to_response('patients.html', {'messages': messages})

