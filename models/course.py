from odoo import models, fields,api

class Course(models.Model):
    _name = 'course'
    _description = 'Course'

    name = fields.Char(string='Course Name', required=True)
    category_id = fields.Many2one('course.category', string='Category', required=True)
    instructor_id = fields.Many2one('instructor', string='Instructor',required=True)
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

    total_enrolled_students = fields.Integer(
        string='Total Enrolled Students', compute='_compute_total_enrolled_students')
        
    course_duration = fields.Integer(
        string='Course Duration (Days)', compute='_compute_course_duration')
    remaining_seats = fields.Integer(
        string='Remaining Seats', compute='_compute_remaining_seats')

    _sql_constraints = [
        ('unique_name', 'UNIQUE(name)', 'Course name must be unique.'),
    ]        
  
    @api.depends('enrollment_ids')
    def _compute_total_enrolled_students(self):
        for course in self:
                course.total_enrolled_students = len(course.enrollment_ids)
    @api.depends('start_date', 'end_date')
    def _compute_course_duration(self):
        for course in self:
            if course.start_date and course.end_date:
                delta = course.end_date - course.start_date
                course.course_duration = delta.days + 1
            else:
                course.course_duration = 0

    def action_mark_completed(self):
        self.state = 'completed'

    @api.depends('max_students', 'enrollment_ids')
    def _compute_remaining_seats(self):
        for course in self:
            course.remaining_seats = course.max_students - len(course.enrollment_ids)

    