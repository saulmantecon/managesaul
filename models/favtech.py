from odoo import models, fields

class favtech(models.Model):
    _name = 'managesaul.favtech'
    _description = 'managesaul.favtech'

    favtech_id = fields.Many2one('managesaul.technology', string='Technology', required=True)
    user = fields.Many2one(
        'res.users',
        string='User',
        default=lambda self: self.env.user,
        required=True
    )
