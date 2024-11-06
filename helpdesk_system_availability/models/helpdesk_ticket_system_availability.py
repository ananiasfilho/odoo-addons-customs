# Copyright (C) 2024 KMEE
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import fields, models


class HelpdeskSystemavailability(models.Model):
    """Helpdesk System Availability"""

    _name = "helpdesk.ticket.system_availability"
    _description = "Helpdesk Ticket System Availability"
    _order = "name asc"

    name = fields.Char(required=True)
    team_ids = fields.Many2many(
        "helpdesk.ticket.team",
        string="Teams",
        help="Helpdesk teams allowed to use this system availability.",
    )
