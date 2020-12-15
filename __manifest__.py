# -*- encoding: utf-8 -*-
{
    'name': 'To-do Application',
    'version': '1.0',
    'author': 'EEP - Profesor',
    'description': """ Modulo primero de las pruebas de desarrollo grupo DAM.""",
    'depends': ['base'],
    'application': True,
    'data' : ['views/todo_app_views.xml',
                'security/ir.model.access.csv',
                'security/todo_access_rules.xml',],
}
