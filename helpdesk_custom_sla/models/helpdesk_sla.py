from odoo import models, fields

class HelpdeskSLA(models.Model):
    _name = "helpdesk.sla"
    _description = "Helpdesk SLA"

    name = fields.Char(string="SLA Name", required=True)
    response_time = fields.Float(string="Response Time (Hours)", required=True, help="Maximum time to respond to a ticket.")
    resolution_time = fields.Float(string="Resolution Time (Hours)", required=True, help="Maximum time to resolve a ticket.")
    active = fields.Boolean(string="Active", default=True)