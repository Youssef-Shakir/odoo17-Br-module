from odoo import models, fields

class CoffeeComplaint(models.Model):
    _name = 'coffee.complaint'
    _description = 'Coffee Machine Complaint'

    machine_id = fields.Many2one('coffee.machine', string="Machine", required=True)
    user_id = fields.Many2one('res.users', string="Filed By", default=lambda self: self.env.uid)
    message = fields.Text(string="Issue", required=True)
    status = fields.Selection([
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('closed', 'Closed')
    ], default='open')