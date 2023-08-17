from odoo import models, fields

class Enrollment(models.Model):
    _name = 'enrollment'
    _description = 'Student Course Enrollment'

    student_id = fields.Many2one('student', string='Student')
    course_id = fields.Many2one('course', string='Course')
    enrollment_date = fields.Date()
