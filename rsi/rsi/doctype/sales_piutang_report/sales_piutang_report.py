# -*- coding: utf-8 -*-
# Copyright (c) 2015, myme and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class SalesPiutangReport(Document):
	def generate(self):
		if not self.sales_partner or self.sales_partner=="":
			frappe.msgprint("Sales Partner Not selected")
			return
		where = """ sales_partner = "{}" """.format(self.sales_partner)
		if self.customer:
			where = """ {} and customer="{}" """.format(where,self.customer)
		invoices = frapp.db.sql("""select customer,name,grand_total,outstanding_amount,due_date from `tabSales Invoice` where {} order by due_date asc""",as_list=1)
		self.set("tagihan", [])
		for r in invoices:
			pp_so = self.append('tagihan', {})
			pp_so.customer = r[0]
			pp_so.invoice = r[1]
			pp_so.total = r[2]
			pp_so.outstanding = r[3]
			pp_so.due_date = r[4]