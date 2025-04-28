from odoo.tests.common import TransactionCase


class TestCommon(TransactionCase):

    def setUp(self):
        super(TestCommon, self).setUp()
        self.hh_doctor = self.env['hr.hospital.doctor'].create({
            "full_name": "James Anderson",
            "speciality": "1",
        })
        self.hh_patient = self.env['hr.hospital.patient'].create({
            "full_name": "Степанюк Ольга Олександрівна",
            "birthday": "1970-02-02",
            "gender": "w",
            "phone": "380667778888",
        })
        diseases_parent = self.hh_diseases = self.env['hr.hospital.diseases'].create({

            "id": "hh_diseases_5",
            "name": "Respiratory  system",
            "description": "description 5",

        })
        self.hh_diseases = self.env['hr.hospital.diseases'].create({
            "id": "hh_diseases_6",
            "name": "asthma",
            "description": "description 6",
            "parent_id": diseases_parent.id,

        })
