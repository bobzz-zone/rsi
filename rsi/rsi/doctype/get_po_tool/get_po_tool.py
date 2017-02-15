from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc


class GetPOTool(Document):
	def po_list_get(self):
		pass

#@frappe.whitelist()
def get_data_from_purchase_order(source_name, target_doc=None):
	def set_missing_values(source, target):
		target_doc = get_mapped_doc("Purchase Order", source_name, {
			"Purchase Order": {
			"doctype": "Get PO Tool",
			"validation": {
			"docstatus": ["=", 1]
			}
		},
		"Purchase Order": {
			"doctype": "Get PO Item",
				"field_map": [
					["po_name", "name"],
					["supplier", "supplier_name"],
					["date", "transaction_date"]
				]
			}
		}, target_doc, set_missing_values)
		return target_doc
