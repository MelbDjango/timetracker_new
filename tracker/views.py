from django.shortcuts import render, redirect, get_object_or_404

from .models import Entry
from .forms import EntryForm


def entry_list(request):
    return render(request, 'tracker/entry_list.html', {
        'object_list': Entry.objects.all(),
    })

def entry_add(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save()
            return redirect('entry-list')

    else:
        form = EntryForm()

    return render(request, 'tracker/entry_form.html', {'form': form})


def entry_edit(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)

    if request.method == 'POST':
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('entry-list')

    else:
        form = EntryForm(instance=entry)

    return render(request, 'tracker/entry_form.html', {
        'object': entry,
        'form': form,
    })
