from odoo import models, fields, api
import datetime

class task(models.Model):
    _name = 'managesaul.task'
    _genero = 'managesaul.task'

    name = fields.Char(string='Nombre', readonly=False, required=True, help="Introduzca el nombre")
    description = fields.Char(string='Descripcion', readonly=False, required=True, help="Introduzca la descripcion")
    start_date = fields.Datetime()
    end_date = fields.Datetime()
    is_paused = fields.Boolean(string='Pausa')
    sprint_id = fields.Many2one(comodel_name = 'managesaul.sprint', string='Sprint', ondelete='cascade')
    technology_id = fields.Many2many(comodel_name="managesaul.technology",
                                    relation="task_technology",
                                    column1="task_id",
                                    column2="technology_id")
    history_id= fields.Many2one(comodel_name = 'managesaul.history', string='history', ondelete='cascade')