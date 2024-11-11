{
    'name': 'Helpdesk Improvement Identification',
    'version': '16.0.1.0.0',
    'depends': ['helpdesk_mgmt'],
    'author': 'KMEE',
    'license': 'AGPL-3',
    'category': 'Helpdesk',
    'description': 'Adiciona uma aba Improvement Identification para descrições de melhorias.',
    'data': [
	'security/ir.model.access.csv',
        'views/helpdesk_ticket_views.xml',
    ],
    'installable': True,
    'application': False,
}
