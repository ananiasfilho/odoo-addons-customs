import logging
import odoo.http as http
from odoo.http import request
from odoo.addons.helpdesk_mgmt.controllers.main import HelpdeskTicketController

_logger = logging.getLogger(__name__)

class HelpdeskTicketController(HelpdeskTicketController):
    @http.route("/new/ticket", type="http", auth="user", website=True)
    def create_new_ticket(self, **kw):
        session_info = request.env["ir.http"].session_info()
        company = request.env.company
        categories = request.env["helpdesk.ticket.category"].with_company(company.id).search([("active", "=", True)])
        
        # Obtenha todas as opções necessárias para o formulário do portal
        customer_priorities = request.env['helpdesk.ticket.customer_priority'].sudo().search([])
        system_availabilitys = request.env['helpdesk.ticket.system_availability'].sudo().search([])
        ticket_types = request.env['helpdesk.ticket.type'].sudo().search([])
        products = request.env['product.product'].sudo().search([])
        affected_users = request.env['res.users'].sudo().search([])

        # Projetos que o usuário está seguindo
        user_id = request.env.user.partner_id.id
        followed_projects = request.env['project.project'].sudo().search([('message_follower_ids.partner_id', '=', user_id)])

        return request.render(
            "helpdesk_mgmt.portal_create_ticket",
            {
                "categories": categories,
                "teams": self._get_teams(),
                "email": request.env.user.email,
                "name": request.env.user.name,
                "ticket_team_id_required": company.helpdesk_mgmt_portal_team_id_required,
                "ticket_category_id_required": company.helpdesk_mgmt_portal_category_id_required,
                "max_upload_size": session_info["max_file_upload_size"],
                "customer_priorities": customer_priorities,
                "system_availabilitys": system_availabilitys,
                "ticket_types": ticket_types,
                "products": products,
                "affected_users": affected_users,
                "followed_projects": followed_projects,
            },
        )

    @http.route("/submitted/ticket", type="http", auth="user", website=True, csrf=True)
    def submit_ticket(self, **kw):
        _logger.info("Submitted values: %s", kw)  # Log dos valores submetidos para depuração
        res = super(HelpdeskTicketController, self).submit_ticket(**kw)
        ticket_id = res.location.split("/")[-1]
        new_ticket = request.env["helpdesk.ticket"].browse(int(ticket_id))

        # Coleta de todos os valores dos campos do formulário
        values = {}
        if kw.get("customer_priority"):
            values["customer_priority_id"] = int(kw.get("customer_priority", 0))

        if kw.get("system_availability"):
            values["system_availability_id"] = int(kw.get("system_availability", 0))

        if kw.get("type"):
            values["type_id"] = int(kw.get("type", 0))

        if kw.get("product"):
            values["product_id"] = int(kw.get("product", 0))

        if kw.get("affected_users"):
            values["affected_users"] = kw.get("affected_users")

        if kw.get("project_id"):
            values["project_id"] = int(kw.get("project_id", 0))

        _logger.info("Values to write on ticket: %s", values)  # Log para verificar os valores de gravação

        # Grava todos os valores no ticket em uma única chamada
        new_ticket.sudo().write(values)

        return res
