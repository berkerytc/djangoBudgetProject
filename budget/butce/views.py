from django.shortcuts import render, redirect
from django.db.models import Sum
from . models import Category, Transaction

def transaction_list(request):
    transactions = Transaction.objects.all()
    categories = Category.objects.all()
    total_balance = Transaction.objects.aggregate(balance=Sum('amount'))
    context = {
        'transactions' : transactions,
        'categories' : categories,
        'balance': total_balance['balance']
    }
    return render(request,'transactions.html',context)


def add_transaction(request):
    categories = Category.objects.all()
    context = {
        'categories' : categories,
        'values' : request.POST
    }
    if request.method == 'GET':
        return render(request, 'transactions/add_transaction.html',context)

    if request.method == 'POST':
        name = request.POST['name']
        amount = request.POST['amount']
        date = request.POST['transaction_date']
        category = request.POST['category']
    Transaction.objects.create(name=name,category=category,amount=amount,date=date)
    return redirect('transactions') 


def edit_transaction(request, id):
    transaction = Transaction.objects.get(pk=id)
    categories = Category.objects.all()
    context = {
        'transaction': transaction,
        'values' : transaction,
        'categories' : categories 
    }
    if request.method == 'GET':
        return render(request, 'transactions/edit_transaction.html',context)
    if request.method == 'POST':
        name = request.POST['name']
        amount = request.POST['amount']
        date = request.POST['transaction_date']
        category = request.POST['category']

    transaction.name = name
    transaction.amount = amount
    transaction.date = date
    transaction.category = category

    transaction.save()
    return redirect('transactions')

def delete_transaction(request, id):
    transaction = Transaction.objects.get(pk=id)
    transaction.delete()
    return redirect('transactions')


def filter_page(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        category = request.POST['category']
        ftransactions = Transaction.objects.all()

        if request.POST['date1']!='' and request.POST['date2']!='':
            ftransactions = ftransactions.filter(date__range=[ request.POST['date1'] , request.POST['date2'] ])
        if category != '':
            ftransactions = ftransactions.filter(category=category)
        

        context = {'categories' : categories,'ftransactions' : ftransactions}
        return render(request,'transactions/filter_page.html',context)

    context = {'categories' : categories}
    return render(request,'transactions/filter_page.html',context)



    