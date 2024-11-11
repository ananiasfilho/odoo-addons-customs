# Copyright (C) 2024 KMEE
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import fields, models


class HelpdeskTeam(models.Model):
    _inherit = "helpdesk.ticket.team"

    request_complexity_ids = fields.Many2many(
        "helpdesk.ticket.request_complexity",
        string="Ticket Request Complexity",
        help="Ticket Request Complexity the team will use. This team's tickets will only "
        "be able to use those Request Complexity.",
    )
