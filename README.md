# drchrono Hackathon

### Requirements
- [pip](https://pip.pypa.io/en/stable/)
- [python virtual env](https://packaging.python.org/installing/#creating-and-using-virtual-environments)

### Setup
``` bash
$ pip install -r requirements.txt
$ python manage.py runserver
```

`social_auth_drchrono/` contains a custom provider for [Python Social Auth](http://psa.matiasaguirre.net/) that handles OAUTH for drchrono. To configure it, set these fields in your `drchrono/settings.py` file:

```
SOCIAL_AUTH_DRCHRONO_KEY
SOCIAL_AUTH_DRCHRONO_SECRET
SOCIAL_AUTH_DRCHRONO_SCOPE
LOGIN_REDIRECT_URL
```

# Design

### Birthday notifications
This application does not automatically wish patients a happy birthday but rather notifies the doctor of any
birthdays and provides the contact information of patients. The doctor already logs in to drchrono to use the
app and making them also log into their email to send automatic messages would not be right considering drchono
already has a service to message patients. 

### Pipeline
load_expires_timestamp was added to the default pipeline in order to save the expiration time of tokens.
 This will come in handy when refreshing tokens. 

### API
api.py contains all functions getting information from the api, in the future, the refresh_token 
function should be moved to the backends file. Information is retrieved from the patients endpoint
instead of the patients:summary endpoint because finding whether it is a patients birthday and 
after that getting their contact information would cause more effort from the user than they would
be hoping to invest.

### Modules
modules.py contains the functions that create the content for the views to keep those readable. They 
offer a phone link to the patient on their cellphone if it is available with a home phone number as a
second option. An email address is also provided with a mailto link for doctors who like to have a standard
message ready to go. Improvements here could be made by automatically opening the drchrono message service
and signing using the doctor's name when the api will allow it. Another extension could be made by allowing
doctors to create their own happy birthday message for a good balance between time efficiency and personability.

### Front-end
Bootstrap creates a simplistic style that would allow this tool to smoothly be absorbed by bigger projects.
