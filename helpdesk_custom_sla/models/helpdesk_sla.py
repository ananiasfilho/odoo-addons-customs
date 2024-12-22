from odoo import models, fields

class HelpdeskSLA(models.Model):
    _name = "helpdesk.sla"
    _description = "Helpdesk SLA"

    name = fields.Char(string="Name", required=True)
    response_time = fields.Float(string="Response Time (hours)")
    resolution_time = fields.Float(string="Resolution Time (hours)")
    attention_threshold = fields.Float(
        string="Attention Threshold (%)",
        default=50,
        help="Percentage of SLA time when attention status is triggered."
    )
    expiring_threshold = fields.Float(
        string="Expiring Threshold (%)",
        default=20,
        help="Percentage of SLA time when expiring status is triggered."
    )
    active = fields.Boolean(default=True)
