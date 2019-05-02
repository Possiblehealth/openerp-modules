import netsvc
import pooler
from osv import fields, osv, orm
from tools.translate import _

class res_partner(osv.osv):
    _description = 'Partner'
    _name = "res.partner"
    _inherit = "res.partner"

