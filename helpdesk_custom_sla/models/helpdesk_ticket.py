from odoo import models, fields, api
from datetime import timedelta

class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    sla_id = fields.Many2one(
        comodel_name="helpdesk.sla",
        string="SLA",
        help="SLA associated with this ticket."
    )
    time_to_response = fields.Char(
        string="Time to Respond",
        compute="_compute_sla_times",
        help="Time remaining to respond based on SLA."
    )
    time_to_resolution = fields.Char(
        string="Time to Resolve",
        compute="_compute_sla_times",
        help="Time remaining to resolve based on SLA."
    )


    created_on_formatted = fields.Char(
        string="Created On",
        compute="_compute_formatted_date",
        store=True,
        help="Formatted creation date in MM/DD/YYYY format."
    )

    @api.depends("create_date")
    def _compute_formatted_date(self):
        for ticket in self:
            if ticket.create_date:
                ticket.created_on_formatted = ticket.create_date.strftime("%m/%d/%Y")
            else:
                ticket.created_on_formatted = "N/A"

    @api.depends("create_date", "sla_id")
    def _compute_sla_times(self):
        for ticket in self:
            if ticket.sla_id and ticket.create_date:
                now = fields.Datetime.now()
                response_deadline = ticket.create_date + timedelta(hours=ticket.sla_id.response_time)
                resolution_deadline = ticket.create_date + timedelta(hours=ticket.sla_id.resolution_time)

                response_diff = response_deadline - now
                resolution_diff = resolution_deadline - now

                def format_time(delta):
                    days = delta.days
                    hours, remainder = divmod(delta.seconds, 3600)
                    minutes = remainder // 60
                    return f"{days}d {hours}h {minutes:02}m"

                ticket.time_to_response = (
                    format_time(response_diff) if response_diff.total_seconds() > 0 else "Expired"
                )
                ticket.time_to_resolution = (
                    format_time(resolution_diff) if resolution_diff.total_seconds() > 0 else "Expired"
                )
            else:
                ticket.time_to_response = "N/A"
                ticket.time_to_resolution = "N/A"
