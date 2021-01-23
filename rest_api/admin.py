from django.contrib import admin
from rest_api.models import Person, Training


# Register your models here.
class People(admin.ModelAdmin):
    list_display = ('id', 'name', 'document', 'birth')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20


admin.site.register(Person, People)


class Trainings(admin.ModelAdmin):
    list_display = ('id', 'training_code', 'description', 'level')
    list_display_links = ('id', 'training_code')
    search_fields = ('training_code',)


admin.site.register(Training, Trainings)

