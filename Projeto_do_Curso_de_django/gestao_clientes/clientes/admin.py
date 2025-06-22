from django.contrib import admin
from .models import Person, Documento, Venda, Produto

class PersonAdmin(admin.ModelAdmin):
    fieldsets = (
    ('Dados pessoais', {'fields': ('first_name', 'last_name', 'doc')}),
    ('Dados complementares', {
        'classes': ('collapse',),
        'fields': ('age', 'salary', 'photo')
        }),
    )
    #fields = (('doc', 'first_name'), 'last_name', ('age', 'salary'), 'bio', 'photo')
    #exclude = ('bio',) 
    list_display = ('first_name', 'doc', 'last_name', 'age', 'salary', 'bio', 'photo')

admin.site.register(Person, PersonAdmin)
admin.site.register(Documento)
admin.site.register(Venda)
admin.site.register(Produto)
