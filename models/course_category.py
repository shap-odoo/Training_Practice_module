from odoo import models, fields

class CourseCategory(models.Model):
    _name = 'course.category'
    _description = 'Course Category'

    name = fields.Char(string='Category Name')
    description = fields.Text(string='Description')
    # course_category_id = fields.Many2one('course', string='Category')
    color = fields.Integer(string=' Tag color')

    # category_id = fields.Many2one('course', string='Category')

    # course_ids = fields.One2many('course', string='Courses')

