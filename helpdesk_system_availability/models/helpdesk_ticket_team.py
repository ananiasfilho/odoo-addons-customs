# Copyright (C) 2024 KMEE
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import fields, models


class HelpdeskTeam(models.Model):
    _inherit = "helpdesk.ticket.team"

    system_availability_ids = fields.Many2many(
        "helpdesk.ticket.system_availability",
        string="Ticket System Availability",
        help="Ticket System Availability the team will use. This team's tickets will only "
        "be able to use those System Availability.",
    )
