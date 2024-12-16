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
    code = fields.Char(string='code', compute='_compute_cod')
    sprint_id = fields.Many2one(comodel_name = 'managesaul.sprint', string='Sprint',compute='_get_sprint', store =True)
    technology_id = fields.Many2many(comodel_name="managesaul.technology",
                                    relation="task_technology",
                                    column1="task_id",
                                    column2="technology_id")
    history_id= fields.Many2one(comodel_name = 'managesaul.history', string='history', ondelete='cascade')
   # project_id = fields.Many2one(comodel_name = 'managesaul.project', related='history.project', readonly=True)

    def _compute_cod(self):
        for task in self:
            task.code = "TSK_" + str(task.id)

    @api.depends('code')
    def _get_sprint(self):
        for task in self:
            sprints = self.env['managesaul.sprint'].search([('project_id.id', '=', task.history_id.project_id.id)])
            found = False
            for sprint in sprints:
                if isinstance(sprint.end_date, datetime.datetime) and sprint.end_date > datetime.datetime.now():
                    task.sprint_id = sprint.id
                    found = True
            if not found:
                task.sprint_id = False