from osv import fields, osv
from openerp import netsvc

import logging

_logger = logging.getLogger(__name__)

class sale_order(osv.osv):
    _name = "sale.order"
    _inherit = "sale.order"

    _columns = {
        'is_insurance_type': fields.boolean('Is Insurance'),
        'payment_type': fields.selection([('insurance', 'INSURANCE'), ('cash', 'CASH')], 'Payment Type')
    }

    _defaults = {
        'is_insurance_type': False,
        'payment_type': 'insurance'
    }

    def search(self, cr, user, args, offset=0, limit=None, order="id DESC", context=None, count=False):
        _logger.info("args")
        _logger.info(args)
        _logger.info("user")
        _logger.info(user)
        _logger.info("order")
        _logger.info(order)
        args.append(['is_insurance_type', '=', False])
        res = super(sale_order, self).search(cr, user, args, offset, limit, order, context, count)
        _logger.info(res)
        return res

    def onchange_payment_type(self, cr, uid, ids, payment_type, is_insurance_type, context=None):
        _logger.info("Inside on change payment type")
        _logger.info(payment_type)
        _logger.info("is_insurance_type")
        _logger.info(is_insurance_type)
        if payment_type.lower() == 'insurance':
            is_insurance_type = True
        else:
            is_insurance_type = False
        return {'value': {'is_insurance_type': is_insurance_type}}



sale_order()