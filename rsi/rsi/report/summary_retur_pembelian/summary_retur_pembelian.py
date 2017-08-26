# Copyright (c) 2013, myme and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns, data = ["Tanggal:Date:150","Hari:Data:150","Faktur:Int:100","Jumlah:Currency:300"], []
	where=""
	if filters.get("warehouse"):
		where=""" and a.warehouse="{}" """.format(filters.get("warehouse"))
	if filters.get("supplier"):
		where=""" {} and a.supplier="{}" """.format(where ,filters.get("supplier"))
	if filters.get("remark"):
		where=""" {} and a.remarks like "%{}%" """.format(where,filters.get("remark"))
	data = frappe.db.sql("""select a.posting_date,date_format(a.posting_date,"%W"),count(1) as "qty" , sum(a.base_grand_total) as "omset" 
		from (select p.posting_date,p.base_grand_total,pi.warehouse,p.remarks,p.supplier,p.is_return,p.docstatus from `tabPurchase Invoice` p join `tabPurchase Invoice Item` pi on p.name=pi.parent group by name) 
		where a.docstatus=1 and a.is_return=1 {} and (posting_date between "{}" and "{}") a group by a.posting_date """.format(where,filters.get("from_date"),filters.get("to_date")),as_list=1)
	return columns, data