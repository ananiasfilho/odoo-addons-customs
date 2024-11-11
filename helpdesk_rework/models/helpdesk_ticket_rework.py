from odoo import models, fields, api
from datetime import datetime

class HelpdeskTicketRework(models.Model):
    _name = 'helpdesk.ticket.rework'
    _description = 'Helpdesk Ticket Rework'

    description = fields.Html(string='Rework Description', required=True)
    ticket_id = fields.Many2one('helpdesk.ticket', string='Ticket', ondelete='cascade')
    create_date = fields.Datetime(string='Creation Date', readonly=True, default=fields.Datetime.now)
    create_uid = fields.Many2one('res.users', string='Created by', readonly=True, default=lambda self: self.env.user)
    write_date = fields.Datetime(string='Last Modified Date', readonly=True)

    @api.model
    def create(self, vals):
        # Define a data de criação e o usuário ao criar o registro
        vals['create_date'] = fields.Datetime.now()
        vals['create_uid'] = self.env.user.id
        return super(HelpdeskTicketRework, self).create(vals)

    def write(self, vals):
        # Atualiza write_date sempre que description é modificada
        if 'description' in vals:
            vals['write_date'] = fields.Datetime.now()
        return super(HelpdeskTicketRework, self).write(vals)

# Funcionq - porem, ao salvar o ticket inteiro, atualiza o write_date do rewirte edita.
#    @api.depends('description')
#    def _compute_audit_fields(self):
#        for record in self:
#            record.write_date = fields.Datetime.now()
#
#    write_date = fields.Datetime(string='Last Modified Date', compute="_compute_audit_fields", store=True)


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    rework_ids = fields.One2many('helpdesk.ticket.rework', 'ticket_id', string='Reworks')
