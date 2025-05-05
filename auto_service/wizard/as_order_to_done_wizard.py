import logging

from datetime import datetime
from odoo import models, fields

_logger = logging.getLogger(__name__)


class ASOrderDoneWizard(models.TransientModel):
    _name = 'as.order.done.wizard'
    _description = 'Wizard for closing the order'

    order_id = fields.Many2one('as.order', string='Order', required=True)
    close_comment = fields.Text()

    def action_confirm_close(self):
        self.order_id.status = 'done'
        self.order_id.date_end = datetime.now()
        self.order_id.notes = self.close_comment
