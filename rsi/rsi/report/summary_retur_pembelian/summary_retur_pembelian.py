# Copyright (c) 2013, myme and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns, data = ["Tanggal:Date:150","Hari:Data:150","Faktur:Int:100","Jumlah:Currency:300"], []
	where=""
	if filters.get("warehouse"):
		where=""" and warehouse="{}" """.format(filters.get("warehouse"))
	if filters.get("supplier"):
		where=""" {} and supplier="{}" """.format(where ,filters.get("supplier"))
	if filters.get("remark"):
		where=""" {} and remarks like "%{}%" """.format(where,filters.get("remark"))
	data = frappe.db.sql("""select posting_date,date_format(posting_date,"%W"),count(1) as "qty" , sum(base_grand_total) as "omset" 
		from (select p.posting_date,p.base_grand_total,pi.warehouse,p.remarks,p.supplier,p.is_return,p.docstatus from `tabPurchase Invoice` p join `tabPurchase Invoice Item` pi on p.name=pi.parent group by name) 
		where docstatus=1 and is_return=1 {} and (posting_date between "{}" and "{}") group by posting_date """.format(where,filters.get("from_date"),filters.get("to_date")),as_list=1)
	return columns, data