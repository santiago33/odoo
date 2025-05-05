import logging

from odoo import models, fields, api, _

_logger = logging.getLogger(__name__)


class ASVehicle(models.Model):
    _name = 'as.vehicle'
    _description = 'Customer Vehicle'
    _sql_constraints = [
        ('license_plate_unique', 'UNIQUE(license_plate)',
         _('License plate must be unique!')),
    ]

    name = fields.Char(
        compute="_compute_name",
        store=True,
        readonly=True,
    )
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        required=True,
    )
    license_plate = fields.Char()
    vin = fields.Char('VIN Code', size=17)
    model_id = fields.Many2one(
        comodel_name='as.car.model',
        string='Car model'

    )
    brand_id = fields.Many2one(
        comodel_name='as.car.brand',
        string='Car manufacture'
    )
    year = fields.Integer()
    notes = fields.Text()

    @api.depends('license_plate', 'model_id')
    def _compute_name(self):
        for record in self:
            record.name = (f'{record.brand_id.name or ''} '
                           f'{record.model_id.name or ''} '
                           f'{record.license_plate or ''}')

    def action_create_order(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'New order',
            'res_model': 'as.order',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_partner_id': self.partner_id.id,
                'default_vehicle_id': self.id,
                'readonly_field': ['partner_id', 'vehicle_id'],
            }
        }
