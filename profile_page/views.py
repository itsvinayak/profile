from django.shortcuts import render

def index(request):
    page_details={
              "title":"hii, this is vinayak",
    }
    return render(request,'profile_page/index.html')
