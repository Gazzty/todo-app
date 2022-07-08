from django.shortcuts import redirect
from django.shortcuts import get_object_or_404, render
from .models import Todo
from .forms import TodoForm

# Create your views here.
def todo_view (request):
    obj = Todo.objects.all()
    my_context = {
        'query': obj
        }
    return render(request, 'todoView.html', my_context)

def todo_create_view (request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TodoForm()
    my_context = {
        'form': form
        }
    return render(request, 'todoCreate.html', my_context)

def todo_delete_view(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/')