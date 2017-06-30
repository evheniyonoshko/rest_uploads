from django.conf.urls import url

from uploads.views import Logout
from uploads import views

from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    url(r'^api/uploads/$', views.UploadsList.as_view()),
    url(r'^api/uploads/(?P<key>[A-Z a-z 0-9]+)/$', views.UploadsDetail.as_view()),
    url(r'^api/users/$', views.UserList.as_view()),
    url(r'^api/users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns += [
    url(r'^api-token-auth/login/$', obtain_auth_token),
    url(r'^api-token-auth/logout/$', Logout.as_view()),
]

# urlpatterns += staticfiles_urlpatterns()
# urlpatterns = format_suffix_patterns(urlpatterns)
