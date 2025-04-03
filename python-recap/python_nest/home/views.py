from django.shortcuts import render

# Create your views here.
def homePage(request):
    if request.method == 'POST':
        data = request.POST
        context = {"all data": data}
        print(context)
    return render(request, 'index.html')