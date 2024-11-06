# Copyright (C) 2024 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, fields, models


class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    system_availability_id = fields.Many2one("helpdesk.ticket.system_availability", string="System Availability")

    @api.onchange("system_availability_id")
    def _onchange_system_availability_id(self):
        if self.system_availability_id and self.team_id and self.system_availability_id not in self.team_id.system_availability_ids:
            self.team_id = False
            self.user_id = False
