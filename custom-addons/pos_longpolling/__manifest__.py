{
    "name": """POS: Longpolling support""",
    "summary": """Technical module to implement instant updates in POS""",
    "category": "Point of Sale",
    "images": [],
    "version": "14.0.2.3.1",
    "application": False,
    "author": "IT-Projects LLC, Dinar Gabbasov",
    "support": "help@itpp.dev",
    "website": "https://github.com/itpp-labs/pos-addons",
    "license": "Other OSI approved licence",  # MIT
    # "price": 0.00,
    # "currency": "EUR",
    "depends": ["bus", "point_of_sale"],
    "external_dependencies": {"python": [], "bin": []},
    "data": ["views/pos_longpolling_template.xml", "views/pos_longpolling_view.xml"],
    "qweb": ["static/src/xml/SyncNotification.xml"],
    "demo": [],
    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "auto_install": False,
    "installable": True,
}
