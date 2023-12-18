# -*- coding: utf-8 -*-

from odoo import models, fields


class AddProduct(models.Model):
    _inherit = 'product.template'

    name = fields.Char(string='Наименование', required=True)
    description = fields.Text(string='Текстовое описание')