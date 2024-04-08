from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView

from .models import News, Category
from .forms import ContactForm

# Create your views here.


def news_list(request):
    news_list = News.published.all()
    context = {
        "news_list": news_list
    }
    return render(request, "news/news_list.html", context)


def news_detail(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published)
    context = {
        "news": news
    }
    return render(request, 'news/news_detail.html', context)

def indexView(request):
    news_list = News.published.all().order_by('-publish_time')[:10]
    categories = Category.objects.all()
    local_news = News.published.all().filter(category__name="mahalliy").order_by("-publish_time")[1:6]
    local_one = News.published.filter(category__name="mahalliy").order_by("-publish_time")[:1]
    context = {
        'news_list': news_list,
        "categories": categories,
        "local_news": local_news,
        "local_one": local_one
    }

    return render(request, 'news/index.html', context)


class IndeView(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['news_list'] = News.published.all().order_by('-publish_time')[:5]
        context['mahalliy_xabarlar'] = News.published.all().filter(category__name="mahalliy").order_by("-publish_time")[1:6]
        context['xorij_xabarlari'] = News.published.all().filter(category__name="xorij").order_by("-publish_time")[1:6]
        context['sport_xabarlar'] = News.published.all().filter(category__name="sport").order_by("-publish_time")[1:6]
        context['texnologiya_xabarlar'] = News.published.all().filter(category__name="texnologiya").order_by("-publish_time")[1:6]
        return context



def erroPageViwe(request):
    context = {

    }
    return render(request, 'news/404.html', context)

# def contactPageView(request):
#     form = ContactForm(request.POST or None)
#     if request.method == "POST" and form.is_valid():
#         form.save()
#         return HttpResponse("<h2> Biz bilan bog`langaningiz uchun raxmat! </h2>")
#     context = {
#         "form": form
#     }
#     return render(request, 'news/contact.html', context)

class ContactPageView(TemplateView):
    template_name = 'news/contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            "form": form
        }
        return render(request, 'news/contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == "POST" and form.is_valid():
            form.save()
            return HttpResponse("<h2> biz bilan bog`langaningiz uchun raxmat</h2>")
        context = {
            "form": form
        }

        return render(request, 'news/contact.html', context)


class LocalNewsView(ListView):
    model = News
    template_name = 'news/mahalliy.html'
    context_object_name = 'mahalliy_yangiliklar'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='mahalliy')
        return news


class ForeignNewsView(ListView):
    model = News
    template_name = 'news/xorij.html'
    context_object_name = 'xorij_yangiliklar'

    def get_queryset(self):
        news=self.model.published.all().filter(category__name="xorij")


class TechnoNewsView(ListView):
    model = News
    template_name = 'news/texnologiya.html'
    context_object_name = 'texnologiya_yangiliklar'

    def get_queryset(self):
        news=self.model.published.all().filter(category__name='texnologiya')


class SportNewsView(ListView):
    model = News
    template_name = 'news/sport.html'
    context_object_name = 'sport_yangiliklar'

    def get_queryset(self):
        news=self.model.published.all().filter(category__name='sport')