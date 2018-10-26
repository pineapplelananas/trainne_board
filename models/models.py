# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class trainee_board(models.Model):
#     _name = 'trainee_board.trainee_board'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
class Teachers(models.Model):
    _name = 'trainee_board.teachers'

    name = fields.Char()
    biography = fields.Html()



    # link odoo theme : https://www.odoo.com/documentation/10.0/howtos/themes.html
    # link git tips : https://gist.github.com/aquelito/8596717