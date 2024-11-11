from odoo import models, fields

class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    solution_details = fields.Html(string="Solution Details (Treatment)", sanitize=True)
