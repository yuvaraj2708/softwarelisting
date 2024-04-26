from django.shortcuts import render,redirect
from .models import *
from django.shortcuts import render, get_object_or_404
from .forms import *
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.core.mail import send_mail

def logout_view(request):
    logout(request)
    return redirect('login')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('submit')  # Replace 'index' with the name of your desired view
        else:
            # Authentication failed
            # You might want to add a message here indicating login failed
            pass
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def index(request):
    categories = Category.objects.all()
    return render(request,"index.html", {'categories': categories})

def get_software_lists(request, subcategory_id):
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    software_lists = SoftwareList.objects.filter(subcategory_id=subcategory_id)

    keyword = request.GET.get('keyword')
    if keyword:
        software_lists = software_lists.filter(heading__icontains=keyword)

    if request.method == 'POST':
        selected_software_ids = request.POST.getlist('selected_software')
        if selected_software_ids:
            return redirect('compare_software', ids=','.join(selected_software_ids))

    return render(request, 'software_lists.html', {'software_lists': software_lists, 'categories': categories, 'subcategories': subcategories})


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

def create_category(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_details')  # Redirect to the page where all details are shown
    else:
        form = CategoryForm()
    return render(request, 'create_category.html', {'form': form,'categories':categories})

def create_subcategory(request):
    if request.method == 'POST':
        form = SubcategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_details')  # Redirect to the page where all details are shown
    else:
        form = SubcategoryForm()
    return render(request, 'create_subcategory.html', {'form': form})

def create_softwarelist(request):
    if request.method == 'POST':
        form = SoftwarelistForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_details')  # Redirect to the page where all details are shown
    else:
        form = SoftwarelistForm()
    return render(request, 'create_softwarelist.html', {'form': form})



def compare_software(request, ids):
    # Convert the comma-separated string of IDs into a list
    software_ids = ids.split(',')
    # Retrieve software details based on the selected IDs
    selected_software = SoftwareList.objects.filter(id__in=software_ids)
    return render(request, 'compare_software.html', {'selected_software': selected_software})


def price(request):
    categories = Category.objects.all()
    return render(request,'price.html',{'categories':categories})

@login_required
def enquiry(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Send email
            send_mail(
                subject,
                f"Name: {name}\nEmail: {email}\nMessage: {message}",
                'your-email@example.com',  # Replace with your email
                ['yuvaraj.margy@gmail.com'],  # Receiver's email
                fail_silently=False,
            )
            messages.success(request, 'Your enquiry has been submitted successfully!')
            return redirect('enquiry')
    else:
        form = EnquiryForm()
    return render(request, 'enquiry.html', {'form': form})


def my_listing(request):
    categories = Category.objects.all()
    return render(request,'my_listing.html',{'categories':categories})