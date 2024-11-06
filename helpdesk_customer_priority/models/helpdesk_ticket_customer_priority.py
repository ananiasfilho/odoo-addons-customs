# Copyright (C) 2024 KMEE
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import fields, models


class HelpdeskCustomerpriority(models.Model):
    """Helpdesk Customer Priority"""

    _name = "helpdesk.ticket.customer_priority"
    _description = "Helpdesk Ticket Customer Priority"
    _order = "name asc"

    name = fields.Char(required=True)
    team_ids = fields.Many2many(
        "helpdesk.ticket.team",
        string="Teams",
        help="Helpdesk teams allowed to use this customer priority.",
    )
