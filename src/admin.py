"""
Admin module for the app src
"""

from ginger.contrib import admin

from .models import *

# admin.site.register(Test)
admin.site.register(TestAppModel1)
admin.site.register(Many2ManyTest)


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('char_field', 'choice_field', 'bool_field', 'positive_integer_field', 'field3')
    list_filter = ('choice_field', 'bool_field', 'field3')
    search_fields = ('char_field',)
    ordering = ('char_field',)
    fieldsets = (
        (None, {
            'fields': ('char_field', 'choice_field', 'bool_field', 'positive_integer_field', 'field3')
        }),
    )
