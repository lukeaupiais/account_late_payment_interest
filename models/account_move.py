from odoo import fields, models

class AccountMove(models.Model):
    _inherit = 'account.move'

    interest_amount = fields.Float(string="Interest Amount", default=0.0)
