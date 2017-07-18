import datetime

from django.core.serializers.json import json, DjangoJSONEncoder
from django.utils.timezone import now


# The second to last step in the pipeline sets the expiration timestamp
# This and the step load_extra_data could be made into one step together,
# but since the adding of this field is slightly different from the others
# anyway, this step makes it easy to see how much the pipeline differs from the default
def load_expires_timestamp(backend, uid, **kwargs):
    social = kwargs.get('social') or \
             backend.strategy.storage.user.get_social_auth(backend.name, uid)
    if social:
        social.set_extra_data({'expires_timestamp': json.dumps(now() +
                    datetime.timedelta(seconds=social.extra_data['expires_in']), cls=DjangoJSONEncoder)})

