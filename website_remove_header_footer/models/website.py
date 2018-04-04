from odoo import api, fields, models, tools

class Website(models.Model):

    _inherit = "website"

    show_header = fields.Boolean(default=True)
    show_footer = fields.Boolean(default=True)

class ResConfigSettings(models.TransientModel):

    _inherit = "website.config.settings"

    show_header = fields.Boolean(related='website_id.show_header')
    show_footer = fields.Boolean(related='website_id.show_footer')