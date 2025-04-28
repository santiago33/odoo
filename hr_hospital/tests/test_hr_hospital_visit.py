from odoo.addons.hr_hospital.tests.common import TestCommon

from datetime import datetime, timedelta
from odoo.exceptions import ValidationError, UserError


class TestHospitalVisit(TestCommon):
    def test_check_scheduled_date_future(self):
        visit = self.env['hr.hospital.visit'].create({
            'doctor_id': self.hh_doctor.id,
            'patient_id': self.hh_patient.id,
            'scheduled_date': datetime.now() + timedelta(days=1),
        })
        self.assertTrue(visit)

    def test_check_scheduled_date_past(self):
        with self.assertRaises(ValidationError):
            self.env['hr.hospital.visit'].create({
                'doctor_id': self.hh_doctor.id,
                'patient_id': self.hh_patient.id,
                'scheduled_date': datetime.now() - timedelta(days=1),
            })

    def test_check_status_completed_without_date(self):
        with self.assertRaises(ValidationError):
            self.env['hr.hospital.visit'].create({
                'doctor_id': self.hh_doctor.id,
                'patient_id': self.hh_patient.id,
                'scheduled_date': datetime.now() + timedelta(days=1),
                'status': 'completed',
                'completed_date': False,
            })

    def test_unlink_with_diagnosis(self):
        diagnosis = self.env['hr.hospital.diagnosis'].create({
            'description': 'description',
            'diseases_id': self.hh_diseases.id,
        })
        visit = self.env['hr.hospital.visit'].create({
            'doctor_id': self.hh_doctor.id,
            'patient_id': self.hh_patient.id,
            'scheduled_date': datetime.now() + timedelta(days=1),
            'diagnosis_id': diagnosis.id,
        })

        visit.diagnosis_id = diagnosis.id

        with self.assertRaises(UserError):
            visit.unlink()

    def test_get_color_status(self):
        visit = self.env['hr.hospital.visit']
        self.assertEqual(visit.get_color_status('scheduled'), 'text-warning')
        self.assertEqual(visit.get_color_status('completed'), 'text-success')
        self.assertEqual(visit.get_color_status('cancelled'), 'text-danger')
