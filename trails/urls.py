from django.urls import path
from .views import (
    TrailListCreateView,
    TrailDetailView,
    NearbyTrailsView,
    TrailImageUploadView,
    TrailReviewListCreateView,
    TrailConditionListCreateView
)

urlpatterns = [
    path('', TrailListCreateView.as_view(), name='trail-list-create'),
    path('<int:pk>/', TrailDetailView.as_view(), name='trail-detail'),
    path('nearby/', NearbyTrailsView.as_view(), name='nearby-trails'),
    path('images/upload/', TrailImageUploadView.as_view(), name='trail-image-upload'),
    path('<int:trail_id>/reviews/', TrailReviewListCreateView.as_view(), name='trail-reviews'),
    path('<int:trail_id>/conditions/', TrailConditionListCreateView.as_view(), name='trail-conditions'),
]