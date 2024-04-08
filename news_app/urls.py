from django.urls import path

from .views import news_list, news_detail, indexView, ContactPageView, erroPageViwe, IndeView, ForeignNewsView, SportNewsView, TechnoNewsView, LocalNewsView

urlpatterns = [
    path('', IndeView.as_view(), name='home_page'),
    path('news/', news_list, name='all_new_list'),
    path("news/<slug:news>/", news_detail, name='news_detail_page'),
    path('contact-us/', ContactPageView.as_view(), name='contact_page'),
    path('404/', erroPageViwe, name='error_page'),
    path('local-news/', ForeignNewsView.as_view(), name='local_news_page'),
    path('techno-views/', TechnoNewsView.as_view(), name='techno_news_page'),
    path('sport-news/', SportNewsView.as_view(), name='sport_news_page'),
    path('foreign-news/', ForeignNewsView.as_view(), name='foreign_news_page'),
]