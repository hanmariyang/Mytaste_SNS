from django.shortcuts import render

# Create your views here.
def sign_up_view(request):
    return render(request, 'account/sign_up.html')

def sign_in_view(request):
    return render(request, 'account/sign_in.html')