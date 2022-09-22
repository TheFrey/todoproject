from django.shortcuts import render, HttpResponse, redirect
from .forms import LoginForm, UserRegistrationForm, TodoItemForm, SubItemForm
from django.contrib.auth import authenticate, login
from .models import ToDoItem, SubItem
from django.urls import reverse


def delete_item(request, idx):
    if request.method == 'POST':
        item = ToDoItem.objects.get(id=idx)
        item.delete()
        return HttpResponse('Deleted')
    else:
        return render(request, 'delete.html')


def modify_item(request, idx):
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('text')
            urgency = form.cleaned_data.get('urgency')
            item_to_modify = ToDoItem.objects.get(id=idx)
            item_to_modify.text = text
            item_to_modify.urgency = urgency
            item_to_modify.save()
            return HttpResponse('Updated')
    else:
        form = TodoItemForm()
        return render(request, 'modify.html', {'form': form})


def add_sub(request, idx, date):
    if request.method == 'POST':
        form = SubItemForm(request.POST)
        if form.is_valid():
            # Create a new user object but avoid saving it yet
            data = form.cleaned_data.get('text')
            new_sub_item = SubItem()
            new_sub_item.item = ToDoItem.objects.get(id=idx, date=date)
            new_sub_item.text = data
            new_sub_item.save()
            return HttpResponse('added')
    else:
        sub_item = SubItemForm()
        return render(request, 'add_sub.html', {'form': sub_item})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(todo_list)
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def todo_list(request, urgency_slug=None):

    if request.method == 'POST':
        form = TodoItemForm(data=request.POST)

        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()

            return redirect(todo_list)

    else:
        if request.user.is_authenticated:
            if urgency_slug:
                todo_items = ToDoItem.objects.filter(user=request.user, urgency=urgency_slug)
            else:
                todo_items = ToDoItem.objects.filter(user=request.user)
            sub_item = SubItem.objects.all()
            sub_item_list = []
            for item in sub_item:
                if item.item in todo_items:
                    sub_item_list.append(item)
            form = TodoItemForm()
            urgency_list = ['white', 'red', 'darkorange', 'green']
            urgency_url = [reverse('todo_list_by_urgency', args=[item]) for item in urgency_list]
            return render(request, 'list.html', {'items': todo_items,
                                                 'sub_item': sub_item_list,
                                                 'form': form,
                                                 'urg_url': urgency_url})

        else:
            return redirect(register)

