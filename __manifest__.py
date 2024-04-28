# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Hospital Managemment',
    'version': '1.0.0',
    'category': 'Hospital',
    'author': 'Odoo16',
    'sequence' : -100,
    'summary': 'Hospital Management System',
    'description': """Hospital Management System""",
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_view.xml',
    ],
    'demo': [],
    'application': True,
    'auto_install' : False,
    'license': 'LGPL-3',
}
