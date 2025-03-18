{
    "name": "HR Hospital",
    "version": "17.0.1.0.0",
    "license": "AGPL-3",
    "author": "Oleksandr Yushko",
    "website": "https://github.com/santiago33",
    "category": "Human Resources",
    "depends": [
        "base",
    ],

    "external_dependencies": {
        "python": [],
    },

    "data": [
        'security/ir.model.access.csv',

        "views/hr_hospital_menu.xml",
        "views/hr_hospital_doctor_views.xml",
        "views/hr_hospital_visit_views.xml",
        "views/hr_hospital_diseases_views.xml",
        "views/hr_hospital_patient_views.xml",
        "data/hr.hospital.diseases.csv",
    ],
    "demo": [
        "demo/hr_hospital_doctor_demo.xml",
        "demo/hr_hospital_patient_demo.xml",
    ],
    "assets": {

    },
    'installable': True,
    'auto_install': False,
}
