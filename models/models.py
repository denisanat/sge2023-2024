# -*- coding: utf-8 -*-

from odoo import models, fields, api


class player(models.Model):
    _name = 'juego.juego'
    _description = 'Town Hall'

    name = fields.Char()
    level = fields.Integer()

class building(models.Model):
    _name = 'juego.building'

    




#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
