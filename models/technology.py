#-*- coding: utf-8 -*-
import datetime
from email.policy import default
from odoo import models, fields, api

class technology(models.Model):
    _name = 'managesaul.technology'
    _description = 'managesaul.technology'
    name = fields.Char(string='Nombre', readonly=False, required=True, help="Introduzca el nombre")
    description = fields.Char(string='Descripcion', readonly=False, required=True, help="Introduzca la descripcion")
    photo = fields.Image(string="photo")
    task_id= fields.Many2many(comodel_name="managesaul.task",
                                    relation="task_technology",
                                    column1="technology_id",
                                    column2="task_id")
    developer_id = fields.Many2many("managesaul.developer",
                                       relation="developer_technologies",
                                       column1='technology_id',
                                       column2='developer_id')