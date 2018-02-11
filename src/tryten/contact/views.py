from django.shortcuts import render
from .forms import contactforms
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def contact(request):
    title='contact'
    form=contactforms(request.POST or None)
    context={'title':title,'form':form,}
    confirm_message=None
    if form.is_valid():
        print("hi")
        name=form.cleaned_data['name']
        comment=form.cleaned_data['comment']
        subject='message form MYSite '
        message='%s %s' %(comment,name)
        emailfrom=form.cleaned_data['email']
        emailto=[settings.EMAIL_HOST_USER]
        send_mail(subject,message,emailfrom,emailto,fail_silently=True)
        title='thanks '
        confirm_message='thnaks for the message. we will get right back to you'
        form=None

    context={'title':title,'form':form,'confirm_message':confirm_message,}
    template='contact/contact.html'
    return render(request,template,context)
