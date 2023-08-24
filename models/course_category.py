from odoo import models, fields

class CourseCategory(models.Model):
    _name = 'course.category'
    _description = 'Course Category'

    name = fields.Char(string='Category Name')
    description = fields.Text(string='Description')
    # category_id = fields.Many2one('course', string='Category')

    # course_ids = fields.One2many('course', 'category_id', string='Courses')

