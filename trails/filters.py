import django_filters
from django_filters import rest_framework as filters
from .models import Trail

class TrailFilter(filters.FilterSet):
    difficulty = filters.MultipleChoiceFilter(
        choices=Trail.DIFFICULTY_CHOICES,
        field_name='difficulty',
        lookup_expr='in'
    )
    min_length = filters.NumberFilter(field_name='length', lookup_expr='gte')
    max_length = filters.NumberFilter(field_name='length', lookup_expr='lte')
    min_elevation = filters.NumberFilter(field_name='elevation_gain', lookup_expr='gte')
    max_elevation = filters.NumberFilter(field_name='elevation_gain', lookup_expr='lte')
    is_loop = filters.BooleanFilter(field_name='is_loop')
    location = filters.CharFilter(field_name='location', lookup_expr='icontains')
    
    class Meta:
        model = Trail
        fields = ['difficulty', 'is_loop', 'location']