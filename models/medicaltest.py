from odoo import models, fields, api

class HospitalMedicalTest(models.Model):
    _name = 'kmhospital.medicaltest'
    _description = 'Medical Test'

    name = fields.Char(string="Medical test name", required=True)
    price = fields.Float(string="Price", required=True)