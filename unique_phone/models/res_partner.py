from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = "res.partner"

    def _check_unique_phone(self, context=None):
        if not context:
            context = {}
        partner_ids = []
        if self.phone:
            partner_ids = self.search([("phone", "=", self.phone)])
        if len(partner_ids) > 1:
            return False
        return True

    _constraints = [
        (
            _check_unique_phone,
            (
                """There is a similar phone number already in the system,
                Please specify another phone, Phone numbers must be UNIQUE!"""
            ),
            ["phone"],
        ),
    ]
