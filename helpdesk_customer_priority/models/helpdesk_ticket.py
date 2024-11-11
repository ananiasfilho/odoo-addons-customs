# Copyright (C) 2024 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, fields, models


class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    customer_priority_id = fields.Many2one("helpdesk.ticket.customer_priority", string="Customer Priority")

    @api.onchange("customer_priority_id")
    def _onchange_customer_priority_id(self):
        if self.customer_priority_id and self.team_id and self.customer_priority_id not in self.team_id.customer_priority_ids:
            self.team_id = False
            self.user_id = False
