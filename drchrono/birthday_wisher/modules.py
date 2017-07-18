from datetime import datetime

from django.conf import settings
from django.utils.safestring import mark_safe

from drchrono.api import get_all_patients


# Since we cannot filter partial dates, we get all patients and then select
# those that have their birthday today.
def get_birthday_patients(social):
    all_patients = get_all_patients(social)

    # Select the patients if their date of birth is entered and today

    if settings.DEBUG:
        # Use 09 02 as default for testing
        birthday_patients = [patient for patient in all_patients if patient['date_of_birth'] and
                             [2, 11] == map(int, patient['date_of_birth'].split('-'))[1:3]]

    else:
        birthday_patients = [patient for patient in all_patients if patient['date_of_birth'] and
                             [datetime.today().month, datetime.today().day] ==
                             map(int, patient['date_of_birth'].split('-'))[1:3]]

    return birthday_patients


# This function creates the body of the happy birthday email based on the patient information available
def make_email_message(patient, doctor):
    message = ''
    if patient['first_name']:
        message = 'Dear ' + patient['first_name'] + ' ' + patient['last_name'] + ',%0D%0A %0D%0A'
    elif patient['last_name']:
        if patient['gender']:
            if patient['gender'] == 'Male':
                message = 'Dear Mr. ' + patient['last_name'] + '%0D%0A %0D%0A'
            elif patient['gender'] == 'Female':
                message = 'Dear Ms. ' + patient['last_name'] + '%0D%0A %0D%0A'
            else:
                message = 'Dear Mr. or Ms. ' + patient['last_name'] + '%0D%0A %0D%0A'
        else:
            message = 'Dear Mr. or Ms. ' + patient['last_name'] + '%0D%0A %0D%0A'

    # If no first or last name is available, the first line is skipped

    message += 'Happy birthday from your doctor! %0D%0A %0D%0A Best regards, %0D%0A '

    if doctor.get_full_name():
        message += 'Doctor ' + doctor.get_full_name()
    else:
        message += 'Your doctor'

    return message


def make_birthday_message(patient, doctor):
    # For correct ways of referring to patient, reads easier than using patient['first_name']
    himher = 'them'
    hisher = 'their'
    if patient['gender'] == 'Male':
        himher = 'him'
        hisher = 'his'
    elif patient['gender'] == 'Female':
        himher = 'her'
        hisher = 'her'

    message = ''

    # Add the photo of the patient if there is one
    if patient['patient_photo']:
        message += '<img src = \"' + patient['patient_photo'] + \
                   '\" alt = \"Patient Photo\" align = \"right\" width = \"100px\">'

    # Notify doctor of birthday
    message += '<div class="hero-unit"> <p>' + patient['first_name'] + ' ' + patient['last_name'] + \
        ' has ' + hisher + ' birthday today!'

    # Add contact information if it is available
    if patient['email']:
        message += '<p> Contact ' + himher + ' by email at: ' + \
              '<a href=\"mailto:' + patient['email'] + \
              ' ?subject=Happy%20Birthday!' + \
              '&amp;body=' + make_email_message(patient, doctor) + '\"> ' + \
              patient['email'] + '</a>'

    if patient['cell_phone']:
        message += '<p> Give ' + himher + ' a call at: <a href="tel:' + \
                    patient['cell_phone'] + '">' + patient['cell_phone'] + '</a>'

    elif patient['home_phone']:
        message += '<p> Give ' + himher + ' a call at: <a href="tel:' + \
                   patient['home_phone'] + '">' + patient['home_phone'] + '</a>'

    # Or a message if it is not
    if not (patient['email'] or patient['cell_phone'] or patient['home_phone']):
        message += '<p> Unfortunately, there is no contact information available for ' + himher

    # uncomment the line below to show all of the patients information
    # message += '<p>' + str(patient)

    message += '</div>'
    return mark_safe(message)
