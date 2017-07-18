from django.shortcuts import render_to_response, redirect, RequestContext


# Create your views here.


def auth_view(request):
    # response = api.get_token(request)
    # print request.COOKIES.get('csrftoken')
    # response.raise_for_status()
    # data = response.json()
    #
    # token = Token.objects.create(
    #     access_token=data['access_token'],
    #     refresh_token=data['refresh_token'],
    #     expires_timestamp=datetime.datetime.now() + datetime.timedelta(seconds=data['expires_in'])
    # )
    # token.save()
    print ''
    print ''
    print ''
    print ''
    print('requestrequestrequestrequestrequest')
    print ''
    #print('\n'.join([x if no_exception_getattr(request, x) else '' for x in dir(request)]))
    print('\n'.join(['%s: %s' % (x, no_exception_getattr(request.user, x)) if no_exception_getattr(request.user, x) else '' for x in dir(request.user)]))

    print ''
    print ''
    print 'acc'
    #print request.session['social_auth_last_login_backend']

    #print('useruseruseruseruseruser')
    #print('\n'.join([x if x else '' for x in (request.session)]))
    #print 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    #print('\n'.join([x if x else '' for x in (request.session.items)]))

    #print request.session.keys
    # print request.session.items
    # print('\n'.join([x if no_exception_getattr(request.user, x) else '' for x in dir(request.user)]))
    print ''
    print ''
    print ''
    print ''
    print('sessionsessionsessionsessionsessionsessionkeyskeyskeyskeys')
    #print request.session.keys
    # print('\n'.join([no_exception_getattr(request.session.keys, x) if no_exception_getattr(request.session.keys, x) else '' for x in dir(request.session.keys)]))

    #print('skuhgksgksk')
    #print('\n'.join(['%s: %s' % (x, no_exception_getattr(request, x)) for x in dir(request)]))


    return redirect("/")

def no_exception_getattr(user, attr):
    try:
        return getattr(user, attr)
    except Exception, e:
        return e

def doctor_login(request):
    return render_to_response('index.html', context, context_instance=RequestContext(request))
