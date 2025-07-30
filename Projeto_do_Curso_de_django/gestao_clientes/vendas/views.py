from django.shortcuts import render
from django.views import View
from .models import Venda

class DashboardView(View):
    def get(self, request):
        data = {}
        data['media'] = Venda.objects.media()
        data['media_desc'] = Venda.objects.media_desconto()
        data['min'] = Venda.objects.min()
        data['max'] = Venda.objects.max()
        data['n_ped'] = Venda.objects.num_pedidos()
        data['n_ped_nfe'] = Venda.objects.num_ped_nefe()

        return render(request, 'vendas/dashboard.html', data)