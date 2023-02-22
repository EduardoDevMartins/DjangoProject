from django.contrib import admin
from .models import Compania, Cliente, origem


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'Nome', 'Data_voo',
                    'Telefone', 'Ticket_voo', 'Email', 'Ativo' )
    list_display_links = 'id', 'Nome'
    list_per_page = 10
    search_fields = ('Nome', 'Telefone', 'Ticket_voo')
    list_editable = ('Telefone', 'Ativo')
    


admin.site.register(Compania)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(origem)
