from odoo import models, fields, api



class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = 'Hospital Patient'

    name = fields.Char(string='Name', tracking=True)
    ref = fields.Char(string='Reference')
    age = fields.Integer(string='Age', tracking=True)
    gender = fields.Selection(string='Gender', selection=[('male', 'Male'), ('female', 'Female'),], tracking=True)
    active = fields.Boolean(string='Active', default=True)
    
    
