from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .forms import EntryForm
from .models import Entry


def entry_list(request):
    return render(request, 'tracker/entry_list.html', {
        'object_list': Entry.objects.order_by('project__name'),
    })


@login_required
def entry_add(request):
    if not request.user.has_perm('tracker.add_entry'):
        messages.warning(request, 'You do not have permission to add entries.')
        return redirect('entry-list')

    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('entry-list')
    else:
        form = EntryForm()

    return render(request, 'tracker/entry_form.html', {'form': form})


@login_required
def entry_edit(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    if entry.user != request.user:
        return HttpResponseForbidden()

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


@login_required
def entry_stop(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)

    if entry.end is None:
        entry.end = timezone.now()
        entry.save()

    return redirect('entry-list')


def entry_continue(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)

    if entry.end is not None:
        entry.pk = None
        entry.start = timezone.now()
        entry.end = None
        entry.save()

    return redirect('entry-list')
