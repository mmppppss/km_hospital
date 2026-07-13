from odoo import models, fields


class HospitalEquipment(models.Model):
    _inherit = 'product.template'

    x_price = fields.Float(string="Equipment Price")