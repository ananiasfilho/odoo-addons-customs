from odoo import models, fields, api
from datetime import timedelta

class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    sla_id = fields.Many2one(
        comodel_name="helpdesk.sla",
        string="SLA",
        help="SLA associado a este ticket."
    )
    time_to_response = fields.Char(
        string="Time to Respond",
        compute="_compute_sla_times",
        help="Tempo restante para responder com base no SLA."
    )
    time_to_resolution = fields.Char(
        string="Time to Resolve",
        compute="_compute_sla_times",
        help="Tempo restante para resolver com base no SLA."
    )
    sla_state = fields.Selection(
        selection=[
            ('on_time', "No Prazo"),
            ('attention', "Atenção"),
            ('expiring', "Expirando"),
            ('expired', "Expirado")
        ],
        string="SLA State",
        compute="_compute_sla_state",
        store=False,
        help="Estado atual do SLA com base nos thresholds."
    )

    @api.depends("create_date", "sla_id")
    def _compute_sla_times(self):
        for ticket in self:
            if ticket.sla_id and ticket.create_date:
                now = fields.Datetime.now()
                response_deadline = ticket.create_date + timedelta(hours=ticket.sla_id.response_time)
                resolution_deadline = ticket.create_date + timedelta(hours=ticket.sla_id.resolution_time)

                def format_time(delta):
                    days = delta.days
                    hours, remainder = divmod(delta.seconds, 3600)
                    minutes = remainder // 60
                    return f"{days}d {hours}h {minutes:02}m"

                response_diff = response_deadline - now
                resolution_diff = resolution_deadline - now

                ticket.time_to_response = (
                    format_time(response_diff) if response_diff.total_seconds() > 0 else "Expired"
                )
                ticket.time_to_resolution = (
                    format_time(resolution_diff) if resolution_diff.total_seconds() > 0 else "Expired"
                )
            else:
                ticket.time_to_response = "N/A"
                ticket.time_to_resolution = "N/A"

    @api.depends("create_date", "sla_id")
    def _compute_sla_state(self):
        for ticket in self:
            if ticket.sla_id and ticket.create_date:
                now = fields.Datetime.now()
                resolution_deadline = ticket.create_date + timedelta(hours=ticket.sla_id.resolution_time)
                total_time = (resolution_deadline - ticket.create_date).total_seconds()

                if total_time <= 0:
                    ticket.sla_state = 'expired'
                    continue

                remaining_time = (resolution_deadline - now).total_seconds()
                attention_time = total_time * (ticket.sla_id.attention_threshold / 100.0)
                expiring_time = total_time * (ticket.sla_id.expiring_threshold / 100.0)

                if remaining_time > attention_time:
                    ticket.sla_state = 'on_time'
                elif remaining_time > expiring_time:
                    ticket.sla_state = 'attention'
                elif remaining_time > 0:
                    ticket.sla_state = 'expiring'
                else:
                    ticket.sla_state = 'expired'
            else:
                ticket.sla_state = 'expired'