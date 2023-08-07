from odoo import models, fields, api
from odoo.exceptions import ValidationError


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = 'mail.thread'
    _description = "Patient.Records"

    name = fields.Char(string="Name", required=True, tracking=True)
    age = fields.Integer(string="Age", tracking=True)
    is_child = fields.Boolean(string="Is Child", tracking=True)
    notes = fields.Text(string="Notes")
    gender = fields.Selection([("male", "Male"), ("female", "Female")], string="Gender")
    doctor_id=fields.Many2one('hospital.doctor', Ondelete="cascade", string="Doctor", required=True)
    tag_ids=fields.Many2many('res.partner.category' ,string='Tags')
    section= fields.Char(string="Section",store=True)
    capitalize_name = fields.Char(string="Capitalize Name", store=True)

    @api.onchange("doctor_id")
    def _onchange_Section(self):
        if self.doctor_id:
            self.section = self.doctor_id.spec
        else:
            self.section = ''

    @api.onchange("name")
    def _onchange_cap(self):
        if self.name:
            self.capitalize_name = self.name.upper()
        else:
            self.capitalize_name = ''

    @api.constrains("is_child", "age")
    def _check_child_age(self):
        for rec in self:
            if rec.is_child and rec.age == 0:
                raise ValidationError(("you should fill the age"))

    @api.onchange("age")
    def _onchange_age(self):
        if self.age <= 10:
            self.is_child = True
        else:
            self.is_child = False
