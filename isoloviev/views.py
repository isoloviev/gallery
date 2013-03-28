from django.core.mail import mail_admins
from django.http import HttpResponseRedirect
from django.shortcuts import render
from isoloviev.models import ContactForm


def home(request):
    return render(request, 'home.html')


def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail_admins('Web Site User Feedback - %s (%s)' % (form.cleaned_data['name'], form.cleaned_data['email']),
                        form.cleaned_data['message'])
            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()

    return render(request, 'contacts.html', {
        'form': form,
    })


def about(request):
    return render(request, 'about.html')