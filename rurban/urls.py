
from django.contrib import admin
from django.urls import path
from zgoruban.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include

urlpatterns = [
    path('djrichtextfield/', include('djrichtextfield.urls')),
    path('admin/', admin.site.urls),
    path('',Home,name= 'home'),
    path('contact',CONTACT,name= 'contact'),
    path('oppurtunities',OPPURTUNITIES,name= 'oppurtunities'),
    path('camps',CAMPS,name= 'camps'),
    path('gallery',GALLERYS,name= 'gallery'),
    path('about',ABOUT,name= 'about'),
    path('blogs',BLOGSS,name= 'blogs'),
    path('demo',DEMO,name= 'demo'),
    path('events',EVENTS,name= 'events'),
    path('news',NEWS,name= 'news'),
    path('terms_conditions',TERMS_CONDITIONS,name= 'terms_conditions'),
    path('privacy_policy',PRIVACY_POLICY,name= 'privacy_policy'),
    path('paymrnt_procedure',PAYMENT_PROCEDURE,name= 'payment_procedure'),
    path('Logout/',LOGOUT,name='Logout'),
    path('Login/',LOGIN,name='Login'),
    path('Forgot/',FORGOT,name='Forgot'),
####           dynamic urls       #######
    path('blog_single/<int:blo_id>/',BLOG_SINGLE, name='blog_single'),
    path('camps_dynamics/<int:cmp_id>/', CAMPS_SINGLE, name='camps_dynamics'),

#####       admin pannel   ##########
    path('admin_index',ADMIN_INDEX,name= 'admin_index'),
    path('admin_contact',ADMIN_CONTACT,name= 'admin_contact'),
    path('admin_opportunities',ADMIN_OPPORTUNITIES,name= 'admin_opportunities'),
    path('admin_mail',ADMIN_MAIl,name= 'admin_mail'),
    path('admin_about',ADMIN_ABOUT,name= 'admin_about'),
    path('admin_home', ADMIN_HOME, name='admin_home'),
    path('admin_home2', ADMIN_HOME2, name='admin_home2'),
    path('admin_home3', ADMIN_HOME3, name='admin_home3'),
    path('admin_home4', ADMIN_HOME4, name='admin_home4'),
    path('admin_camps', ADMIN_CAMPS, name='admin_camps'),
    path('admin_news', ADMIN_NEWS, name='admin_news'),
    path('admin_gallery', ADMIN_GALLERY, name='admin_gallery'),
    path('admin_blogs', ADMIN_BLOGS, name='admin_blogs'),
    path('admin_events', ADMIN_EVENTS, name='admin_events'),
    path('admin_youtube',ADMIN_YOUTUBE, name='admin_youtube'),

####  admin delete  ####
    path('admin_gallery_delete/<int:del_id>/', ADMIN_GALLERY_DELETE, name='admin_gallery_delete'),
    path('admin_news_delete/<int:del_id>/', ADMIN_NEWS_DELETE, name='admin_news_delete'),
    path('admin_events_delete/<int:del_id>/', ADMIN_EVENTS_DELETE, name='admin_events_delete'),
    path('admin_blogs_delete/<int:del_id>/', ADMIN_BLOGS_DYNAMICC_DELETE, name='admin_blogs_delete'),
    path('admin_team_delete/<int:del_id>/', ADMIN_TEAM_DELETE, name='admin_team_delete'),
    path('admin_testimony_delete/<int:del_id>/', ADMIN_TESTIMONY_DELETE, name='admin_testimony_delete'),
    path('admin_camps_delete/<int:del_id>/', ADMIN_CAMPS_DELETE, name='admin_camps_delete'),
    path('admin_participant_delete/<int:del_id>/', ADMIN_PARTICPANT_DELETE, name='admin_participant_delete'),

####### admin dynamic functions  ######
    path('admin_blogs_dynamic/<int:bdy_id>/', ADMIN_BLOGS_DYNAMICC, name='admin_blogs_dynamic'),
    path('admin_camps_dynamic/<int:camp_id>/', ADMIN_CAMPS_DYNAMICC, name='admin_camps_dynamic'),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)