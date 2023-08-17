from odoo import models, fields

class Instructor(models.Model):
    _name = 'instructor'
    _description = 'Instructor Information'

    name = fields.Char(required=True)
    email_id = fields.Char()
    contact_no = fields.Char()
    specialization = fields.Char()
    course_ids = fields.One2many('course', 'instructor_id', string='Courses')
