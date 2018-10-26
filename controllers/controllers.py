# -*- coding: utf-8 -*-
from odoo import http

class TraineeBoard(http.Controller):
    @http.route('/trainee_board/trainee_board/', auth='public', website=True)
    def index(self, **kw):
         Teachers = http.request.env['trainee_board.teachers']
         return http.request.render('trainee_board.index', {
            'teachers': Teachers.search([])
        })

    @http.route('/trainee_board/home/', auth='public', website=True)
    def links(self, **kw):
        return http.request.render('trainee_board.links')

    @http.route('/trainee_board/<int:id>/', auth='public', website=True)
    def teacher(self, id):
        return '<h1>{} ({})</h1>'.format(id, type(id).__name__)


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