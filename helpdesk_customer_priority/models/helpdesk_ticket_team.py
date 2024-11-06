# Copyright (C) 2024 KMEE
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import fields, models


class HelpdeskTeam(models.Model):
    _inherit = "helpdesk.ticket.team"

    customer_priority_ids = fields.Many2many(
        "helpdesk.ticket.customer_priority",
        string="Ticket Customer Priority",
        help="Ticket Customer Priority the team will use. This team's tickets will only "
        "be able to use those Customer Priorities.",
    )
