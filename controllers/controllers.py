# -*- coding: utf-8 -*-
from odoo import http

# class TraineeBoard(http.Controller):
#     @http.route('/trainee_board/trainee_board/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/trainee_board/trainee_board/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('trainee_board.listing', {
#             'root': '/trainee_board/trainee_board',
#             'objects': http.request.env['trainee_board.trainee_board'].search([]),
#         })

#     @http.route('/trainee_board/trainee_board/objects/<model("trainee_board.trainee_board"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('trainee_board.object', {
#             'object': obj
#         })