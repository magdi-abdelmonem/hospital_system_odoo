{
    "name":"Hospital Managment System",
    "author":"odoo mates",
    "Technical Name":"the hospital management",
    "summary":"odoo 16",
    "website":'www.hospital.com',

    "depends":["mail",'board'],


    'data': [
        "security/ir.model.access.csv",
        'views/menu.xml',
        'views/patient.xml',
        'views/doctor.xml',
        'views/appointment.xml',
        'views/res_config_settings_views.xml',
        'reports/doctor_report.xml',
        'reports/patient_report.xml',
        'wizard/cancel_appointment.xml',
        'data/patient_sequence.xml',
    ]

}