from odoo import models, fields,api,exceptions

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

    @api.constrains('enrollment_status')
    def _check_enrollment_status(self):
        for enrollment in self:
            if enrollment.enrollment_status == 'enrolled' and not enrollment.course_id.start_date <= fields.Date.today() <= enrollment.course_id.end_date:
                raise exceptions.ValidationError('Enrollment status should be "Enrolled" only if the course is within its start and end dates.')
            elif enrollment.enrollment_status == 'expired' and enrollment.course_id.start_date <= fields.Date.today() <= enrollment.course_id.end_date:
                raise exceptions.ValidationError('Enrollment status should be "Expired" only if the course is outside its start and end dates.')        