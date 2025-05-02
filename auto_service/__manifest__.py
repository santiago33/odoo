# -*- coding: utf-8 -*-
{
    'name': "Аutomation of car workshops",
    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "Oleksandr Yushko",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '17.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',

        'report/as_order_report.xml',

        'views/as_car_brand_views.xml',
        'views/as_car_model_views.xml',
        'views/as_order_views.xml',
        'views/as_order_item_views.xml',
        'views/as_vehicle_views.xml',

        'views/res_partner_view.xml',
        'views/product_template.xml',

        'views/menu_auto_service.xml',

        'wizard/as_order_to_done_wizard_view.xml',



    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',

    ],
    'images': [
        'static/description/icon.png',
    ],
}
