from openerp import models, fields, api


class CustomCustomer(models.Model):

    _inherit = "res.partner"
    total = fields.Integer(string="Total", compute="_compute_total")

    # _sql_constraints = [
    #     (
    #         "phone",
    #         "unique (phone)",
    #         "Customer with the same phone number already Exists!",
    #     ),
    # ]

    @api.one
    @api.depends("price", "qty")
    def _compute_total(self):
        self.total = self.price * self.qty

    @api.constrains("phone")
    def _check_phone(self):
        partner_rec = self.env["res.partner"].search(
            [("phone", "=", self.phone), ("supplier", "=", True), ("id", "!=", self.id)]
        )
        if partner_rec:
            raise ValueError(
                _("Exists ! Already a customer exists in this phone number")
            )
