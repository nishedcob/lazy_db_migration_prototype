
from rest_framework.routers import DefaultRouter

from data.views import ThingViewSet, SubThingViewSet, UnrelatedThingViewSet

router = DefaultRouter()
router.register(r'things', ThingViewSet, basename='thing')
router.register(r'subthings', SubThingViewSet, basename='subthing')
router.register(r'unrelated_things', UnrelatedThingViewSet, basename='unrelated_thing')
urlpatterns = router.urls
