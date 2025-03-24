from odoo import models, fields, api
class LearningOne(models.Model):
    _name = "learning.one"
    # Define your fields
    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
