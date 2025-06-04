{
    "name":"Machine_Maintiance_system",
    "version":"0.1",
    "depends": ["stock", "mail", "website", "portal"],
    "author": "Yousif Shakir",
    "category": "Custom",
    "summary": "Track coffee machines by serial and handle customer complaints.",
    "data": [
        "security/ir.model.access.csv",
        "security/security.xml",
        "views/machine_views.xml",
        "views/complaint_views.xml",
        "views/menus.xml",
        "views/portal_templates.xml",
        "views/portal_my_machines_home.xml",
        "views/portal_my_machines_page.xml"
    ],
    "installable": True,
    "application": True,
}