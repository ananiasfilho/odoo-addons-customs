# Copyright (C) 2024 KMEE
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import fields, models


class HelpdeskRequestcomplexity(models.Model):
    """Helpdesk Request Complexity"""

    _name = "helpdesk.ticket.request_complexity"
    _description = "Helpdesk Ticket Request Complexity"
    _order = "name asc"

    name = fields.Char(required=True)
    team_ids = fields.Many2many(
        "helpdesk.ticket.team",
        string="Teams",
        help="Helpdesk teams allowed to use this request.complexity.",
    )
