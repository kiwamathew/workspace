from django.shortcuts import render

# Create your views here.
def homePage(request):
    if request.method == 'POST':
        data = request.POST
        context = {"all data": data}
        
    return render(request, 'index.html')

def viewPage(request):
    
    savers_name = 'name'
    savers_occupation = 'occupation'
    savers_amount = 'amount'
    savers_date = 'date'
    savers_transaction_id = 'transaction id'

    all_data = [
        savers_name,
        savers_occupation,
        savers_amount,
        savers_date,
        savers_transaction_id,
                ]
    
    context = {
        "saver_data": all_data
    }
    
   
    return render(request, 'view.html', context)