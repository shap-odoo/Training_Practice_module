from odoo import models, fields,api

class Instructor(models.Model):
    _name = 'instructor'
    _description = 'Instructor Information'

    name = fields.Char(required=True)
    email_id = fields.Char(string='Email', help='Enter a valid email address')
    contact_no = fields.Integer(string='Contact No.')
    specialization = fields.Char(string="Specialization",required=True)
    course_ids = fields.One2many('course', 'instructor_id', string='Courses')

    @api.depends('course_ids')
    def _compute_total_courses_taught(self):
        for instructor in self:
            instructor.total_courses_taught = len(instructor.course_ids)

    total_courses_taught = fields.Integer(
        string='Total Courses Taught', compute='_compute_total_courses_taught')