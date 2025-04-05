import logging

from odoo import models, fields, _

_logger = logging.getLogger(__name__)


class PersonMixin(models.AbstractModel):
    _name = 'hr.hospital.person.mixin'
    _description = 'Person mixin'

    full_name = fields.Char(required=True, )
    phone = fields.Char()
    photo = fields.Binary()
    gender = fields.Selection(
        default="o",
        selection=[
            ('m', _('Men')),
            ('w', _('Woman')),
            ('o', _('Other')),
        ]
    )
