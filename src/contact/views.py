from django.shortcuts import render, redirect
from .forms import ContactoForm
from .models import Contact
from .serializers import ContactSerializer
from rest_framework import viewsets

def contact(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda los datos en la base de datos
            return redirect("contact")  # Redirige después de enviar
    else:
        form = ContactoForm()
    
    return render(request, "contact.html", {"form": form})

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer