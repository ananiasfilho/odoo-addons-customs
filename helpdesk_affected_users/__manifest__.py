{
    'name': 'Helpdesk Affected Users',
    'version': '16.0.1.0.0',
    'depends': ['helpdesk_mgmt'],
    'author': 'KMEE',
    'category': 'Helpdesk',
    'description': 'Adiciona o campo Affected Users ao módulo de Helpdesk para registrar o número de usuários afetados.',
    'data': [
        'security/ir.model.access.csv',
        'views/helpdesk_ticket_views.xml',
    ],
    'installable': True,
    'application': False,
}
