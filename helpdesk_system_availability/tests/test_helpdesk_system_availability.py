from odoo.addons.helpdesk_mgmt.tests import test_helpdesk_ticket


class TestHelpdeskSystemAvailability(test_helpdesk_ticket.TestHelpdeskTicket):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        Ticket = cls.env["helpdesk.ticket"]
        Team = cls.env["helpdesk.ticket.team"]
        SystemAvailability = cls.env["helpdesk.ticket.system_availability"]

        cls.ht_team1 = Team.create({"name": "Team 1", "user_ids": [(4, cls.user.id)]})
        cls.ht_system_availability1 = SystemAvailability(
            {"name": "System Availability 1", "team_ids": [(4, cls.ht_team1.id)]}
        )
        cls.ht_system_availability2 = SystemAvailability({"name": "System Availability 2"})
        cls.ht_ticket1 = Ticket.create(
            {"name": "Test 1", "description": "Ticket test 1"}
        )

    def test_helpdesk_onchange_system_availability_id(self):
        self.ht_ticket1.write({"team_id": self.ht_team1.id, "user_id": self.user.id})

        self.ht_ticket1.system_availability_id = self.ht_system_availability1
        self.ht_ticket1._onchange_system_availability_id()
        self.assertEqual(
            self.ht_ticket1.team_id,
            self.ht_team1,
            "Helpdesk Ticket: when system availability is changed, ticket team should be unchanged"
            " if current team belongs to the new system availability",
        )
        self.assertEqual(
            self.ht_ticket1.user_id,
            self.user,
            "Helpdesk Ticket: when system availability is changed, ticket user should be unchanged"
            " if user belongs to a that belongs to the new system availability",
        )

        self.ht_ticket1.system_availability_id = self.ht_system_availability2
        self.ht_ticket1._onchange_system_availability_id()
        self.assertFalse(
            self.ht_ticket1.team_id,
            "Helpdesk Ticket: When system availability is changed, ticket team should be reset if"
            " current team does not belong to the new system availability",
        )
        self.assertFalse(
            self.ht_ticket1.user_id,
            "Helpdesk Ticket: When system availability is changed, ticket user should be reset if"
            " current user does not belong to a team assigned to the new system availability",
        )
