import logging

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class HHDoctor(models.Model):
    _name = 'hr.hospital.doctor'
    _inherit = 'hr.hospital.person.mixin'
    _description = 'Doctor'
    _rec_name = 'full_name'

    work_experience = fields.Integer()
    is_intern = fields.Boolean(default=False)

    mentor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        string='Doctor mentor for intern',
        domain=[('is_intern', '=', False)],
    )
    speciality = fields.Selection(
        selection=[
            ('1', _('Allergy and Immunology')),
            ('2', _('Cardiology')),
            ('3', _('Anesthesiology')),
            ('4', _('Dermatology')),
            ('5', _('Family Medicine')),
        ],
    )

    patient_ids = fields.Many2many(
        comodel_name='hr.hospital.patient',

    )

    @api.constrains('mentor_id')
    def _check_mentor_id(self):
        for record in self:
            if record.mentor_id and record.mentor_id.is_intern:
                raise ValidationError(_('An intern cannot be a mentor.'))
