from django.shortcuts import render
from django.views import View
from django.db.models import Sum, F, FloatField, Max, Avg, Min, Count
from .models import Venda

class DashboardView(View):
    def get(self, request):
        data = {}
        data['media'] = Venda.objects.all().aggregate(Avg('valor'))['valor__avg']
        data['media_desc'] = Venda.objects.all().aggregate(Avg('desconto'))['desconto__avg']
        data['max'] = Venda.objects.all().aggregate(Max('valor'))['valor__max']
        data['min'] = Venda.objects.all().aggregate(Min('valor'))['valor__min']
        data['n_ped'] = Venda.objects.all().aggregate(Count('id'))['id__count']
        data['n_ped_nfe'] = Venda.objects.filter(
            nfe_emitida=True
        ).aggregate(Count('id'))['id__count']

        return render(request, 'vendas/dashboard.html', data)