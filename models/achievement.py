from odoo import models, fields

class Achievement(models.Model):
    _name = 'achievement'
    _description = 'Student Achievements'

    achievement_id = fields.Char(string='Achievement ID',required=True)
    achievement_name = fields.Char(string='Achievement Name')
    date_received = fields.Date(string='Date Received')
    awarded_by = fields.Char()

    # Additional Fields
    achievement_type = fields.Selection([  ('course_completion', 'Course Completion'),
        ('top_performer', 'Top Performer'),
        ('perfect_attendance', 'Perfect Attendance'),
    ], string='Achievement Type')

    description = fields.Text(string='Description')
    is_verified = fields.Boolean(string='Verified')
    verification_date = fields.Date(string='Verification Date')
    certificate_image = fields.Binary(string='Certificate Image', attachment=True)
    

    achievement_criteria = fields.Text(string='Achievement Criteria')
    milestone_achieved = fields.Boolean(string='Milestone Achieved')
    student_id = fields.Many2one('student', string='Student')
    # related_projects = fields.Many2many('project', string='Related Projects/Assignments')
    achievement_status = fields.Selection([
        ('pending', 'Pending'),
        ('earned', 'Earned'),
        ('verified', 'Verified')
    ], string='Achievement Status')













    # verification_details = fields.Text(string='Verification Details')
    # notification_sent = fields.Boolean(string='Notification Sent')
    # date_notified = fields.Date(string='Date Notified')
