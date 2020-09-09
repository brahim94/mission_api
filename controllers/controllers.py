# -*- coding: utf-8 -*-
# from odoo import http


# class TechMissionApi(http.Controller):
#     @http.route('/tech_mission_api/tech_mission_api/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tech_mission_api/tech_mission_api/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tech_mission_api.listing', {
#             'root': '/tech_mission_api/tech_mission_api',
#             'objects': http.request.env['tech_mission_api.tech_mission_api'].search([]),
#         })

#     @http.route('/tech_mission_api/tech_mission_api/objects/<model("tech_mission_api.tech_mission_api"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tech_mission_api.object', {
#             'object': obj
#         })
