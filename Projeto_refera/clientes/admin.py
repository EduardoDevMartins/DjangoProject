from django.contrib import admin
from .models import Status, Cliente, Resultado


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'Chamado', 'Data_atrelamento', 'Ativo', 'Descricao')
    list_display_links = 'id', 'Chamado'
    list_per_page = 10
    search_fields = ('Chamado','Data_atrelamento')
    list_editable = ('Data_atrelamento', 'Ativo', 'Descricao')
    


admin.site.register(Status)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Resultado)
