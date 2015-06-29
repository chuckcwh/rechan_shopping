from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # General
    url(r'^$', 'rechan_shopping.views.index', name='index'),
    # url(r'^profile/$', 'rechan_shopping.views.profile', name='profile'),
    # url(r'^cart/$', 'rechan_shopping.views.cart', name='cart'),
    # url(r'^faq/$', 'rechan_shopping.views.faq', name='faq'),
    # url(r'^product/(?P<cat>[0-9A-Za-z_\-]+)/$', 'rechan_shopping.views.prod_list', name='prod_list'),
    # url(r'^product/(?P<prod_id>\d+)/$', 'rechan_shopping.views.product', name='product'),
    # url(r'^stock/$', 'rechan_shopping.views.stock', name='stock'),
    # url(r'^stock/(?P<prod_id>[0-9A-Za-z_\-]+)$', 'rechan_shopping.views.stock_detail', name='stock_detail'),
    # url(r'^admin_purchase_confirm/$', 'rechan_shopping.views.admin_purchase_confirm', name='admin_purchase_confirm'),
    # url(r'^admin/', include(admin.site.urls)),

    # # Ajax
    # url(r'^get_cart_items/$', 'rechan_shopping.views.get_cart_items', name='get_cart_items'),
    # url(r'^get_stock/(?P<cat>[0-9A-Za-z_\-]+)/$', 'rechan_shopping.views.get_stock', name='get_stock'),
    

    # # Account management
    # url(r'^register/$', 'rechan_shopping.views.register', name='register'),
    # url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    # url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': 'index'}, name='logout',),
    # url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    # url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     'django.contrib.auth.views.password_reset_confirm',
    #     name='password_reset_confirm'),
    # url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)