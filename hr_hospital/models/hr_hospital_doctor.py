import logging

from odoo import models, fields, api
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class HHDoctor(models.Model):
    _name = 'hr.hospital.doctor'
    _inherit = 'hr.hospital.person.mixin'
    _description = 'Doctor'
    _rec_name = 'full_name'

    work_experience = fields.Integer()
    is_intern = fields.Boolean(default=False)

    mentor_id  = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        string='Doctor mentor for intern'
    )
    speciality_id = fields.Selection(
        selection=[('1', 'Allergy and Immunology'),
                   ('2', 'Cardiology'),
                   ('3', 'Anesthesiology'),
                   ('4', 'Dermatology'),
                   ('5', 'Family Medicine'),
                   ],
    )

    patient_ids =fields.Many2many(
        comodel_name='hr.hospital.patient',

    )

    @api.constrains('mentor_id')
    def _check_mentor_id(self):
        for record in self:
            if record.is_intern and record.mentor_id:
                raise ValidationError('An intern cannot be a mentor.')
