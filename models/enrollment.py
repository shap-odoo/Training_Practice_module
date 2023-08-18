from odoo import models, fields,api

class Enrollment(models.Model):
    _name = 'enrollment'
    _description = 'Student Course Enrollment'

    student_id = fields.Many2one('student', string='Student')
    course_id = fields.Many2one('course', string='Course')
    enrollment_date = fields.Date()
    enrollment_status = fields.Selection(
        string='Enrollment Status',
        selection=[('enrolled', 'Enrolled'), ('expired', 'Expired')],
        compute='_compute_enrollment_status')

    _sql_constraints = [
        ('unique_student_course', 'UNIQUE(student_id, course_id)', 'Student can only enroll once in a course.'),
    ]
    

    @api.depends('course_id.start_date', 'course_id.end_date')
    def _compute_enrollment_status(self):
        for enrollment in self:
            if enrollment.course_id.start_date <= fields.Date.today() <= enrollment.course_id.end_date:
                enrollment.enrollment_status = 'enrolled'
            else:
                enrollment.enrollment_status = 'expired'