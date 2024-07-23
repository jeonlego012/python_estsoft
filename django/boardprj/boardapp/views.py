from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils import timezone
from django.core.paginator import Paginator

from .forms import BoardModelForm
from .models import Board

# Create your views here.
def index(request):
    return render(request, 'boardapp/index.html')

# function-based
def list(request):
    boards = Board.objects.all()

    return render(request, 'boardapp/list.html', {'boards':boards})

def create(request):
    if request.method == "POST":
        form = BoardModelForm(request.POST)
        print(f"result!!! {form['title'].data}")

        form.save()

        return redirect('boardapp:index')
    else:
        form = BoardModelForm()

        return render(request, 'boardapp/create.html', {'form':form})
    
# class-based
class BoardListView(ListView):
    model = Board
    paginate_by = 20

    # 내장 객체. default는 board_list.html({model이름}_list.html)
    template_name="boardapp/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        print(f"result!! {paginator.page_range} {paginator.count}")

        return context

class BoardDetailView(DetailView):
    model  = Board
    pk_url_kwarg = 'id'
    template_name = 'boardapp/detail.html'

class BoardCreateView(CreateView):
    model = Board
    fields =  BoardModelForm().fields
    template_name = 'boardapp/create.html'

    def get_success_url(self):
        return reverse('boardapp:list')

class BoardUpdateView(UpdateView):
    model = Board
    fields = BoardModelForm().fields
    pk_url_kwarg = 'id'
    template_name = 'boardapp/update.html'

    def get_object(self):
        obj = super().get_object()
        obj.updated_at = timezone.now()
        return obj
    
    def get_success_url(self):
        return reverse('boardapp:list')
    
class BoardDeleteView(DeleteView):
    model = Board
    pk_url_kwarg = 'id'
    template_name = 'boardapp/delete.html'

    success_url = reverse_lazy('boardapp:list')
