import logging

from datetime import date
from odoo import models, fields, api


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
        string='Personal doctor'
    )

    @api.depends("birthday")
    def _compute_age(self):
        for record in self:
            if record.birthday:
                year = date.today() - record.birthday
                record.age = year.days / 365.24
