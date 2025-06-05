from odoo import models, fields

class ProductOwnership(models.Model):
    _name = 'product.ownership'
    _description = 'Product Ownership'
    _rec_name = 'product_id'

    product_id = fields.Many2one('product.product', string="Product", required=True)
    owner_id = fields.Many2one('res.users', string="Owner", required=True, domain=[('share', '=', True)])
    invoice_file = fields.Binary(string="Invoice File")
    invoice_filename = fields.Char(string="Invoice Filename")
    location = fields.Char(string="Location")

    status = fields.Selection([
        ('active', 'Active'),
        ('maintenance', 'Under Maintenance'),
        ('inactive', 'Inactive'),
    ], string="Status", default='active')

    notes = fields.Text(string="Notes")
