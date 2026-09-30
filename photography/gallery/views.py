from django.shortcuts import render, HttpResponseRedirect # type: ignore
from gallery.forms import GalleryForm
from gallery.models import Gallery
from django.contrib import messages  # type: ignore


#ADMIN PANEL 
#USERNAME:admin & PASSWORD:admin

# Create your views here.
def root_file(request):
    return render(request, 'root.html')

def home_page(request):
    context = {'home': 'active'}
    return render(request, 'home.html', context)

def about_page(request):
    context = {'about': 'active'}
    return render(request, 'about.html', context)

def contect_page(request):
    context = {'contect': 'active'}
    return render(request, 'contect.html', context)

def dashboard_view(request):
    if request.user.is_authenticated:
        context = {'dashboard': 'active'}
        return render(request, 'dashboard.html', context)
    else:
        return HttpResponseRedirect('/login/')

    

def upload_img_view(request, context=None):
    if request.user.is_authenticated:
        context = context or {}
        context['upload'] = 'active'

        if request.method == 'POST':
            form = GalleryForm(request.POST, request.FILES)
            if form.is_valid():
                data = form.save(commit=False)
                data.user = request.user
                data.save()
                messages.success(request, 'Your image uploaded Successfully!!!')
                return HttpResponseRedirect('/view_img/')
        else:
            form = GalleryForm()

        context['form'] = form
        return render(request,'upload_img.html', context)
    else:
        return HttpResponseRedirect('/login/')


def view_img_view(request, context=None):
    if request.user.is_authenticated:
        context = context or {}
        context['view'] = 'active'
        candidates = Gallery.objects.filter(user=request.user).order_by('-uploaded_at')
        context['candidates'] = candidates
        return render(request, 'view_img.html', context)
    else:
        return HttpResponseRedirect('/login/')
    
def all_picture_page(request):
    if request.user.is_authenticated:
        candidates = Gallery.objects.filter(user=request.user).order_by('-uploaded_at')
        return render(request, 'all_pictures.html', {'candidates': candidates})
    else:
        return HttpResponseRedirect('/login/')

# FOR EDIDING THE POST IMAGE
def edit_data(request, id):
    if request.user.is_authenticated:
        try:
            pi = Gallery.objects.get(pk=id, user=request.user)
        except Gallery.DoesNotExist:
            messages.error(request, "Image not found or access denied.")
            return HttpResponseRedirect('/view_img/')
        
        if request.method == 'POST':
            fm = GalleryForm(request.POST, request.FILES, instance=pi)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Your image updated successfully!')
                return HttpResponseRedirect('/view_img/')
        else:
            fm = GalleryForm(instance=pi)

        return render(request, 'edit_data.html', {'form': fm})
    else:
        return HttpResponseRedirect('/login/')


#FOR DELETE THE IMAGE WHICH UPLOADED
def delete_img(request, id):
    if request.method == 'POST':
        pi = Gallery.objects.get(pk=id)
        pi.delete()
        messages.success(request, 'Your Image Deleted Successfully!!!')
        return HttpResponseRedirect('/view_img/')
