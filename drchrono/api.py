import datetime
import requests
from django.conf import settings
from django.core.serializers.json import json, DjangoJSONEncoder
from django.utils.timezone import now, make_aware, get_current_timezone


# refreshes the token if it hasn't expired
def refresh_token(func):

    def func_wrapper(*args, **kwargs):
        social = args[0]
        if make_aware(datetime.datetime.strptime(social.extra_data['expires_timestamp'][1:-6], '%Y-%m-%dT%H:%M:%S'),
                      get_current_timezone()) < now():
            response = requests.post('https://drchrono.com/o/token/', data={
                'refresh_token': social.extra_data['refresh_token'],
                'grant_type': 'refresh_token',
                'client_id': settings.SOCIAL_AUTH_DRCHRONO_KEY,
                'client_secret': settings.SOCIAL_AUTH_DRCHRONO_SECRET,
            }).json()

            social.set_extra_data({'access_token':response["access_token"], 'refresh_token' : response["refresh_token"],
                                   'expires_timestamp' : json.dumps(now() +
                                   datetime.timedelta(seconds=response['expires_in']), cls=DjangoJSONEncoder)})


        return func(*args, **kwargs)

    return func_wrapper


# returns a list of all patients.
# uses a Token object to connect to the api
@refresh_token
def get_all_patients(social):

    patients = []
    patients_url = 'https://drchrono.com/api/patients'
    headers = {
        'Authorization': 'Bearer %s' % social.extra_data['access_token']
        }

    while patients_url:
        data = requests.get(patients_url, headers=headers)

        print 'data'
        print data

        # Check for the case of no patients
        if not data:
            break

        json_data = data.json()
        patients.extend(json_data['results'])
        patients_url = json_data['next']  # A JSON null on the last page

    return patients

