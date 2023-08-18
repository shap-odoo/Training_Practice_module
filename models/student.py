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
    achievement_ids = fields.One2many('achievement', 'student_id', string='Achievements')
    student_id = fields.Many2one('achievement', string='Student')
    enrollment_ids = fields.One2many('enrollment', 'student_id', string='Enrollments')
    course_id = fields.Many2one('course', string='Course')
