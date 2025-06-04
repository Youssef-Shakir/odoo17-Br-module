from odoo import models, fields

class CoffeeMachine(models.Model):
    _name = 'coffee.machine'
    _description = 'Coffee Machine'

    name = fields.Char(string="Serial Number", required=True)
    owner_id = fields.Many2one('res.partner', string="Customer")
    invoice_file = fields.Binary(string="Invoice File")
    invoice_filename = fields.Char(string="Filename")
    location = fields.Char(string="Machine Location")
    status = fields.Selection([
    ('active', 'Active'),
    ('maintenance', 'Under Maintenance'),
    ('inactive', 'Inactive'),
    ], string="Status", default='active')
    notes = fields.Text(string="Notes")
