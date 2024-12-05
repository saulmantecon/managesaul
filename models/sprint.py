#-*- coding: utf-8 -*-
import datetime
from email.policy import default
from odoo import models, fields, api
import datetime

class sprint(models.Model):
    _name = 'managesaul.sprint'
    _description = 'managesaul.sprint'
    name = fields.Char(string='Nombre', readonly=False, required=True, help="Introduzca el nombre")
    description = fields.Char(string='Descripcion', readonly=False, required=True, help="Introduzca la descripcion")
    duration = fields.Integer()
    start_date = fields.Datetime()
    end_date = fields.Datetime(compute = "_get_end_date", store = True)
    is_paused = fields.Boolean(string='Pausa')
    task_id = fields.One2many(comodel_name ='managesaul.task', inverse_name='sprint_id', string='Task')
    project_id = fields.Many2one(comodel_name='managesaul.project', string='Project', ondelete='cascade' )

    @api.depends('start_date', 'duration')
    def _get_end_date(self):

        for sprint in self:
            #try:
            if isinstance(sprint.start_date, datetime.datetime) and sprint.duration > 0:
                sprint.end_date = sprint.start_date + datetime.timedelta(days=sprint.duration)
            else:
                sprint.end_date = sprint.start_date