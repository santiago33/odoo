import logging

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class ASOrderItem(models.Model):
    _name = 'as.order.item'
    _description = ' Order item'


    order_id = fields.Many2one(
        comodel_name='as.order',
        string='Order',
        required=True,
    )
    product_id = fields.Many2one(
        comodel_name='product.template',
        string='Product',
        required=True,
        domain=[('is_auto_part', '=', True)],
    )
    qty = fields.Integer(default=1)
    price = fields.Integer(string='Price unit')
    subtotal_price = fields.Integer(
        compute="_compute_subtotal",
        store=True,
        readonly=True,
    )

    @api.depends('qty', 'price')
    def _compute_subtotal(self):
        for record in self:
            record.subtotal_price = record.price * record.qty


