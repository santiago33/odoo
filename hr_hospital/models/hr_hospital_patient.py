import logging

from datetime import date
from odoo import models, fields, api
from odoo.fields import One2many

_logger = logging.getLogger(__name__)


class HHPatient(models.Model):
    _name = 'hr.hospital.patient'
    _inherit = 'hr.hospital.person.mixin'
    _description = 'Patient'
    _rec_name = 'full_name'

    birthday = fields.Date()
    passport_data = fields.Char()
    contact_person = fields.Char()
    age = fields.Integer(
        compute="_compute_age",
        store=True,
        readonly=True,
    )
    doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        string='Personal doctor',
    )
    visit_ids = One2many(
        comodel_name='hr.hospital.visit',
        inverse_name='patient_id',
        string='Visits',
    )
    diagnosis_ids = fields.Many2many(
        comodel_name='hr.hospital.diagnosis',
        string="Diagnosis",
        compute="_compute_diagnosis",
        store=True
    )

    @api.depends("birthday")
    def _compute_age(self):
        for record in self:
            if record.birthday:
                year = date.today() - record.birthday
                record.age = year.days / 365.24

    @api.depends('visit_ids.diagnosis_id')
    def _compute_diagnosis(self):
        for record in self:
            record.diagnosis_ids = record.visit_ids.mapped('diagnosis_id')

    def action_open_patient_visits(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'History visit',
            'res_model': 'hr.hospital.visit',
            'view_mode': 'tree,form',
            'domain': [('patient_id', '=', self.id)],
            'context': {'default_patient_id': self.id},
        }
