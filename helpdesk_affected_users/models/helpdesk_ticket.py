from odoo import models, fields

class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    affected_users = fields.Integer(string="Affected Users")
