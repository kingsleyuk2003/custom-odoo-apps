# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# Copyright 2017  Kinsolve Solutions
# Copyright 2017 Kingsley Okonkwo (kingsley@kinsolve.com, +2348030412562)
# License: see https://www.gnu.org/licenses/lgpl-3.0.en.html

{
    'name': 'Stock Level Excel Report',
    'version': '0.1',
    'category': 'Inventory',
    'description': """
Stock Level Report in Excel. Check the Reporting Menu of the Inventory Module. \n
For help contact: Email: kingsley@kinsolve.com or Call: +2348030412562  \n
Maintained by:
Kingsley Okonkwo (CEO Kinsolve Solutions)
""",
    'author': 'Kingsley Okonkwo (kingsley@kinsolve.com)',
    'website': 'http://kinsolve.com',
    'depends': ['base','stock','report_xlsx'],
    'data': [
        'wizard/stock_level_wizard_view.xml',
        'report.xml'
    ],
    'test':[],
    'installable': True,
    'images': [],
}