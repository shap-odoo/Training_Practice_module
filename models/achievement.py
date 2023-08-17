from odoo import models, fields

class Achievement(models.Model):
    _name = 'achievement'
    _description = 'Student Achievements'

    achievement_id = fields.Char(required=True)
    student_id = fields.Many2one('student', string='Student')
    achievement_name = fields.Char()
    date_received = fields.Date()
    awarded_by = fields.Char()
