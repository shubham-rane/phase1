from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('creditmgmt/viewusers', views.viewusers, name="homepage"),
	path('creditmgmt/transfer',views.transfer, name="transfer"),
	path('creditmgmt/update',views.update, name="update"),
	path('creditmgmt/adduser',views.adduser,name="adduser")

]
