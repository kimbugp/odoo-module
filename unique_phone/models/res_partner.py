from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.constrains("phone")
    def _check_unique_phone(self):
        for record in self:
            partner_ids = self.search([("phone", "=", record.phone)])
            if len(partner_ids) > 1:
                raise ValidationError("A record with this phone already exists: %s" % record.phone)