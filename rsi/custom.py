from __future__ import unicode_literals
import frappe

def update():
	#jv = frappe.db.sql("select parent from `tabJournal Entry Account` where account='2110.100-HUTANG DAGANG - RSI' and debit>0 group by parent",as_list=1)
	pe = frappe.db.sql("select name,party from `tabPayment Entry` where docstatus =1 and mode_of_payment='Giro'",as_list=1)
	for row in pe:
		frappe.db.sql("update `tabGL Entry` set against ='1103.100-PIUTANG GIRO - RSI'  where against = '1102.801-BANK BCA 5993 - RSI' and voucher_no='{}'".format(row[0]))
