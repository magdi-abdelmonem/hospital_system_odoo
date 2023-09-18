from odoo import models, fields, api
from datetime import date
class HospitalAppoinment(models.Model):
    _name = 'hospital.appointment'
    _inherit = 'mail.thread'
    _description = "appointment"
    _rec_name = "patient_id"

    patient_id=fields.Many2one("hospital.patient",string="Patient",required=True)
    doctor_id=fields.Many2one("hospital.doctor",string="Doctor",required=True)
    gender=fields.Selection(related="patient_id.gender")
    appointment_time=fields.Datetime(string="Appointment time",default=fields.Datetime.now)
    booking_date=fields.Date(string="Booking Date")
    state=fields.Selection([("draft","Draft"),
                            ("consultation", "consultation"),
                            ("done","Done"),
                            ("canceled","Canceled")],
                                string="State" ,default="draft")
    cancel_reason = fields.Text(string="The reason of cancelation")

    priority=fields.Selection(
                    [("1","low"),
                     ("2","normal"),
                     ("3","high"),
                     ("4","very high"),
                     ],string="Priority")

    def submit_action(self):
        for rec in self:
            rec.state="consultation"

    def cancel_action(self):
        for rec in self:
            rec.state="canceled"


    def done_action(self):
        for rec in self:
            rec.state="done"