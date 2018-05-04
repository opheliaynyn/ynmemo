from django.shortcuts import render
from django.contrib.auth.decorators import login_required

#@login_required
def index(request):
    return render(request,
                  'progress/index.html',
                  {'user': request.user})

"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth

@login_required
def index(request):
    user = UserSocialAuth.objects.get(user_id=request.user.id)
    pageDic = {
        'user': user
    }
    return render(request, 'progress/index.html', pageDic)
"""