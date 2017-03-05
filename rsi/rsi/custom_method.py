from __future__ import unicode_literals
import frappe
from frappe import _, throw
from frappe.utils import flt, cint, nowdate,getdate, cstr,date_diff


@frappe.whitelist()
def payment_discount_rule(payment,method):
	deduction=0
	for data in payment.get("references"):
		if data.reference.doctype=="Sales Invoice":
			if nowdate < data.due_date:
				deduction+= flt(data.allocated_amount)
	if deduction>0:
		payment.get("deductions").append(
			{"account":"4103.021-DISC.PENJUALAN JAA UMUM (JAU) - RSI",
			"cost_center":"Main - RSI",
			"amount":deduction})

