# Copyright (C) 2024 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, fields, models


class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    request_complexity_id = fields.Many2one("helpdesk.ticket.request_complexity", string="Request Complexity")

    @api.onchange("request_complexity_id")
    def _onchange_request_complexity_id(self):
        if self.request_complexity_id and self.team_id and self.request_complexity_id not in self.team_id.request_complexity_ids:
            self.team_id = False
            self.user_id = False
