{
    "name": "HR Hospital",
    "version": "17.0.1.0.0",
    "license": 'OPL-1',
    "author": "Oleksandr Yushko",
    "website": "https://github.com/santiago33/odoo",
    "category": "Human Resources",

    "depends": [
        "base",

    ],

    "external_dependencies": {
        "python": [],
    },

    "data": [
        'security/ir.model.access.csv',

        "wizard/views/hr_hospital_patient_wizard_view.xml",
        "wizard/views/hr_hospital_report_diseases_month_wizard_view.xml",

        "views/hr_hospital_menu.xml",
        "views/hr_hospital_doctor_views.xml",
        "views/hr_hospital_visit_views.xml",
        "views/hr_hospital_diseases_views.xml",
        "views/hr_hospital_patient_views.xml",
        "views/hr_hospital_diagnosis_views.xml",

        "data/hr_hospital_diseases_data.xml",

        "report/hr_hospital_doctor_report.xml"
    ],

    "demo": [
        "demo/hr_hospital_doctor_demo.xml",
        "demo/hr_hospital_patient_demo.xml",
        "demo/hr_hospital_diagnosis_demo.xml",

        "demo/hr_hospital_visit_demo.xml",

    ],

    "assets": {

    },
    'installable': True,
    'auto_install': False,

    'images': [
        'static/description/hospital.png',
    ],
}
