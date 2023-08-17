from odoo import models, fields

class Student(models.Model):
    _name = 'student'
    _description = 'Student Information'

    name = fields.Char(required=True)
    date_of_birth = fields.Date()
    email = fields.Char()
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    contact_no = fields.Char()
    address = fields.Text()
    # achievement_ids = fields.One2many('achievement', 'student_id', string='Achievements')
