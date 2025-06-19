{
    'name': 'New Fields in Contacts',
    'version': '1.0.0',
    'summary': 'Adds various new fields to Contacts. '
    'Requires Odoo 16 or newer!',
    'category': 'Custom',
    'author': 'Adrian',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': ['security/ir.model.access.csv', 
             'data/ir_cron_update_next_birthday.xml',
             'views/res_partner_view.xml'],
    'post_init_hook': 'load_stakeholder_options',
    'installable': True,
    'application': True,
    'auto_install': False
}
