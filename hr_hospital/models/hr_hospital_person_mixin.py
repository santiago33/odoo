import logging
from odoo import models, fields


class PersonMixin(models.AbstractModel):
    _name = 'hr.hospital.person.mixin'
    _description = 'Person mixin'

    full_name = fields.Char(required=True, )
    phone = fields.Char()
    photo = fields.Binary()
    gender = fields.Char()
