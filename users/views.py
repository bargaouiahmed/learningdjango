from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('posts:posts_list')  # Redirect after successful registration
    else:
        form = UserCreationForm()
    # The render statement should not be inside the `else` block
    return render(request, 'registration/register.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid() :
            login(request, form.get_user())
            if "next" in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('posts:posts_list')

    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})
def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('users:login')
