from odoo import models, fields

class Course(models.Model):
    _name = 'course'
    _description = 'Course'

    name = fields.Char(string='Course Name', required=True)
    category_id = fields.Many2one('course.category', string='Category', required=True)
    instructor_id = fields.Many2one('instructor', string='Instructor')
    description = fields.Text(string='Description')
    syllabus = fields.Text(string='Syllabus')
    max_students = fields.Integer(string='Maximum Students')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('completed', 'Completed')],
        string='Course Status',
        default='draft',
        copy=False)
    enrollment_ids = fields.One2many('enrollment', 'course_id', string='Enrollments')
    instructor_id = fields.Many2one('instructor', string='Instructor', required=True)
    category_id = fields.Many2one('course.category', string='Category', required=True)