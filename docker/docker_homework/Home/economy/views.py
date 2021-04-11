from django.shortcuts import render
from economy.models import EconomyNews
from django.views.generic import ListView, DetailView
from economy.forms import EconomySearchForm
from django.views.generic.edit import FormView
from django.db.models import Q
import os

# Create your views here.

class EconomyLV(ListView):
    model = EconomyNews
    template_name = 'economy_list.html'
    paginate_by = 20

class EconomyDV(DetailView):
    model = EconomyNews

class EconomySearchFormView(FormView):
    form_class = EconomySearchForm 
    template_name = "economy/economy_search.html"

    def form_valid(self, form):
        schword = self.request.POST['search_word']
        economy_list = EconomyNews.objects.filter(Q(title__icontains=schword) | Q(paper__icontains=schword) | Q(summary__icontains=schword)).distinct()

        # 검색된 결과 
        context = {}

        context['form'] = form
        context['search_keyword'] = schword
        context['search_list'] = economy_list

        return render(self.request, self.template_name, context) 

