import logging
from email.policy import default

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_auto_part = fields.Boolean(
        default=False,
        string='Part for car'
    )
