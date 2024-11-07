import odoo.http as http
from odoo.http import request
from odoo.addons.helpdesk_mgmt.controllers.main import HelpdeskTicketController

class HelpdeskTicketController(HelpdeskTicketController):
    # Ajuste a rota para corresponder à URL correta do portal
    @http.route("/ticket/new", type="http", auth="user", website=True)
    def portal_create_ticket(self, **kw):
        # Obtém as opções de disponibilidade de sistema
        system_availabilitys = request.env['helpdesk.ticket.system_availability'].sudo().search([])

        # Renderiza o formulário do portal com as opções
        return request.render("helpdesk_mgmt.portal_create_ticket", {
            'system_availabilitys': system_availabilitys,
        })

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
