from odoo.addons.helpdesk_mgmt.tests import test_helpdesk_ticket


class TestHelpdeskCustomerPriority(test_helpdesk_ticket.TestHelpdeskTicket):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        Ticket = cls.env["helpdesk.ticket"]
        Team = cls.env["helpdesk.ticket.team"]
        CustomerPriority = cls.env["helpdesk.ticket.customer_priority"]

        cls.ht_team1 = Team.create({"name": "Team 1", "user_ids": [(4, cls.user.id)]})
        cls.ht_customer_priority1 = CustomerPriority(
            {"name": "Customer Priority 1", "team_ids": [(4, cls.ht_team1.id)]}
        )
        cls.ht_customer_priority2 = CustomerPriority({"name": "Customer Priority 2"})
        cls.ht_ticket1 = Ticket.create(
            {"name": "Test 1", "description": "Ticket test 1"}
        )

    def test_helpdesk_onchange_customer_priority_id(self):
        self.ht_ticket1.write({"team_id": self.ht_team1.id, "user_id": self.user.id})

        self.ht_ticket1.customer_priority_id = self.ht_customer_priority1
        self.ht_ticket1._onchange_customer_priority_id()
        self.assertEqual(
            self.ht_ticket1.team_id,
            self.ht_team1,
            "Helpdesk Ticket: when customer_priority is changed, ticket team should be unchanged"
            " if current team belongs to the new customer_priority",
        )
        self.assertEqual(
            self.ht_ticket1.user_id,
            self.user,
            "Helpdesk Ticket: when customer_priority is changed, ticket user should be unchanged"
            " if user belongs to a that belongs to the new customer_priority",
        )

        self.ht_ticket1.customer_priority_id = self.ht_customer_priority2
        self.ht_ticket1._onchange_customer_priority_id()
        self.assertFalse(
            self.ht_ticket1.team_id,
            "Helpdesk Ticket: When customer_priority is changed, ticket team should be reset if"
            " current team does not belong to the new customer_priority",
        )
        self.assertFalse(
            self.ht_ticket1.user_id,
            "Helpdesk Ticket: When customer_priority is changed, ticket user should be reset if"
            " current user does not belong to a team assigned to the new customer_priority",
        )
