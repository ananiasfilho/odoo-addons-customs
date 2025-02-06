{
    'name': 'Rework Management',
    'version': '1.0',
    'summary': 'Manage rework tasks within activities',
    'description': 'Module to register activities and manage rework tasks.',
    'license': 'AGPL-3',
    'author': 'Ananias Filho',
    'depends': ['helpdesk_mgmt_timesheet'],
    'data': [
        'security/ir.model.access.csv',
        'views/helpdesk_ticket_views.xml',
    ],
    'installable': True,
    'application': False,
}
