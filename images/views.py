from django.contrib import messages
from django.shortcuts import render, redirect

from images.forms import ImageCreateForm


def image_create(request):
    if request.method == 'POST':
        # Form is sent
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            # Form data is valid
            cd = form.cleaned_data
            new_item = form.save(commit=False)

            # Assign current user to the item
            new_item.user = request.user
            new_item.save()
            messages.success(request, 'Image added successfully')

            # Redirect to new created item detail view
            return redirect(new_item.get_absolute_url())
    else:
        # Build form with data provided by the bookmarklet via GET
        form = ImageCreateForm(data=request.GET)

    return render(request, 'images/image/create.html',
                  {'section': 'images',
                   'form': form})
