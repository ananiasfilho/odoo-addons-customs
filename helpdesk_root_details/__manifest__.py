{
    'name': 'Helpdesk Root Details',
    'version': '16.0.1.0.0',
    'depends': ['helpdesk_mgmt'],
    'author': 'Ananias Filho',
    'license': 'AGPL-3',
    'category': 'Helpdesk',
    'description': 'Adiciona uma aba Root Details para descrições de causa raiz no helpdesk.',
    'data': [
	'security/ir.model.access.csv',
        'views/helpdesk_ticket_views.xml',
    ],
    'installable': True,
    'application': False,
}
