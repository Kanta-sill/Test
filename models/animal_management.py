from odoo import _, fields, models, api


class AnimalManagement(models.Model):
    _name = 'animal.management'
    _description = 'Animal Management'

    name = fields.Char()
    date_of_birth = fields.Date()
    animal_category = fields.Many2many('animal.management.category')