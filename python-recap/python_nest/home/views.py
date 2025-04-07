from django.shortcuts import render, redirect

# Create your views here.
def homePage(request):
    if request.method == 'POST':
        data = request.POST
        # context = {"all data": data}
        return redirect('view/')
        
    return render(request, 'index.html')

# def viewPage(request):
    
#     savers_name = 'name'
#     savers_occupation = 'occupation'
#     savers_amount = 'amount'
#     savers_date = 'date'
#     savers_transaction_id = 'transaction id'

#     all_data = [
#         savers_name,
#         savers_occupation,
#         savers_amount,
#         savers_date,
#         savers_transaction_id,
#                 ]
    
#     context = {
#         "saver_data": all_data
#     }
    
   
#     return render(request, 'view.html', context)
formdata = {}
def viewPage(request):
    if request.method == 'POST':
        all_data = {
            "name": request.POST.get('name'),
            "occupation": request.POST.get('occupation'),
            "amount": request.POST.get('occupation'),
            "date": request.POST.get('date'),
            "transaction": request.POST.get('transaction id')
        }
        global formdata
        formdata = all_data
        context = {
            'all_data': all_data
        }
        # return redirect('viewdata')
    return render(request, 'view.html', context)

# def viewdata(request):
#     global formdata
#     all_data = formdata
#     context = {
#         "all_data": all_data
#     }

#     return render(request, 'view.html', context)