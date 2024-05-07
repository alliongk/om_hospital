# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Hospital Managemment',
    'version': '1.0.0',
    'category': 'Hospital',
    'author': 'Odoo16',
    'sequence' : -100,
    'summary': 'Hospital Management System',
    'description': """Hospital Management System - Odoo16""",
    'depends': ['mail', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'data/patient_tag_data.xml',
        'data/patient.tag.csv',
        'wizard/cancel_appointment.xml',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
        'views/appointment_view.xml',
        'views/patient_tag_view.xml',
    ],
    'demo': [],
    'application': True,
    'auto_install' : False,
    'license': 'LGPL-3',
}
