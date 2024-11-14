# Estrutura inicial do módulo helpdesk_custom_sla
# Diretório: helpdesk_custom_sla

# __manifest__.py
{
    "name": "Helpdesk Custom SLA",
    "summary": "Adds SLA management functionality to the OCA helpdesk module.",
    "version": "16.0.1.0.0",
    "author": "KMEE",
    "website": "https://kmee.com.br",
    "license": "AGPL-3",
    "depends": ["helpdesk_mgmt"],
    "data": [
    "security/ir.model.access.csv",
    "views/helpdesk_sla_views.xml",
    "views/helpdesk_ticket_views.xml",
    ],

    "installable": True,
    "application": False,
    "auto_install": False
}