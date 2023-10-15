from django.urls import path

from .views import main_view

app_name = 'some_main_app'

urlpatterns = [
    path('', main_view, name='index'),
    path('white_label/', main_view, name='white_label'),
    path('about/', main_view, name='about'),
    path('services/', main_view, name='services'),
    path('contacts/', main_view, name='contacts'),
    path('white_label/forex_crm', main_view, name='forex_crm'),
    path('white_label/mt4_mt5', main_view, name='mt4_mt5'),
    path('white_label/mt4_mt5', main_view, name='mt4_mt5'),
    path('white_label/web_forex_terminal',
         main_view, name='web_forex_terminal'),
    path('white_label/ctrader/', main_view, name='ctrader'),
    path('about/news', main_view, name='news'),
    path('about/contacts/phones', main_view, name='phones'),
    path('about/contacts/phones/tel1', main_view, name='tel1'),
    path('about/contacts/phones/tel2', main_view, name='tel2'),
    path('about/contacts/phones/tel3', main_view, name='tel3'),
    path('about/contacts/email', main_view, name='email'),
    path('about/contacts/email/email_box1', main_view, name='email_box1'),
    path('about/contacts/email/email_box2', main_view, name='email_box2'),
]
