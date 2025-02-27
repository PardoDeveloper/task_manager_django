from django import forms
from .models import Contact

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["nombre", "apellido", "correo", "telefono", "mensaje"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "w-full p-2 border rounded-lg"}),
            "apellido": forms.TextInput(attrs={"class": "w-full p-2 border rounded-lg"}),
            "correo": forms.EmailInput(attrs={"class": "w-full p-2 border rounded-lg"}),
            "telefono": forms.TextInput(attrs={"class": "w-full p-2 border rounded-lg"}),
            "mensaje": forms.Textarea(attrs={"class": "w-full p-2 border rounded-lg", "rows": 4}),
        }
