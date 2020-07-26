from django.urls import path, include

from apis import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('todos', views.TodoViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
