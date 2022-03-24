from django.contrib import admin
from .models import Gabriel, Skills, Profile, Portifolio


# admin profile controller
class ProfileInline(admin.TabularInline):  # Add inline Profile fields to main profile(social network and useful links)
    model = Profile
    extra = 1


@admin.register(Gabriel)
class GabrielAdmin(admin.ModelAdmin):
    inlines = [
        ProfileInline,
    ]


admin.site.register(Skills)
admin.site.register(Portifolio)

