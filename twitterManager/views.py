from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth

def index(request):
    user = UserSocialAuth.objects.get(user_id=request.user.id)
    pageDic = {
        'user': user
    }
    return redirect(request, 'twitterManager/index.html', pageDic)

