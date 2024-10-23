from django.shortcuts import render, redirect
from . import callDB
from .forms import ContactForm


def contact_list_view(request):
    query = "SELECT * FROM api_contact"  # Adjust for your database schema
    form = callDB(query)
    return render(request, 'contact_list.html', {'form': form})


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/success')  
    else:
        form = ContactForm()  # This should always create a new form on GET request
    return render(request, 'formulaireNom.html', {'form': form})