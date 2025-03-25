import logging
from odoo import models, fields

_logger = logging.getLogger(__name__)


class ReportDiseasesForMonthWizard(models.TransientModel):
    _name = 'hr.hospital.report.diseases.month.wizard'
    _description = 'Monthly Disease Report'

    start_date = fields.Date()
    end_data = fields.Date()
    doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
    )
    diseases_id = fields.Many2many(
        comodel_name='hr.hospital.diseases',
    )

    def generate_report(self):
        diseases = self.env['hr.hospital.'].search([
            ('start_date', '>=', self.start_date),
            ('end_date', '<=', self.end_data),
            ('doctor_id', '=', self.doctor_id),
            ('diseases_id', '=', self.diseases_id)
        ])
        return diseases
