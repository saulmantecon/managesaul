# -*- coding: utf-8 -*-
# from odoo import http


# class Managesaul(http.Controller):
#     @http.route('/managesaul/managesaul', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/managesaul/managesaul/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('managesaul.listing', {
#             'root': '/managesaul/managesaul',
#             'objects': http.request.env['managesaul.managesaul'].search([]),
#         })

#     @http.route('/managesaul/managesaul/objects/<model("managesaul.managesaul"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('managesaul.object', {
#             'object': obj
#         })
