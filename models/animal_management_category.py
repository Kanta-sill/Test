from odoo import _, fields, models, api


class AnimalManagementCategory(models.Model):
    _name = 'animal.management.category'
    _description = 'Animal Category'

    name = fields.Char()
    code = fields.Char()
    icon = fields.Image()
    animal_ids = fields.Many2many('animal.management')

    @api.onchange('name')
    def change_code(self):
        for this in self:
            this.code = this.name