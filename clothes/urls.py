"""
URL configuration for clothes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sale import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView



urlpatterns=[
    path('admin/', admin.site.urls),
    path('',views.home),
    path('home/',views.home),
    path('about/',views.about),
    path('product/',views.product),
    path('contact/',views.contact),
    path('product_detail/', views.product_detail),
# =====================================================================================================================
#



# ==================================================================================================
#  URL OF Registration form (BY Raghvendra Sir)
   path('login/',views.user_login),
   path('register/',views.register),
   path('logout/',views.user_logout),
# ==================================================================================================
# URL for forgot password

   path('reset_password/', PasswordResetView.as_view(template_name = 'home/passwordreset/password_reset.html'),name='reset_password'),
   path('password_reset_done/', PasswordResetDoneView.as_view(template_name = 'home/passwordreset/password_reset_done.html'),name='password_reset_done'),
   path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name = 'home/passwordreset/password_reset_confirm.html'),name='password_reset_confirm'),
   path('password_reset_complete/',PasswordResetCompleteView.as_view(template_name = 'home/passwordreset/password_reset_complete.html'),name='password_reset_complete'),

# ================================================================================================
#  Url for Add to Cart
# =================================================================================================
    path('add_to_cart/',views.add_to_cart,name='add_to_cart'),
    path('show_cart/',views.show_cart,name='show_cart'),

 
 
#  path('our_products/product/cart/',views.cartOurProducts,name='home_latest_product_cart/'),














# Dashboard URLS


# For Dashboard URL
   path('dashboard/',views.dash_home,name='dashboard'),
   


# For Dashboard   URL of Home Models

 # URL of Model Home

    path('dash/home/',views.home_info,name='dash_home'),
    path('dash/home/add/',views.dashHomeAdd,name='dash_home_add'),
    path('dash/home/del/<int:id>/',views.dashHomeDel,name='dash_home_del'),
    path('dash/home/up/<int:id>/',views.dashHomeUp,name='dash_home_up'),

# URL of Home Page of Model (Home) of dashboard.Html
    path('dash/home/page/',views.dashHomePage,name='dash_home_page'),


# URL of Model Home section (Latest_Product)
    path('dash/home/latest_product/',views.homeLatestProduct,name='dash_home_latest_product'),
    
    path('dash/home/latest_product/add/',views.homeLatestProduct_add,name='dash_home_latest_product_add'),

    path('dash/home/latest_product/del/<int:id>/',views.homeLatestProduct_del,name='dash_home_latest_product_del'),

    path('dash/home/latest_product/up/<int:id>/',views.homeLatestProduct_up,name='dash_home_latest_product_up'),
    
    

# URL of Model Home section (Sixteen)
    path('dash/home/six/',views.home_six,name='dash_home_six'),

    path('dash/home/six/add/',views.home_sixAdd,name='dash_home_six_add'),

    path('dash/home/six/del/<int:id>/',views.home_sixDel,name='dash_home_six_del'),

    path('dash/home/six/up/<int:id>/',views.home_sixUp,name='dash_home_six_up'),


# ================================================================================================
# For Dashboard   URL of About Models

# URL of Model About
  
    path('dash/about/',views.about_info,name='dash_about'),

    path('dash/about/add/',views.aboutAdd,name='dash_about_add'),

    path('dash/about/del/<int:id>/',views.aboutDel,name='dash_about_del'),

    path('dash/about/up/<int:id>/',views.aboutUp,name='dash_about_up'),

 # URL of Home Page of Model (About) of dashboard.html
    path('dash/about/page/',views.dashAboutPage,name='dash_about_page'),

# URL of Model About section (Member)

    path('dash/about/member/',views.about_member,name='dash_about_member'),

    path('dash/about/member/add/',views.about_memberAdd,name='dash_about_member_add'),

    path('dash/about/member/del/<int:id>/',views.about_memberDel,name='dash_about_member_del'),

    path('dash/about/member/up/<int:id>/',views.about_memberUp,name='dash_about_member_up'),


# URL of Model About section (Service)

    path('dash/about/service/',views.about_service,name='dash_about_service'),

    path('dash/about/service/add/',views.about_serviceAdd,name='dash_about_service_add'),

    path('dash/about/service/del/<int:id>/',views.about_serviceDel,name='dash_about_service_del'),

    path('dash/about/service/up/<int:id>/',views.about_serviceUp,name='dash_about_service_up'),

# URL of Model About section (Partner)

     path('dash/about/partner/',views.about_partner,name='dash_about_partner'),
     path('dash/about/partner/add/',views.about_partnerAdd,name='dash_about_partner_add'),
     path('dash/about/partner/del/<int:id>/',views.about_partnerDel,name='dash_about_partner_del'),
     path('dash/about/partner/up/<int:id>/',views.about_partnerUp,name='dash_about_partner_up'),

# ================================================================================================
   
   
#  URL of Model Products section (Product)

 path('dash/product/',views.product_info,name='dash_product'),
 path('dash/product/add/',views.productAdd,name='dash_product_add'),
 path('dash/product/del/<int:id>/',views.productDel,name='dash_product_del'),
 path('dash/product/up/<int:id>/',views.productUp,name='dash_product_up'),

 # URL of Product Page of Model (Product) of dashboard.html

 path('dash/product/page/',views.dashproductPage,name='dash_product_page'),

# ================================================================================================
 #  URL of Model Products section (Product_ban)

 path('dash/product_ban/',views.product_banner,name='dash_product_banner'),
 path('dash/product_ban/add/',views.product_bannerAdd,name='dash_product_banner_add'),
 path('dash/product_ban/del/<int:id>/',views.product_bannerDel,name='dash_product_banner_del'),
 path('dash/product_ban/up/<int:id>/',views.product_bannerUp,name='dash_product_banner_up'),
 

# =============================================================================================
#  URL of Model Cotact


#  URL of Model Contact section (Contact_ban)
 path('dash/contact_ban/',views.contactBan,name='dash_contact_ban'),
 path('dash/contact_ban/add/',views.contactBan_add,name='dash_contact_ban_add'),
 path('dash/contact_ban/del/<int:id>/',views.contactBan_Del,name='dash_contact_ban_del'),
path('dash/contact_ban/up/<int:id>/',views.contactBan_Up,name='dash_contact_ban_up'),


# URL of Contact Page of Model (Contact) of dashboard.html

 path('dash/contact/page/',views.dashContactPage,name='dash_contact_page'),

#  URL of Model Contact section (Contact_desc)
 path('dash/contact_desc/',views.contact_desc,name='dash_contact_desc'),
 path('dash/contact_desc/add/',views.contact_descAdd,name='dash_contact_desc_add'),
 path('dash/contact_desc/del/<int:id>/',views.contact_descDel,name='dash_contact_desc_del'),
 path('dash/contact_desc/up/<int:id>/',views.contact_descUp,name='dash_contact_desc_del'),

# URL of Model Contact section (Con_Partner)
path('dash/contact/part/',views.contact_part,name='dash_contact_part'),
path('dash/contact/part/add/',views.contact_partAdd,name='dash_contact_part_add'),
path('dash/contact/part/del/<int:id>/',views.contact_partDel,name='dash_contact_part_del'),
path('dash/contact/part/up/<int:id>/',views.contact_partUp,name='dash_contact_part_up'),

# URL of Model Contact section (Contact form)
path('dash/contact_form/',views.contact_form,name='dash_contact_form'),
path('dash/contact_form/add/',views.contact_formAdd,name='dash_contact_form'),
path('dash/contact_form/del/<int:id>/',views.contact_formDel,name='dash_contact_form_del'),
path('dash/contact_form/up/<int:id>/',views.contact_formUp,name='dash_contact_form_del'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
