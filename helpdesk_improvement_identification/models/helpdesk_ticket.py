from odoo import models, fields

class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    improvement_identification = fields.Html(string="Improvement Identification", sanitize=True)
