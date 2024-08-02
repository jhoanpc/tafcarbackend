from rest_framework import routers
from .api import PersonViewSet, DetailsPersonViewSet, DetailsEconomicActivityViewSet
from .views import PersonView
#from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
router = routers.DefaultRouter()

router.register('api/people', PersonViewSet,basename='people')
router.register('api/details', DetailsPersonViewSet,basename='details')
router.register('api/activity', DetailsEconomicActivityViewSet,basename='activity')

urlpatterns = router.urls

"""urlpatterns = [
    path('people', PersonView.as_view())
]"""

#urlpatterns = format_suffix_patterns(urlpatterns)

