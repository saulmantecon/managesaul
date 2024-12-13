#-*- coding: utf-8 -*-
import datetime
from email.policy import default
from odoo import models, fields, api

class project(models.Model):
    _name = 'managesaul.project'
    _description = 'managesaul.project'
    name = fields.Char(string='Nombre', readonly=False, required=True, help="Introduzca el nombre")
    description = fields.Char(string='Descripcion', readonly=False, required=True, help="Introduzca la descripcion")
    history_id = fields.One2many(comodel_name ='managesaul.history', inverse_name='project_id', string='history')
    sprint_id = fields.One2many(comodel_name='managesaul.sprint', inverse_name='project_id', string='sprints')
