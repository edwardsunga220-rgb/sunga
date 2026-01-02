from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import InquiryForm

def index(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been deployed successfully!")
            return redirect('core:index') # Redirect on success
        else:
            # If invalid, we don't redirect. We let the code fall through 
            # to the render() below, carrying the 'form' with errors.
            messages.error(request, "Deployment failed. Please fix the errors below.")
    else:
        form = InquiryForm()

    return render(request, 'index.html', {'form': form})