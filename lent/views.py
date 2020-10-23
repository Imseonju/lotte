from django.shortcuts import render, get_object_or_404
from .models import lent
from user.models import CustomUser
# Create your views here.
def detail(request):
    return render(request, 'lent/detail.html')

def create(request):
    if request.method == 'POST' and request.session.get('user', False):
        machine = request.POST['machine']
        category = request.POST['category']
        provider = get_object_or_404(CustomUser, username = request.session['user'])

        lental = lent(
            machine = machine,
            category = category,
            provider = provider,
        )
        lental.save()

        return redirect('detail')
    else:
        return render(request, 'user/home.html')