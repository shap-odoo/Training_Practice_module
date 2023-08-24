from odoo import models, fields,api,exceptions
import re

class Student(models.Model):
    _name = 'student'
    _description = 'Student Information'

    name = fields.Char(string="name",required=True)
    date_of_birth = fields.Date()
    email = fields.Char(string='Email', help='Enter a valid email address')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    contact_no = fields.Char(string="Contact Number ", required=True)
    address = fields.Text()
    achievement_ids = fields.Many2many('achievement', string='Achievements')
    # achievement_id = fields.Many2one('achievement', string='Student')
    enrollment_ids = fields.One2many('enrollment', 'student_id', string='Enrollments')
    course_id = fields.Many2one('course', string='Course')

    _sql_constraints = [
        ('unique_email', 'UNIQUE(email)', 'Email must be unique.'),
    ]

    @api.constrains('contact_no')
    def _check_contact_no(self):
        for student in self:
            if student.contact_no and not re.match(r'^\d{10}$', student.contact_no):
                raise models.ValidationError('Contact number must be a 10-digit numeric value.')


    @api.depends('enrollment_ids')
    def _compute_total_enrollments(self):
        for student in self:
            student.total_enrollments = len(student.enrollment_ids)

    total_enrollments = fields.Integer(
        string='Total Enrollments', compute='_compute_total_enrollments')

    @api.constrains('email')
    def _check_email(self):
        for student in self:
            if student.email and not re.match(r'^[\w\.-]+@[\w\.-]+$', student.email):
                raise exceptions.ValidationError('Invalid email format.')