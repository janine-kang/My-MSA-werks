from django.shortcuts import render
from itnews.models import IT_news
from django.views.generic import ListView, DetailView
from itnews.forms import RefreshForm
from itnews.forms import ITnewsSearchForm
from django.views.generic.edit import FormView
from django.db.models import Q
import os

# Create your views here.

class BreakingsLV(ListView):
    model = IT_news
    template_name = 'it_news_list.html'
    paginate_by = 20

class BreakingsDV(DetailView):
    model = IT_news

class SearchFormView(FormView):
    form_class = ITnewsSearchForm 
    template_name = "itnews/it_news_search.html"

    def form_valid(self, form):
        schword = self.request.POST['search_word']
        it_news_list = IT_news.objects.filter(Q(title__icontains=schword) | Q(paper__icontains=schword) | Q(summary__icontains=schword)).distinct()

        # 검색된 결과 
        context = {}

        context['form'] = form
        context['search_keyword'] = schword
        context['search_list'] = it_news_list

        return render(self.request, self.template_name, context) 

class RefreshFormView(FormView):
    template_name = "itnews/it_news_list.html"
    form_class = RefreshForm
    success_url = '/IT/'
    context_object_name = "news" 

    paginate_by = 20


    def form_valid(self, form):
        print(self.request)
        os.chdir('/Users/janine-kang/Desktop/SecondChance/Home/scraper')
        os.system('scrapy crawl IT')
        return super().form_valid(form)