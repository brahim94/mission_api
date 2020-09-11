# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class ResConfigFleetSettings(models.TransientModel):

    _inherit = "res.config.settings"

    gps_api_hash = fields.Char('GPS api_hash')


    @api.model
    def set_values(self):
        super(ResConfigFleetSettings, self).set_values()
        set_param = self.env['ir.config_parameter'].sudo().set_param
        set_param('tech_mission_api.gps_api_hash', int(self.gps_api_hash))

    @api.model
    def get_values(self):
        res = super(ResConfigFleetSettings, self).get_values()
        get_param = self.env['ir.config_parameter'].sudo().get_param
        res['gps_api_hash'] = int(get_param('tech_mission_api.gps_api_hash'))
        return res


class Tech_Fleet(models.Model):

    _inherit = "fleet.vehicle"

    gps_id = fields.Char('GPS ID')


class TechMission(models.Model):

    _inherit = "tech.mission"

    date_from = fields.Date(default=fields.Date.today, string="Date from", required="True")
    date_to = fields.Date(string="Date to")
    time_from = fields.Float(string='Time from')
    time_to = fields.Float(string='Time to')
    device_id = fields.Char(related='vehicle_id.gps_id', string='device ID')

    def get_distance(self):
        return self.write({'state': 'cancel'})
