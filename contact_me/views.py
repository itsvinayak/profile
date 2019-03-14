from django.shortcuts import render
from .forms import msgForm

def contact_me(request):

    if request.method=='POST':
        form=msgForm(request.POST)
        if form.is_valid():
            form.save()
    form=msgForm()

    page_details={
                 "title":"contact me",
                 "form":form,
    }
    return render(request,"contact_me/contact.html",page_details)
