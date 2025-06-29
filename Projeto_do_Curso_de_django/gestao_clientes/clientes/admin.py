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
    list_filter = ('age', 'salary')
    list_display = ('first_name', 'doc', 'last_name', 'age', 'salary', 'bio', 'tem_foto')

    def tem_foto(self, obj):
        if obj.photo:
            return 'Sim'
        else:
            return 'Não'
        
    tem_foto.short_description = 'Possui foto'

class VendaAdmin(admin.ModelAdmin):
    readonly_fields = ('valor',)
    raw_id_fields = ('pessoa',)
    list_filter = ('pessoa__doc', 'desconto')
    list_display = ('id', 'pessoa', 'get_total')
    search_fields = ('id', 'pessoa__first_name', 'pessoa__doc__num_doc')

    def total(self, obj):
        return obj.get_total()
    
    total.short_description = 'Total'

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'preco')

admin.site.register(Person, PersonAdmin)
admin.site.register(Documento)
admin.site.register(Venda, VendaAdmin)
admin.site.register(Produto, ProdutoAdmin)
