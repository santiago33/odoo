import logging

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from odoo.fields import One2many

_logger = logging.getLogger(__name__)


class ASOrder(models.Model):
    _name = 'as.order'
    _description = 'Order'

    name = fields.Char(
        compute="_compute_name",
        store=True,
        readonly=True,
    )
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Partner',
        required=True,
    )
    vehicle_id = fields.Many2one(
        comodel_name='as.vehicle',
        string='Vehicle',
        required=True,
    )
    date_start = fields.Datetime(required=True, )
    date_end = fields.Datetime()
    notes = fields.Text()
    status = fields.Selection(
        default="draft",
        selection=[
            ('draft', _('draft')),
            ('in_progress', _('in_progress')),
            ('done', _('done')),
            ('cancelled', _('cancelled')),
        ],
    )

    mechanic_id = fields.Many2one(
        comodel_name='res.users'
    )
    total_cost = fields.Char(
        compute="_compute_total_cost",
        store=True,
        readonly=True,
    )

    item_ids = One2many(comodel_name='as.order.item',
                        inverse_name='order_id',
                        string='Items order'
                        )

    @api.depends('item_ids.subtotal_price')
    def _compute_total_cost(self):
        for record in self:
            record.total_cost = sum(item.subtotal_price
                                    for item in record.item_ids)

    @api.depends('partner_id.name', 'vehicle_id.name')
    def _compute_name(self):
        for record in self:
            record.name = f'{record.partner_id.name or ''} {record.vehicle_id.name or ''} #{record.id or ''}'

    def action_open_done_wizard(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Done Order',
            'res_model': 'as.order.done.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_order_id': self.id},
        }

    def print_report(self):
        return (self.env.ref('auto_service.action_report_as_order')
                .report_action(self))
