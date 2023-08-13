{
    "name":"Hospital Managment System",
    "author":"odoo mates",
    "Technical Name":"the hospital management",
    "summary":"odoo 16",
    "website":'www.hospital.com',

    "depends":["mail"],


    'data': [
        "security/ir.model.access.csv",
        'views/menu.xml',
        'views/patient.xml',
        'views/doctor.xml',
        'reports/doctor_report.xml',
        'reports/patient_report.xml',
    ]

}