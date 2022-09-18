
from django.urls import path
from .views import index,   SearchResultsListView,register, review_rating,signin,productview


urlpatterns = [
    path('',index, name="index"),
 
    path('register/',register, name="register"),
    path('review/<int:myid>',review_rating, name="review"),
    path('productview/<int:myid>', productview , name='productview/<int:myid>'),
    # path('<int:pk>/checkout/', BookCheckoutView.as_view(), name = 'checkout'),
    # path('complete/', paymentComplete, name = 'complete'),
    path('search/', SearchResultsListView.as_view(), name = 'search_results'),
    path('signin/', signin, name='signin'),
]