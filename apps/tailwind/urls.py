from django.urls import path
from .views import (
    tailwind_detail_view
)

app_name = 'apps.tailwind'

urlpatterns = [
    path('', tailwind_detail_view, name='home'),


]

# 1:32:00