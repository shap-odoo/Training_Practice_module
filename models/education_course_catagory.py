from odoo import models, fields

class CourseCategory(models.Model):
    _name = 'education.course.category'
    _description = 'Course Category'

    # name = fields.Char(string='Category Name', required=True)
    # description = fields.Text(string='Description')
    # parent_id = fields.Many2one('education.course.category', string='Parent Category')
