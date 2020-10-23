from django.shortcuts import render
from .models import lent
from user.models import CustomUser
# Create your views here.
def detail(request):
    return render(request, 'lent/detail.html')