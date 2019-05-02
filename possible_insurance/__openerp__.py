{
    'name': 'Claims Management',
    'version': '1.0',
    'category': 'PossibleHealth',
    'summary': 'Prepare Claims for Insurance to be forwarded to insurance connect app',
    'description': """
Prepare Claims for Insurance
==================================

This module prepares Claims for Insurance
""",
    'author': 'PossibleHealth',
    'website': '',
    'images': [],
    'depends': ["base","sale","account"],
    'init_xml': [],
    'update_xml': [

    ],
    'data': [
        'quotation_view.xml',
        'insurance_quotation_view.xml',
        'sale_quotation_table_view.xml'
    ],
    'demo_xml': [],
    'css': [],
    'js': [

    ],
    'test': [],
    'installable': True,
    'auto_install': False,
    'application': True

}