from django.shortcuts import render, redirect
from . import forms
# Create your views here.


def add_category(request):
    if request.method == 'POST':  # user post request koreche
        # user er post request data ekhane capture korlam
        category_form = forms.CategoryForm(request.POST)
        if category_form.is_valid():  # post kora data gula amra valid kina check kortechi
            category_form.save()  # jodi data valid hoy taile database e save korbo
            # sob thik thakle take add author ei url e pathiye dibo
            return redirect('add_category')

    else:  # user normally website e gele blank form pabe
        category_form = forms.CategoryForm()
    return render(request, 'add_category.html', {'form': category_form})
