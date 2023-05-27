from django.urls import path
from .views import*

urlpatterns=[
    path('',index),
    path('reg',register),
    path('usrreg',usrregister),
    path('login',login),
    path('userhome',userhome),
    path('emphome',emphome,name="emphome"),
    path('quattion',quattion),
    path('update_emp/<int:pk>',update_emp),
    path('update_usr/<int:pk>',update_usr),
    path('feed_backs',feed_backs),
    # path('generate_pdf',generate_pdf),
    path('logout',logout_view),
    path('selectemp/<int:id>/',selectemp),
    path('mytender',mytender),
    path('recived_tender',recived_tender)

]