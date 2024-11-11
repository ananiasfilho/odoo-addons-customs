{
    'name': 'Helpdesk Solution Details (Treatment)',
    'version': '16.0.1.0.0',
    'depends': ['helpdesk_mgmt'],
    'author': 'KMEE',
    'license': 'AGPL-3',
    'category': 'Helpdesk',
    'description': 'Adiciona uma aba Solution Details (Treatment) para descrições das tratativas do ticket no helpdesk.',
    'data': [
	'security/ir.model.access.csv',
        'views/helpdesk_ticket_views.xml',
    ],
    'installable': True,
    'application': False,
}
