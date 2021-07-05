from django.urls import path
from base.views.user_views import MyTokenObtainPairView, registerUser, getuserProfile, getUsers, updateUserProfile
 



urlpatterns = [
    path('register/', registerUser, name='register'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('profile/', getuserProfile, name="user-profile"),
    path('profile/update/', updateUserProfile, name='user-profile-update'),
    path('', getUsers, name="users"),
]


