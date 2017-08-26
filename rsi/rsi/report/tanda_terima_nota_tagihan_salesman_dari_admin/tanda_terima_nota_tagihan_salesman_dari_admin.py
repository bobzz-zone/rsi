# Copyright (c) 2013, myme and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns, data = ["Customer:Link/Customer:200","Tanggal:Date:150",
	"Invoice:Link/Sales Invoice:200","Jumlah:Currency:200","Usia:Int:100"], []
	where=""
	if filters.get("sales"):
		where=""" and sales="{}" """.format(filters.get("sales"))
	result = frappe.db.sql("""select customer,posting_date,name,outstanding_amount,datediff(NOW(),posting_date) as "period" from `tabSales Invoice` where docstatus=1 and outstanding_amount>0 and is_return=0 {} and (posting_date between "{}" and "{}") """.format(where,filters.get("from_date"),filters.get("to_date")),as_list=1)
	customer=""
	for row in result:
		if customer == row[0]:
			row.append(["",row[1],row[2],row[3],,row[4]])
		else:
			customer=row[0]
			row.append([row[0],row[1],row[2],row[3],row[4]])
	return columns, data
