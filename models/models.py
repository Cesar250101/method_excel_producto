# -*- coding: utf-8 -*-

import tempfile
import binascii
import logging
from datetime import datetime
from odoo.exceptions import Warning
from odoo import models, fields, api, exceptions, _
from odoo.osv import expression
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DF

_logger = logging.getLogger(__name__)
try:
    import csv
except ImportError:
    _logger.debug('Cannot `import csv`.')
try:
    import xlwt
except ImportError:
    _logger.debug('Cannot `import xlwt`.')
try:
    import cStringIO
except ImportError:
    _logger.debug('Cannot `import cStringIO`.')
try:
    import base64
except ImportError:
    _logger.debug('Cannot `import base64`.')



try:
    import xlrd
except ImportError:
    _logger.debug('Cannot `import xlrd`.')



class Productos(models.Model):
    _inherit = 'product.template'

    disponibilidad = fields.Char(string='Disponible en Proveedor')


class account_bank_statement_wizard(models.TransientModel):
    _name= "method_excel_producto.importar.wizard"

    file = fields.Binary('File')
    file_opt = fields.Selection([('excel','Excel'),('csv','CSV')], default='excel')


    @api.multi
    def import_file(self):
        #if not file:
        #    raise Warning('Please Select File')
        if self.file_opt == 'excel':
            fp = tempfile.NamedTemporaryFile(suffix=".xlsx")
            fp.write(binascii.a2b_base64(self.file))
            fp.seek(0)
            values = {}
            workbook = xlrd.open_workbook(fp.name)
            sheet = workbook.sheet_by_index(0)
            contador = 0
            for row_no in range(sheet.nrows-11):
                line = list(map(lambda row:isinstance(row.value, str) and row.value.encode('utf-8') or str(row.value), sheet.row(row_no)))
                try:
                    barcode=line[0]
                    disponible=line[3]
                    fecha=line[3].decode("utf-8")
                    product_obj= self.env['product.template'].search([('barcode','=',barcode)])
                    if product_obj:
                        for i in product_obj:
                            i.disponibilidad=disponible                
                except:
                    _logger.warning('No encuentra Fecha')
#
    def _find_partner(self,name):
        partner_id = self.env['res.partner'].search([('name','=',name)])
        if partner_id:
            return partner_id.id
        else:
            return
