{
    'name': 'Armenian Localization',
    'version': '1.0.1',
    "category": "Accounting/Localizations",
    'author': 'Erpswiss',
    'website': 'https://www.erpswiss.com',
    'depends': ['base', 'base_address_city', 'account'],
    'data': [
        'data/account_chart_template_data.xml',
        'data/account.account.template.csv',
        'data/res.country.state.csv',
        'data/res.city.csv',
        'data/account.tax.csv',
        'data/res_country_data.xml',
        "data/account_tax_group_data.xml",
        "data/account_tax_template.xml",
        'data/account_chart_template_configure.xml',
        'views/res_partner_views.xml',
    ],
    'images': ['static/description/Connecter Logo4x.png'],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
