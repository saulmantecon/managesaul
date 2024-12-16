#-*- coding: utf-8 -*-
import datetime
from email.policy import default
from odoo import models, fields, api

class history(models.Model):
    _name = 'managesaul.history'
    _description = 'managesaul.history'
    name = fields.Char(string='Nombre', readonly=False, required=True, help="Introduzca el nombre")
    description = fields.Char(string='Descripcion', readonly=False, required=True, help="Introduzca la descripcion")
    project_id = fields.Many2one(comodel_name='managesaul.project', string='project', ondelete='cascade')
    task_id = fields.One2many(comodel_name ='managesaul.task', inverse_name='history_id', string='task')
    # Esto no funciona ------------------------------------------
    used_technologies = fields.Many2many("managesaul.technology", compute = "_get_used_technologies")

    def _get_used_technologies(self):
        for history in self:
            technologies = None  # Array para concatenar todas las tecnologías. Inicialmente no tiene valor
            for task in history.task_id:  # Para cada una de las tareas de la historia
                if not technologies:
                    technologies = task.technology_id
                else:
                    technologies = technologies + task.technology_id
            history.used_technologies = technologies  # Asignar las tecnologías a la historia