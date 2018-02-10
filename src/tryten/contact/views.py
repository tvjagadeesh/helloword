from django.shortcuts import render
from .forms import contactforms
# Create your views here.
def contact(request):
    form=contactforms(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data['email'])
    context=locals()
    template='contact/contact.html'
    return render(request,template,context)
