from odoo import models, fields, api


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _inherit = 'mail.thread'
    _description = "doctor.Records"

    name = fields.Char(string="Name", required=True, tracking=True)
    gender = fields.Selection([("male", "Male"), ("female", "Female")], string="Gender", tracking=True)
    spec = fields.Selection([("internal Medicine", "Internal Medicine"),
                             ("cardiology", "Cardiology"),("nephrology", "Nephrology"),
                             ("oncology", "Oncology"), ("surgery", "Surgery"),
                             ("pediatric", "Pediatric"), ("pphthalmologist", "Ophthalmologist"),
                             ("neurology", "Neurology"), ("urology", "Urology"),
                             ("dermatology", "Dermatology"), ("radiology", "Radiology"),
                             ("psychiatry", "Psychiatry"), ("dentistry", "Dentistry"),
                             ], string="Specialization", required=True)
    personal_img=fields.Image(string="Personal Image")

    have_car=fields.Boolean(string="Have a car ? ")
    phone=fields.Integer(string="Phone Number")
    email=fields.Char(string="Email")
    address=fields.Char(string="Address")
    Marital_Status=fields.Selection([("single","Single"),("married","Married")],string="Marital Status")