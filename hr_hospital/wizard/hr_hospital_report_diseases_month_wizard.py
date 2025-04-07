import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class ReportDiseasesForMonthWizard(models.TransientModel):
    _name = 'hr.hospital.report.diseases.month.wizard'
    _description = 'Monthly Disease Report'

    start_date = fields.Date()
    end_date = fields.Date()
    doctor_ids = fields.Many2many(
        comodel_name='hr.hospital.doctor',
        relation='doctor_report_wizard_rel'
    )
    diseases_ids = fields.Many2many(
        comodel_name='hr.hospital.diseases',
        relation='diseases_report_wizard_rel'
    )

    def generate_report(self):
        domain = []
        if self.doctor_ids:
            domain += [('visit_ids.doctor_id', 'in', self.doctor_ids.ids)]
        if self.diseases_ids:
            domain += [('diseases_id', 'in', self.diseases_ids.ids)]
        if self.start_date:
            domain += [('visit_ids.completed_date', '>=', self.start_date)]
        if self.end_date:
            domain += [('visit_ids.completed_date', '<=', self.end_date)]
        return {
            'type': 'ir.actions.act_window',
            'name': 'Report diagnosis',
            'res_model': 'hr.hospital.diagnosis',
            'view_mode': 'tree,form',
            'domain': domain,
            'context': {'group_by': 'diseases_id'},
            'target': 'inline',
        }

    def default_get(self, fields_list):
        res = super().default_get(fields_list)
        res['doctor_ids'] = [(6, 0, self.env.context.get('active_ids'))]
        return res
