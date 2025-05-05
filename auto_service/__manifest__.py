# -*- coding: utf-8 -*-
{
    'name': "Аutomation of car workshops",
    'license': 'OPL-1',
    'author': "Oleksandr Yushko",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '17.0.0.1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product'],

    # always loaded
    'data': [
        'security/auto_service_security_groups.xml',
        'security/auto_service_security.xml',
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
