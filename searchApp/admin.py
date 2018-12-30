from django.contrib import admin
from .models import Country,Course,Institute,Discipline


class BaseAdmin(admin.ModelAdmin):
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}


class InstituteInline(admin.StackedInline):
    model = Institute


class CourseInline(admin.StackedInline):
    model = Course


@admin.register(Country)
class CountryAdmin(BaseAdmin):
    list_display = ['name', 'slug']
    list_editable = ['slug']
    inlines = [InstituteInline]


@admin.register(Institute)
class InstituteAdmin(BaseAdmin):
    list_display = ['name', 'country', 'is_university']
    list_editable = ['country', 'is_university']
    list_filter = ['country', 'is_university']
    inlines = [CourseInline]


@admin.register(Course)
class CourseAdmin(BaseAdmin):
    list_display = ['name', 'location', 'level', 'fee_level', 'institute', 'intake_months']
    list_editable = ['location', 'level', 'fee_level', 'intake_months']
    list_filter = ['level', 'fee_level', 'discipline']


@admin.register(Discipline)
class DisciplineAdmin(BaseAdmin):
    list_display = ['name', 'slug']
    list_editable = ['slug']