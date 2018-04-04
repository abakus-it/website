# -*- coding: utf-8 -*-
{
    'name': "Remove header and Footer on Website",

    'summary': """
    """,

    'description': """
        Remove header and Footer on Website

        This module simply adds
        - the choice to display the header on the website pages
        - the choice to display the footer on the website pages
        
        
        This module has been developed by Valentin THIRION @ AbAKUS it-solutions.
    """,

    'author': "Valentin THIRION, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Website',
    'version': '10.0.1.0',

    'depends': [
        'website',
    ],

    'data': [
        'views/website_config.xml',
        'views/website_templates.xml',
    ],

    'installable': True
}
