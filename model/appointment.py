from odoo import models, fields, api
from datetime import date
class HospitalAppoinment(models.Model):
    _name = 'hospital.appointment'
    _inherit = 'mail.thread'
    _description = "appointment"

    patient_id=fields.Many2one("hospital.patient",string="Patient",required=True)
    gender=fields.Selection(related="patient_id.gender")
    appointment_time=fields.Datetime(string="Appointment time",default=fields.Datetime.now)
    booking_date=fields.Date(string="Booking Date")