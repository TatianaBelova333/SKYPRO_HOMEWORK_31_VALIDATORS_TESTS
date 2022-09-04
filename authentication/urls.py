from django.urls import path

from authentication import views as user_view
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('', user_view.UserListView.as_view()),
    path('<int:pk>/', user_view.UserDetailView.as_view()),
    path('create/', user_view.UserCreateView.as_view()),
    path('<int:pk>/update/', user_view.UserUpdateView.as_view()),
    path('<int:pk>/delete/', user_view.UserDeleteView.as_view()),
    path('login/', views.obtain_auth_token),
    path('logout/', user_view.Logout.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]