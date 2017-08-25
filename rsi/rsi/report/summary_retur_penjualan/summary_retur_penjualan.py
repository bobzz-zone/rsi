# Copyright (c) 2013, myme and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns, data = ["Tanggal:Date:150","Hari:Data:150","Faktur:Int:100","Jumlah:Currency:300"], []
	where=""
	if filters.get("sales"):
		where=""" and sales="{}" """.format(filters.get("sales"))
	if filters.get("type")!="All":
		where=""" {} and jenis_kredit="{}" """.format(where ,filters.get("type"))
	result = frappe.db.sql("""select posting_date,date_format(posting_date,"%W"),count(1) as "qty" , sum(base_grand_total) as "omset" from `tabSales Invoice` where docstatus=1 {} and is_return=1 and (posting_date between "{}" and "{}") group by posting_date """.format(where,filters.get("from_date"),filters.get("to_date")),as_list=1)
	return columns, data
