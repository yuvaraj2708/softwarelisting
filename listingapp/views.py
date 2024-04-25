from django.shortcuts import render,redirect
from .models import *
from django.shortcuts import render, get_object_or_404
from .forms import *

def index(request):
    categories = Category.objects.all()
    return render(request,"index.html", {'categories': categories})

def get_software_lists(request, subcategory_id):
    categories = Category.objects.all()
    software_lists = SoftwareList.objects.filter(subcategory_id=subcategory_id)
    return render(request, 'software_lists.html', {'software_lists': software_lists,'categories': categories})

def view_software_details(request, software_id):
    categories = Category.objects.all()
    software = get_object_or_404(SoftwareList, pk=software_id)
    return render(request, 'view_software.html', {'software': software,'categories': categories})

def all_details(request):
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    softwarelist = SoftwareList.objects.all()
    return render(request, 'all_details.html', {'categories': categories, 'subcategories': subcategories, 'softwarelist': softwarelist})

def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('all_details')  # Redirect to the page where all details are shown
    else:
        form = CategoryForm(instance=category)
    return render(request, 'edit_category.html', {'form': form})

def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('all_details')  # Redirect to the page where all details are shown
    # If method is GET or any other, you may render a confirmation page here
    return render(request, 'confirm_delete_category.html', {'category': category})

def edit_subcategory(request, subcategory_id):
    subcategory = get_object_or_404(Subcategory, id=subcategory_id)
    if request.method == 'POST':
        form = SubcategoryForm(request.POST, instance=subcategory)
        if form.is_valid():
            form.save()
            return redirect('all_details')  # Redirect to the page where all details are shown
    else:
        form = SubcategoryForm(instance=subcategory)
    return render(request, 'edit_subcategory.html', {'form': form})

def delete_subcategory(request, subcategory_id):
    subcategory = get_object_or_404(Subcategory, id=subcategory_id)
    if request.method == 'POST':
        subcategory.delete()
        return redirect('all_details')  # Redirect to the page where all details are shown
    # If method is GET or any other, you may render a confirmation page here
    return render(request, 'confirm_delete_subcategory.html', {'subcategory': subcategory})

def edit_softwarelist(request, softwarelist_id):
    softwarelist = get_object_or_404(SoftwareList, id=softwarelist_id)
    if request.method == 'POST':
        form = SoftwarelistForm(request.POST, instance=softwarelist)
        if form.is_valid():
            form.save()
            return redirect('all_details')  # Redirect to the page where all details are shown
    else:
        form = SoftwarelistForm(instance=softwarelist)
    return render(request, 'edit_softwarelist.html', {'form': form})

def delete_softwarelist(request, softwarelist_id):
    softwarelist = get_object_or_404(SoftwareList, id=softwarelist_id)
    if request.method == 'POST':
        softwarelist.delete()
        return redirect('all_details')  # Redirect to the page where all details are shown
    # If method is GET or any other, you may render a confirmation page here
    return render(request, 'confirm_delete_softwarelist.html', {'softwarelist': softwarelist})