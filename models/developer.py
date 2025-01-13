from odoo import models, fields, api


class developer(models.Model):  # no se si funciona, preguntar
    _name = 'res.partner'
    _inherit = 'res.partner'
    technologies_id = fields.Many2many("managesaul.technology",
                                       relation="developer_technologies",
                                       column1='developer_id',
                                       column2='technology_id')
