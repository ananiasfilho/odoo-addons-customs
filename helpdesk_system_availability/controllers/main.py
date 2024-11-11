import logging
import odoo.http as http
from odoo.http import request
from odoo.addons.helpdesk_mgmt.controllers.main import HelpdeskTicketController

#_logger = logging.getLogger(__name__)
class HelpdeskTicketController(HelpdeskTicketController):
    @http.route("/new/ticket", type="http", auth="user", website=True)
    def create_new_ticket(self, **kw):
        session_info = http.request.env["ir.http"].session_info()
        company = request.env.company
        category_model = http.request.env["helpdesk.ticket.category"]
        categories = category_model.with_company(company.id).search(
            [("active", "=", True)]
        )
        email = http.request.env.user.email
        name = http.request.env.user.name
        company = request.env.company
        
        system_availabilitys = request.env['helpdesk.ticket.system_availability'].sudo().search([])

        
        return http.request.render(
            "helpdesk_mgmt.portal_create_ticket",
            {
                "categories": categories,
                "teams": self._get_teams(),
                "email": email,
                "name": name,
                "ticket_team_id_required": (
                    company.helpdesk_mgmt_portal_team_id_required
                ),
                "ticket_category_id_required": (
                    company.helpdesk_mgmt_portal_category_id_required
                ),
                "max_upload_size": session_info["max_file_upload_size"],
                "system_availabilitys": system_availabilitys
            },
        )

    @http.route("/submitted/ticket", type="http", auth="user", website=True, csrf=True)
    def submit_ticket(self, **kw):
        res = super(HelpdeskTicketController, self).submit_ticket(**kw)
        ticket_id = res.location.split("/")[-1]
        new_ticket = request.env["helpdesk.ticket"].browse(int(ticket_id))

        if kw.get("system_availability"):
            new_ticket.sudo().write({
                "system_availability_id": int(kw.get("system_availability", 0)),
            })

        return res
