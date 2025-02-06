from odoo import models, fields, api
from datetime import datetime

class HelpdeskTicketRework(models.Model):
    _name = 'helpdesk.ticket.rework'
    _description = 'Helpdesk Ticket Rework'

    name = fields.Char(string='Rework type', required=True)
    description = fields.Html(string='Rework Description', required=True)
    create_date = fields.Datetime(
        string='Creation Date', 
        readonly=True,
        default=fields.Datetime.now
    )
    create_uid = fields.Many2one(
        'res.users',
        string='Created by',
        readonly=True,
        default=lambda self: self.env.user
    )
    write_date = fields.Datetime(string='Last Modified Date', readonly=True)


class AcccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    is_rework = fields.Boolean(string='Is rework?')
    rework_id = fields.Many2one(
        comodel_name='helpdesk.ticket.rework',
        string='Rework type'
    )

    @api.onchange('is_rework')
    def _onchange_is_rework(self):
        for record in self:
            if not record.is_rework:
                record.rework_id = False
