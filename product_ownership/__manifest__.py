{
    'name': "Product Ownership",
    'version': '1.0',
    'depends': ['base', 'product'],
    'author': "Yousif Shakir",
    'category': 'Inventory',
    'summary': "Track ownership and status of products",
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/product_ownership_views.xml',
    ],
    'installable': True,
    'application': True,
}
