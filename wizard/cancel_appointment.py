from odoo import models,fields,api

class CancelAppointment(models.TransientModel):

    _name = 'cancel.appointment'

    def _default_patient(self):
        return self.env['hospital.appointment'].browse(self._context.get('active_id'))

    appointment_id = fields.Many2one("hospital.appointment", string="Appointment", required=True, default=_default_patient)
    cancel_reason = fields.Text(string="The reason of cancelation")


    def cancel_appointment_action(self):
        get_ids = int(self.appointment_id)
        return self.env['hospital.appointment'].browse(get_ids).write(
            {'state': 'canceled', 'cancel_reason': self.cancel_reason})