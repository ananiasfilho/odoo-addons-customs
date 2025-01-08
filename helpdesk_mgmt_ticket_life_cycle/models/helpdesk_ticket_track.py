
from odoo import models, fields, api
from datetime import datetime

class HelpdeskTicketTrack(models.Model):
    _inherit = 'helpdesk.ticket'

    stage_duration_ids = fields.One2many('helpdesk.ticket.stage.duration', 'ticket_id', string="Stage Durations")

    @api.model
    def create(self, vals):
        ticket = super(HelpdeskTicketTrack, self).create(vals)
        if ticket.stage_id:
            ticket.stage_duration_ids.create({
                'ticket_id': ticket.id,
                'stage_id': ticket.stage_id.id,
                'start_date': fields.Datetime.now()
            })
        return ticket

    def write(self, vals):
        res = super(HelpdeskTicketTrack, self).write(vals)
        if 'stage_id' in vals:
            for ticket in self:
                previous_stage = ticket.stage_duration_ids.filtered(lambda s: not s.end_date)
                if previous_stage:
                    previous_stage.end_date = fields.Datetime.now()
                ticket.stage_duration_ids.create({
                    'ticket_id': ticket.id,
                    'stage_id': vals['stage_id'],
                    'start_date': fields.Datetime.now()
                })
        return res

class HelpdeskTicketTrackStageDuration(models.Model):
    _name = 'helpdesk.ticket.stage.duration'
    _description = 'ticket Stage Duration'

    ticket_id = fields.Many2one('helpdesk.ticket', string="ticket", required=True, ondelete='cascade')
    stage_id = fields.Many2one('helpdesk.ticket.stage', string="Stage", required=True)
    start_date = fields.Datetime(string="Start Date", required=True)
    end_date = fields.Datetime(string="End Date")

    duration_display = fields.Char(string="Duration", compute='_compute_duration_display', store=True)

    @api.depends('start_date', 'end_date')
    def _compute_duration_display(self):
        for record in self:
            if record.start_date and record.end_date:
                duration = record.end_date - record.start_date
                days = duration.days
                hours, remainder = divmod(duration.seconds, 3600)
                minutes, _ = divmod(remainder, 60)
                record.duration_display = f"{days} dias e {hours}:{minutes:02d} horas"
            else:
                record.duration_display = "0 dias e 0:00 horas"
