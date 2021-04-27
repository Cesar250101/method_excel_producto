# -*- coding: utf-8 -*-
from odoo import http

# class MethodExcel-Producto(http.Controller):
#     @http.route('/method_excel-_producto/method_excel-_producto/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/method_excel-_producto/method_excel-_producto/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('method_excel-_producto.listing', {
#             'root': '/method_excel-_producto/method_excel-_producto',
#             'objects': http.request.env['method_excel-_producto.method_excel-_producto'].search([]),
#         })

#     @http.route('/method_excel-_producto/method_excel-_producto/objects/<model("method_excel-_producto.method_excel-_producto"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('method_excel-_producto.object', {
#             'object': obj
#         })