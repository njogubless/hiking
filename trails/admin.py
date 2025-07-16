from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Trail, TrailImage, TrailReview, TrailCondition

@admin.register(Trail)
class TrailAdmin(OSMGeoAdmin):
    list_display = ('name', 'difficulty', 'length', 'elevation_gain', 'location', 'is_active', 'created_at')
    list_filter = ('difficulty', 'is_loop', 'is_active', 'created_at')
    search_fields = ('name', 'description', 'location')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description', 'difficulty', 'location')
        }),
        ('Trail Details', {
            'fields': ('length', 'elevation_gain', 'estimated_time', 'is_loop', 'is_active')
        }),
        ('Geographic Data', {
            'fields': ('start_point', 'end_point', 'trail_path')
        }),
        ('Metadata', {
            'fields': ('created_by', 'created_at', 'updated_at')
        }),
    )

@admin.register(TrailImage)
class TrailImageAdmin(admin.ModelAdmin):
    list_display = ('trail', 'caption', 'is_primary', 'uploaded_by', 'created_at')
    list_filter = ('is_primary', 'created_at')
    search_fields = ('trail__name', 'caption')

@admin.register(TrailReview)
class TrailReviewAdmin(admin.ModelAdmin):
    list_display = ('trail', 'user', 'rating', 'is_approved', 'created_at')
    list_filter = ('rating', 'is_approved', 'created_at')
    search_fields = ('trail__name', 'user__email', 'comment')
    actions = ['approve_reviews', 'disapprove_reviews']
    
    def approve_reviews(self, request, queryset):
        queryset.update(is_approved=True)
    approve_reviews.short_description = "Approve selected reviews"
    
    def disapprove_reviews(self, request, queryset):
        queryset.update(is_approved=False)
    disapprove_reviews.short_description = "Disapprove selected reviews"

@admin.register(TrailCondition)
class TrailConditionAdmin(admin.ModelAdmin):
    list_display = ('trail', 'condition', 'reported_by', 'created_at')
    list_filter = ('condition', 'created_at')
    search_fields = ('trail__name', 'description', 'reported_by__email')