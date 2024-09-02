from django.shortcuts import render
from django.contrib import messages

def index(request):
    messages.info(request, "Three credits remain in your account.")
    messages.success(request, "Profile details updated.")
    messages.warning(request, "Your account expires in three days.")
    messages.error(request, "Document deleted.")
    return render(request, 'base.html')

