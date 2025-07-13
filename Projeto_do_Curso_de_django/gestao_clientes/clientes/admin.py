from django.contrib import admin
from .models import Person, Documento, Venda
from .actions import nfe_emitida, nfe_nao_emitida
from .models import ItensDoPedido

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
    search_fields = ('id', 'first_name')
    autocomplete_fields = ['doc']

    def tem_foto(self, obj):
        if obj.photo:
            return 'Sim'
        else:
            return 'Não'
        
    tem_foto.short_description = 'Possui foto'

class VendaAdmin(admin.ModelAdmin):
    readonly_fields = ('valor',)
    autocomplete_fields = ('pessoa',)   #raw_id_fields = ('pessoa',)
    list_filter = ('pessoa__doc', 'desconto')
    list_display = ('id', 'pessoa', 'nfe_emitida')
    search_fields = ('id', 'pessoa__first_name', 'pessoa__doc__num_doc')
    actions = [nfe_emitida, nfe_nao_emitida]
    #filter_horizontal = ['produtos']

    def total(self, obj):
        return obj.get_total()
    
    total.short_description = 'Total'

class DocumentoAdmin(admin.ModelAdmin):
    search_fields = ['num_doc']

admin.site.register(Person, PersonAdmin)
admin.site.register(Documento, DocumentoAdmin)
admin.site.register(Venda, VendaAdmin)
admin.site.register(ItensDoPedido)
