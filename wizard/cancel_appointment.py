from odoo import models, fields, api



class CancelAppointmentWizard(models.TransientModel):
    _name = 'cancel.appointment.wizard'
    _description = 'Cancel Appointment Wizard'

    appointment_id = fields.Many2one(comodel_name='hospital.appointment', string='Appointment')
    reason = fields.Text(string='Reason')
    
    
    def action_cancel(self):
        return