# Copyright (C) 2024 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Helpdesk Ticket System Availability",
    "version": "16.0.1.1.0",
    "license": "AGPL-3",
    "summary": "Add a system availability to your tickets",
    "author": "KMEE, " "Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/helpdesk",
    "depends": ["helpdesk_mgmt"],
    "data": [
        "security/ir.model.access.csv",
        "views/helpdesk_ticket_system_availability.xml",
        "views/helpdesk_ticket_team.xml",
        "views/helpdesk_ticket.xml",
	"views/helpdesk_ticket_portal_form.xml",
	"views/helpdesk_templates.xml",
	#"views/helpdesk_templates_view.xml",
    ],
    "application": False,
    "development_status": "Beta",
    "maintainers": ["ananiasfilho"],
}
