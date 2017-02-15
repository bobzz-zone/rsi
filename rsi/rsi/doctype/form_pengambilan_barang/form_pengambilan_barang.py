# -*- coding: utf-8 -*-
# Copyright (c) 2015, myme and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _
from frappe.model.mapper import get_mapped_doc

class FormPengambilanBarang(Document):
	pass



# editan rico
@frappe.whitelist()
def make_pengambilan_barang(source_name, target_doc=None):
	def set_missing_values(source, target):
		
		
		target.posting_date = frappe.utils.nowdate()
		target.customer = source.customer_so


	def update_item(source, target, source_parent):

		target.warehouse = source.t_warehouse

		target.amount = (source.qty - source.qty_form) * source.rate
		target.net_amount = source.qty * source.net_rate

		target.qty = source.qty - source.qty_form

		target.ste_docname = source.parent
		target.ste_childname = source.name

	target_doc = get_mapped_doc("Stock Entry", source_name, {
		"Stock Entry": {
			"doctype": "Form Pengambilan Barang",
			"validation": {
				"docstatus": ["=", 1]
			}
		},
		"Stock Entry Detail": {
			"doctype": "Form Pengambilan Barang Data",
			"postprocess": update_item,
			"condition": lambda doc: abs(doc.qty_form) < abs(doc.qty)
		},
		"Sales Taxes and Charges": {
			"doctype": "Sales Taxes and Charges",
			"add_if_empty": True
		},
		"Sales Team": {
			"doctype": "Sales Team",
			"add_if_empty": True
		}
		
	}, target_doc, set_missing_values)

	return target_doc