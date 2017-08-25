# Copyright (c) 2013, myme and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns, data = ["Tanggal:Date:150","Hari:Data:150","Faktur:Int:100","Jumlah:Currency:300"], []
	where=""
	if filters.get("sales"):
		where=""" and ped.sales="{}" """.format(filters.get("sales"))
	if filters.get("remark"):
		where=""" {} and pe.remarks like "%{}%" """.format(where,filters.get("remark"))
	if filters.get("invoice"):
		where=""" {} and ped.reference_name = "{}" """.format(where,filters.get("invoice"))
	data = frappe.db.sql("""select pe.posting_date,date_format(pe.posting_date,"%W"),count(1) as "qty" , sum(ped.allocated_amount-ped.discount_accumulated) as "omset" 
		from `tabPayment Entry Reference` ped join `tabPayment Entry` pe on ped.parent=pe.name 
	 where pe.docstatus=1 and ped.reference_doctype="Sales Invoice" {} and (pe.posting_date between "{}" and "{}") group by pe.posting_date """.format(where,filters.get("from_date"),filters.get("to_date")),as_list=1)
	return columns, data
