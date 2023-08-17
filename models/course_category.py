from odoo import models, fields

class CourseCategory(models.Model):
    _name = 'course.category'
    _description = 'Course Category'

    name = fields.Char(string='Category Name', required=True)
    description = fields.Text(string='Description')
    course_ids = fields.One2many('course', 'category_id', string='Courses')

