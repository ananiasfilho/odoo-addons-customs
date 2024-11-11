from odoo import models, fields

class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    root_details = fields.Html(string="Root Details", sanitize=True)
