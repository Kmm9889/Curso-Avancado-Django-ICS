from django.contrib import admin
from .models import Venda
from .models import ItensDoPedido
from .actions import nfe_emitida, nfe_nao_emitida


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


admin.site.register(Venda, VendaAdmin)
admin.site.register(ItensDoPedido)
