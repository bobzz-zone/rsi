# -*- coding: utf-8 -*-
# Copyright (c) 2015, Myme and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import msgprint
from frappe.utils import  date_diff

class custom_method(Document):
	pass
@frappe.whitelist()
def auto_sales_assign(doc,method):
	#frappe.session.user
	sales_partner = frappe.db.sql("""select name from `tabSales Partner` where user = "{}" """.format(frappe.session.user),as_list=1)
	if sales_partner :
		for data in sales_partner:
			if doc.sales_partner=="":
				doc.sales_partner=data[0]
			else:
				msgprint("b")
	else:
		msgprint("a")
@frappe.whitelist()
def payment_entry_discount(doc,method):
	total=0
	for ref in doc.references:
		if ref.reference_doctype=="Sales Invoice":
			date = frappe.get_value("Sales Invoice",ref.reference_name,"posting_date")
			diff = date_diff(doc.posting_date,date)
			if diff<13:
				gg=(ref.allocated_amount/0.948)-ref.allocated_amount
				total+=gg
				ref.allocated_amount +=gg
			elif diff < 56:
				gg=(ref.allocated_amount/0.96)-ref.allocated_amount
				total+=gg
				ref.allocated_amount+=gg
	if total >0:
		found=0
		for d in doc.deductions:
			if d.account=="4103.021-DISC.PENJUALAN JAA UMUM (JAU) - RSI":
				found = 1;
				d.amount=total;
		if found==0:
			new_deduction = doc.append("deductions",{})
			new_deduction.account = "4103.021-DISC.PENJUALAN JAA UMUM (JAU) - RSI"
			new_deduction.amount = total
			new_deduction.cost_center = "Main - RSI"
		msgprint("Discount accumulated")

#@frappe.whitelist()
#def update_qty_ste_di_sales_order_on_submit(doc, method):
# 	if doc.order_type == "Titipan" :
# 		# tabel di STE
# 		if doc.items :
# 			sales_order = doc.sales_order
# 			prev_docname = ""
# 			prev_childname = ""
# 			qty_ste = 0
# 			for i in doc.items :
# 				prev_docname = i.prev_docname
# 				prev_childname = i.prev_childname
# 				qty_ste = i.qty

# 				so_qty_ste = frappe.db.sql("""
# 					SELECT
# 					soi.`ste_qty`
# 					FROM `tabSales Order Item` soi
# 					WHERE soi.`parent` = "{}"
# 					AND soi.`name` = "{}"
# 				""".format(prev_docname, prev_childname))

# 				if so_qty_ste :
# 					qty_ste = qty_ste + so_qty_ste[0][0]
# 					frappe.db.sql("""
# 						UPDATE `tabSales Order Item` soi SET soi.`ste_qty` = {0} 
# 						WHERE soi.`parent` = "{1}"
# 						AND soi.`name` = "{2}" 
# 					""".format(qty_ste,prev_docname, prev_childname))
# 					frappe.db.commit()

# 				else :
# 					frappe.db.sql("""
# 						UPDATE `tabSales Order Item` soi SET soi.`ste_qty` = {0} 
# 						WHERE soi.`parent` = "{1}"
# 						AND soi.`name` = "{2}" 
# 					""".format(qty_ste,prev_docname, prev_childname))
# 					frappe.db.commit()

# @frappe.whitelist()
# def update_qty_ste_di_sales_order_on_cancel(doc, method):
# 	if doc.order_type == "Titipan" :
# 		# tabel di STE
# 		if doc.items :
# 			sales_order = doc.sales_order
# 			prev_docname = ""
# 			prev_childname = ""
# 			qty_ste = 0
# 			for i in doc.items :
# 				prev_docname = i.prev_docname
# 				prev_childname = i.prev_childname
# 				qty_ste = i.qty

# 				so_qty_ste = frappe.db.sql("""
# 					SELECT
# 					soi.`ste_qty`
# 					FROM `tabSales Order Item` soi
# 					WHERE soi.`parent` = "{}"
# 					AND soi.`name` = "{}"
# 				""".format(prev_docname, prev_childname))

# 				if so_qty_ste :
# 					qty_ste = so_qty_ste[0][0] - qty_ste
# 					frappe.db.sql("""
# 						UPDATE `tabSales Order Item` soi SET soi.`ste_qty` = {0} 
# 						WHERE soi.`parent` = "{1}"
# 						AND soi.`name` = "{2}" 
# 					""".format(qty_ste,prev_docname, prev_childname))
# 					frappe.db.commit()

# 				else :
# 					frappe.db.sql("""
# 						UPDATE `tabSales Order Item` soi SET soi.`ste_qty` = {0} 
# 						WHERE soi.`parent` = "{1}"
# 						AND soi.`name` = "{2}" 
# 					""".format(qty_ste,prev_docname, prev_childname))
# 					frappe.db.commit()


# @frappe.whitelist()
# def update_qty_fom_di_ste_on_submit(doc, method):
# 	if doc.order_type == "Titipan" :
# 		# tabel di STE
# 		if doc.items :
# 			stock_entry = doc.stock_entry
# 			ste_docname = ""
# 			ste_childname = ""
# 			qty_ste = 0
# 			for i in doc.items :
# 				ste_docname = i.ste_docname
# 				ste_childname = i.ste_childname
# 				qty_ste = i.qty

# 				so_qty_ste = frappe.db.sql("""
# 					SELECT
# 					soi.`qty_form`
# 					FROM `tabStock Entry Detail` soi
# 					WHERE soi.`parent` = "{}"
# 					AND soi.`name` = "{}"
# 				""".format(ste_docname, ste_childname))

# 				if so_qty_ste :
# 					qty_ste = qty_ste + so_qty_ste[0][0]
# 					frappe.db.sql("""
# 						UPDATE `tabStock Entry Detail` soi SET soi.`qty_form` = {0} 
# 						WHERE soi.`parent` = "{1}"
# 						AND soi.`name` = "{2}" 
# 					""".format(qty_ste,ste_docname, ste_childname))
# 					frappe.db.commit()

# 				else :
# 					frappe.db.sql("""
# 						UPDATE `tabStock Entry Detail` soi SET soi.`qty_form` = {0} 
# 						WHERE soi.`parent` = "{1}"
# 						AND soi.`name` = "{2}" 
# 					""".format(qty_ste,ste_docname, ste_childname))
# 					frappe.db.commit()

# @frappe.whitelist()
# def update_qty_form_di_ste_on_cancel(doc, method):
# 	if doc.order_type == "Titipan" :
# 		# tabel di STE
# 		if doc.items :
# 			stock_entry = doc.stock_entry
# 			ste_docname = ""
# 			ste_childname = ""
# 			qty_ste = 0
# 			for i in doc.items :
# 				ste_docname = i.ste_docname
# 				ste_childname = i.ste_childname
# 				qty_ste = i.qty

# 				so_qty_ste = frappe.db.sql("""
# 					SELECT
# 					soi.`qty_form`
# 					FROM `tabStock Entry Detail` soi
# 					WHERE soi.`parent` = "{}"
# 					AND soi.`name` = "{}"
# 				""".format(ste_docname, ste_childname))

# 				if so_qty_ste :
# 					qty_ste = so_qty_ste[0][0] - qty_ste
# 					frappe.db.sql("""
# 						UPDATE `tabStock Entry Detail` soi SET soi.`qty_form` = {0} 
# 						WHERE soi.`parent` = "{1}"
# 						AND soi.`name` = "{2}" 
# 					""".format(qty_ste,ste_docname, ste_childname))
# 					frappe.db.commit()

# 				else :
# 					frappe.db.sql("""
# 						UPDATE `tabStock Entry Detail` soi SET soi.`qty_form` = {0} 
# 						WHERE soi.`parent` = "{1}"
# 						AND soi.`name` = "{2}" 
# 					""".format(qty_ste,ste_docname, ste_childname))
# 					frappe.db.commit()



# @frappe.whitelist()
# def check_workflow(table_name, name):
# 	result = ""
# 	frappe.db.sql("""
# 			UPDATE `tab{0}` SET workflow_state = "Pending" WHERE name = "{1}" """.format(table_name, name))
# 	frappe.db.commit()

# @frappe.whitelist()
# def insert_invoice_summary(doc, method):
	
# 	if doc.is_return == 1 :
# 		sales_invoice_return = doc.name
# 		return_against = doc.return_against

# 		mi = frappe.get_doc("Sales Invoice", doc.return_against)
# 		mi.append("invoice_summary", {
# 			"doctype": "Invoice Summary",
# 			"type" : "Sales Invoice",
# 			"type_code" : doc.name,
# 			"date" : doc.posting_date
# 		})

# 		mi.flags.ignore_permissions = 1
# 		mi.save()



# @frappe.whitelist()
# def validate_item_colour(doc, method):
# 	if doc.colour :
# 		count = 0

# 		split_colour = doc.colour.split("\n")


# 		# new_colour = []

# 		# garis_lurus = "|"
# 		# for i in split_colour :
# 		# 	if garis_lurus in i :
# 		# 		if i.split("|")[0] < 0 :
# 		# 			frappe.throw("Nomor Warna tidak boleh -")
# 		# 		elif i.split("|")[0] < 10 :
# 		# 			new_colour.append("0"+str(i.split("|")[0])+"|"+i.split("|")[1])

# 		# 		else :
# 		# 			new_colour.append(str(i))

# 		# 	elif garis_lurus not in i :
# 		# 		if i < 0 :
# 		# 			frappe.throw("Nomor Warna tidak boleh -")
# 		# 		elif i < 10 and i >= 0 :
# 		# 			new_colour.append("0"+str(i))
# 		# 		else :
# 		# 			new_colour.append(str(i))
# 		# 	else :
# 		# 		frappe.throw("Format tidak sesuai dengan Colour")

		

# 		# new_colour_final = ""
# 		# count = 0
# 		# for n in new_colour :
# 		# 	if count == 0 :
# 		# 		new_colour_final = str(n) + "\n"
# 		# 		count = count + 1
# 		# 	else :
# 		# 		new_colour_final + new_colour_final + str(n) + "\n"

# 		# doc.colour = new_colour_final




# 		for c in split_colour :
			
# 			check_colour = frappe.db.sql("""
# 				SELECT c.`name` 
# 				FROM `tabColour` c
# 				WHERE c.`name` = "{}"
# 			""".format(c))

# 			if check_colour :
# 				count = 1
# 			else :
# 				pr_doc = frappe.new_doc("Colour")
# 				pr_doc.update({
# 					"colour": c
# 				})
# 				pr_doc.flags.ignore_permissions = 1
# 				pr_doc.save()


# @frappe.whitelist()
# def divide_group(item_code_variant):
	
# 	group = item_code_variant.split(" ")[0]

# 	return group



# # @frappe.whitelist()
# # def projected_stock_by_item_pcs(item_code):

# 		# qty_pending_order = 0
# 		# qty_terkirim = 0
# 		# qty_dialokasi = 0
# 		# qty_inventory = 0

# 		# uom = frappe.get_doc("Item",item_code).stock_uom


# 		# get_qty_pending_order = frappe.db.sql("""
# 		# 	SELECT
# 		# 	SUM(por.`pcs_qty`)

# 		# 	FROM `tabPending Order` po
# 		# 	JOIN `tabPending Order Pcs` por
# 		# 	ON po.`name` = por.`parent`
# 		# 	WHERE po.`docstatus` < 2
# 		# 	AND por.`docstatus` < 2
# 		# 	AND por.`item_code_pcs` = "{}"
# 		# 	GROUP BY por.`item_code_pcs`
# 		# 	""".format(item_code))


# 		# get_qty_terkirim = frappe.db.sql("""
# 		# 	SELECT
# 		# 	SUM(por.`qty_terkirim`)

# 		# 	FROM `tabPending Order` po
# 		# 	JOIN `tabPending Order Pcs` por
# 		# 	ON po.`name` = por.`parent`
# 		# 	WHERE po.`docstatus` < 2
# 		# 	AND por.`docstatus` < 2
# 		# 	AND por.`item_code_pcs` = "{}"
# 		# 	GROUP BY por.`item_code_pcs`
# 		# 	""".format(item_code))



# 		# get_qty_dialokasi = frappe.db.sql("""
# 		# 	SELECT
# 		# 	SUM(por.`qty_dialokasi`)

# 		# 	FROM `tabPending Order` po
# 		# 	JOIN `tabPending Order Pcs` por
# 		# 	ON po.`name` = por.`parent`
# 		# 	WHERE po.`docstatus` < 2
# 		# 	AND por.`docstatus` < 2
# 		# 	AND por.`item_code_pcs` = "{}"
# 		# 	GROUP BY por.`item_code_pcs`
# 		# 	""".format(item_code))



# 		# # bukan dari inventory karena pcs tetapi ambil dari tab Bin
# 		# get_qty_inventory = frappe.db.sql("""
# 		# 	SELECT
# 		# 	SUM(b.`actual_qty`)
# 		# 	FROM `tabBin` b
# 		# 	WHERE b.`item_code` = "{}"
# 		# 	GROUP BY b.`item_code`
# 		# 	""".format(item_code))



# 		# if get_qty_pending_order :
# 		# 	qty_pending_order = float(get_qty_pending_order[0][0])
# 		# else :
# 		# 	qty_pending_order = 0


# 		# if get_qty_terkirim :
# 		# 	qty_terkirim = float(get_qty_terkirim[0][0])
# 		# else :
# 		# 	qty_terkirim = 0


# 		# if get_qty_dialokasi :
# 		# 	qty_dialokasi = float(get_qty_dialokasi[0][0])
# 		# else :
# 		# 	qty_dialokasi = 0


# 		# if get_qty_inventory :
# 		# 	qty_inventory = float(get_qty_inventory[0][0])
# 		# else :
# 		# 	qty_inventory = 0

# 		# send_data = []
# 		# temp_qty_pending_order = qty_pending_order - qty_dialokasi - qty_terkirim
# 		# temp_qty_dialokasi = qty_dialokasi
# 		# temp_qty_terkirim = qty_terkirim
# 		# temp_qty_inventory = qty_inventory - qty_dialokasi - (qty_pending_order - qty_dialokasi - qty_terkirim)

# 		# send_data.append(str(temp_qty_pending_order))
# 		# send_data.append(str(temp_qty_dialokasi))
# 		# send_data.append(str(temp_qty_terkirim))
# 		# send_data.append(str(temp_qty_inventory))


	

# # 	return send_data





# @frappe.whitelist()
# def projected_stock_by_item(item_code, colour):
# 	uom = frappe.get_doc("Item",item_code).stock_uom

# 	if uom == "Pcs" :
# 		qty_pending_order = 0
# 		qty_terkirim = 0
# 		qty_dialokasi = 0
# 		qty_inventory = 0

# 		get_qty_pending_order = frappe.db.sql("""
# 			SELECT
# 			SUM(por.`qty_sisa`)

# 			FROM `tabPending Order` po
# 			JOIN `tabPending Order Pcs` por
# 			ON po.`name` = por.`parent`
# 			WHERE po.`docstatus` < 2
# 			AND por.`docstatus` < 2
# 			AND por.`item_code_pcs` = "{}"
# 			GROUP BY por.`item_code_pcs`
# 			""".format(item_code))

# 		get_qty_terkirim = frappe.db.sql("""
# 			SELECT
# 			SUM(por.`pcs_qty`)

# 			FROM `tabPacking List Delivery` po
# 			JOIN `tabPacking List Delivery Pcs` por
# 			ON po.`name` = por.`parent`
# 			WHERE po.`docstatus` < 2
# 			AND por.`docstatus` < 2
# 			AND por.`item_code_pcs` = "{}"
# 			GROUP BY por.`item_code_pcs`
# 			""".format(item_code))

# 		get_qty_dialokasi = frappe.db.sql("""
# 			SELECT
# 			SUM(por.`qty_sisa`)

# 			FROM `tabOrder Processing` po
# 			JOIN `tabOrder Processing Summary Pcs` por
# 			ON po.`name` = por.`parent`
# 			WHERE po.`docstatus` < 2
# 			AND por.`docstatus` < 2
# 			AND por.`item_code_pcs` = "{}"
# 			GROUP BY por.`item_code_pcs`
# 			""".format(item_code))

# 		# bukan dari inventory karena pcs tetapi ambil dari tab Bin
# 		get_qty_inventory = frappe.db.sql("""
# 			SELECT
# 			SUM(b.`actual_qty`)
# 			FROM `tabBin` b
# 			WHERE b.`item_code` = "{}"
# 			GROUP BY b.`item_code`
# 			""".format(item_code))


# 		if get_qty_pending_order :
# 			qty_pending_order = float(get_qty_pending_order[0][0])
# 		else :
# 			qty_pending_order = 0

# 		if get_qty_terkirim :
# 			qty_terkirim = float(get_qty_terkirim[0][0])
# 		else :
# 			qty_terkirim = 0

# 		if get_qty_dialokasi :
# 			qty_dialokasi = float(get_qty_dialokasi[0][0])
# 		else :
# 			qty_dialokasi = 0

# 		if get_qty_inventory :
# 			qty_inventory = float(get_qty_inventory[0][0])
# 		else :
# 			qty_inventory = 0

# 		send_data = []
# 		if qty_terkirim == 0 :
# 			temp_qty_terkirim = 0
# 		else :
# 			temp_qty_terkirim = qty_terkirim

# 		if qty_dialokasi == 0 :
# 			temp_qty_dialokasi = 0
# 		else :
# 			temp_qty_dialokasi = qty_dialokasi - temp_qty_terkirim


# 		if qty_pending_order == 0 :
# 			temp_qty_pending_order = 0
# 		else :
# 			temp_qty_pending_order = qty_pending_order - temp_qty_dialokasi


# 		if qty_inventory == 0 :
# 			temp_qty_inventory = 0
# 		else :
# 			temp_qty_inventory = qty_inventory - temp_qty_dialokasi

# 		send_data.append(str(temp_qty_pending_order))
# 		send_data.append(str(temp_qty_dialokasi))
# 		send_data.append(str(temp_qty_terkirim))
# 		send_data.append(str(temp_qty_inventory))

# 		return send_data

# 	else :
# 		qty_pending_order = 0
# 		qty_terkirim = 0
# 		qty_dialokasi = 0
# 		qty_inventory = 0

# 		get_qty_pending_order = frappe.db.sql("""
# 			SELECT
# 			SUM(por.`qty_sisa`)

# 			FROM `tabPending Order` po
# 			JOIN `tabPending Order Roll` por
# 			ON po.`name` = por.`parent`
# 			WHERE po.`docstatus` < 2
# 			AND por.`docstatus` < 2
# 			AND por.`item_code_roll` = "{}"
# 			AND por.`colour` = "{}"
# 			GROUP BY por.`item_code_roll`
# 			""".format(item_code, colour))

# 		get_qty_terkirim = frappe.db.sql("""
# 			SELECT
# 			SUM(por.`roll_qty`)

# 			FROM `tabPacking List Delivery` po
# 			JOIN `tabPacking List Delivery Data` por
# 			ON po.`name` = por.`parent`
# 			WHERE po.`docstatus` < 2
# 			AND por.`docstatus` < 2
# 			AND por.`item_code_roll` = "{}"
# 			AND por.`colour` = "{}"
# 			GROUP BY por.`item_code_roll`
# 			""".format(item_code, colour))

# 		get_qty_dialokasi = frappe.db.sql("""
# 			SELECT
# 			SUM(por.`qty_sisa`)

# 			FROM `tabOrder Processing` po
# 			JOIN `tabOrder Processing Summary Roll` por
# 			ON po.`name` = por.`parent`
# 			WHERE po.`docstatus` < 2
# 			AND por.`docstatus` < 2
# 			AND por.`item_code_roll` = "{}"
# 			AND por.`colour` = "{}"
# 			GROUP BY por.`item_code_roll`
# 			""".format(item_code, colour))

# 		get_qty_inventory = frappe.db.sql("""
# 			SELECT
# 			SUM(di.`total_roll`)
# 			FROM `tabData Inventory` di
# 			WHERE di.`item_code_variant` = "{}"
# 			AND di.`colour` = "{}"

# 			GROUP BY di.`item_code_variant`
# 			""".format(item_code, colour))

# 		if get_qty_pending_order :
# 			qty_pending_order = float(get_qty_pending_order[0][0])
# 		else :
# 			qty_pending_order = 0

# 		if get_qty_terkirim :
# 			qty_terkirim = float(get_qty_terkirim[0][0])
# 		else :
# 			qty_terkirim = 0

# 		if get_qty_dialokasi :
# 			qty_dialokasi = float(get_qty_dialokasi[0][0])
# 		else :
# 			qty_dialokasi = 0

# 		if get_qty_inventory :
# 			qty_inventory = float(get_qty_inventory[0][0])
# 		else :
# 			qty_inventory = 0

# 		send_data = []

# 		if qty_terkirim == 0 :
# 			temp_qty_terkirim = 0
# 		else :
# 			temp_qty_terkirim = qty_terkirim

# 		if qty_dialokasi == 0 :
# 			temp_qty_dialokasi = 0
# 		else :
# 			temp_qty_dialokasi = qty_dialokasi - temp_qty_terkirim


# 		if qty_pending_order == 0 :
# 			temp_qty_pending_order = 0
# 		else :
# 			temp_qty_pending_order = qty_pending_order - temp_qty_dialokasi
		


# 		if qty_inventory == 0 :
# 			temp_qty_inventory = 0
# 		else :
# 			temp_qty_inventory = qty_inventory - temp_qty_dialokasi


# 		send_data.append(str(temp_qty_pending_order))
# 		send_data.append(str(temp_qty_dialokasi))
# 		send_data.append(str(temp_qty_terkirim))
# 		send_data.append(str(temp_qty_inventory))

# 		return send_data




# @frappe.whitelist()
# def projected_stock_by_colour(item_code, colour):

# 	qty_pending_order = 0
# 	qty_terkirim = 0
# 	qty_dialokasi = 0
# 	qty_inventory = 0

# 	uom = frappe.get_doc("Item",item_code).stock_uom

# 	get_qty_pending_order = frappe.db.sql("""
# 		SELECT
# 		SUM(por.`qty_sisa`)

# 		FROM `tabPending Order` po
# 		JOIN `tabPending Order Roll` por
# 		ON po.`name` = por.`parent`
# 		WHERE po.`docstatus` < 2
# 		AND por.`docstatus` < 2
# 		AND por.`item_code_roll` = "{}"
# 		AND por.`colour` = "{}"
# 		GROUP BY por.`item_code_roll`
# 		""".format(item_code, colour))

# 	get_qty_terkirim = frappe.db.sql("""
# 		SELECT
# 		SUM(por.`roll_qty`)

# 		FROM `tabPacking List Delivery` po
# 		JOIN `tabPacking List Delivery Data` por
# 		ON po.`name` = por.`parent`
# 		WHERE po.`docstatus` < 2
# 		AND por.`docstatus` < 2
# 		AND por.`item_code_roll` = "{}"
# 		AND por.`colour` = "{}"
# 		GROUP BY por.`item_code_roll`
# 		""".format(item_code, colour))

# 	get_qty_dialokasi = frappe.db.sql("""
# 		SELECT
# 		SUM(por.`qty_sisa`)

# 		FROM `tabOrder Processing` po
# 		JOIN `tabOrder Processing Summary Roll` por
# 		ON po.`name` = por.`parent`
# 		WHERE po.`docstatus` < 2
# 		AND por.`docstatus` < 2
# 		AND por.`item_code_roll` = "{}"
# 		AND por.`colour` = "{}"
# 		GROUP BY por.`item_code_roll`
# 		""".format(item_code, colour))

# 	get_qty_inventory = frappe.db.sql("""
# 		SELECT
# 		SUM(di.`total_roll`)
# 		FROM `tabData Inventory` di
# 		WHERE di.`item_code_variant` = "{}"
# 		AND di.`colour` = "{}"

# 		GROUP BY di.`item_code_variant`
# 		""".format(item_code, colour))


# 	if get_qty_pending_order :
# 		qty_pending_order = float(get_qty_pending_order[0][0])
# 	else :
# 		qty_pending_order = 0

# 	if get_qty_terkirim :
# 		qty_terkirim = float(get_qty_terkirim[0][0])
# 	else :
# 		qty_terkirim = 0

# 	if get_qty_dialokasi :
# 		qty_dialokasi = float(get_qty_dialokasi[0][0])
# 	else :
# 		qty_dialokasi = 0

# 	if get_qty_inventory :
# 		qty_inventory = float(get_qty_inventory[0][0])
# 	else :
# 		qty_inventory = 0

# 	send_data = []
# 	if qty_terkirim == 0 :
# 		temp_qty_terkirim = 0
# 	else :
# 		temp_qty_terkirim = qty_terkirim

# 	if qty_dialokasi == 0 :
# 		temp_qty_dialokasi = 0
# 	else :
# 		temp_qty_dialokasi = qty_dialokasi - temp_qty_terkirim


# 	if qty_pending_order == 0 :
# 		temp_qty_pending_order = 0
# 	else :
# 		temp_qty_pending_order = qty_pending_order - temp_qty_dialokasi




# 	if qty_inventory == 0 :
# 		temp_qty_inventory = 0
# 	else :
# 		temp_qty_inventory = qty_inventory - temp_qty_dialokasi

# 	send_data.append(str(temp_qty_pending_order))
# 	send_data.append(str(temp_qty_dialokasi))
# 	send_data.append(str(temp_qty_terkirim))
# 	send_data.append(str(temp_qty_inventory))

# 	return send_data










# # repack
# @frappe.whitelist()
# def projected_stock_by_item_repack(item_code, colour, yard_atau_meter_per_roll):
# 	uom = frappe.get_doc("Item",item_code).stock_uom
	
# 	qty_pending_order = 0
# 	qty_terkirim = 0
# 	qty_dialokasi = 0
# 	qty_inventory = 0

# 	get_qty_pending_order = frappe.db.sql("""
# 		SELECT
# 		SUM(por.`qty_sisa`)

# 		FROM `tabPending Order` po
# 		JOIN `tabPending Order Roll` por
# 		ON po.`name` = por.`parent`
# 		WHERE po.`docstatus` < 2
# 		AND por.`docstatus` < 2
# 		AND por.`item_code_roll` = "{}"
# 		AND por.`colour` = "{}"
# 		GROUP BY por.`item_code_roll`
# 		""".format(item_code, colour))

# 	get_qty_terkirim = frappe.db.sql("""
# 		SELECT
# 		SUM(por.`roll_qty`)

# 		FROM `tabPacking List Delivery` po
# 		JOIN `tabPacking List Delivery Data` por
# 		ON po.`name` = por.`parent`
# 		WHERE po.`docstatus` < 2
# 		AND por.`docstatus` < 2
# 		AND por.`item_code_roll` = "{}"
# 		AND por.`colour` = "{}"
# 		AND por.`yard_atau_meter_per_roll` = "{}"
# 		GROUP BY por.`item_code_roll`
# 		""".format(item_code, colour, yard_atau_meter_per_roll))

# 	get_qty_dialokasi = frappe.db.sql("""
# 		SELECT
# 		SUM(por.`qty_sisa`)

# 		FROM `tabOrder Processing` po
# 		JOIN `tabOrder Processing Summary Roll` por
# 		ON po.`name` = por.`parent`
# 		WHERE po.`docstatus` < 2
# 		AND por.`docstatus` < 2
# 		AND por.`item_code_roll` = "{}"
# 		AND por.`colour` = "{}"
# 		AND por.`yard_atau_meter` = "{}"
# 		GROUP BY por.`item_code_roll`
# 		""".format(item_code, colour, yard_atau_meter_per_roll))

# 	get_qty_inventory = frappe.db.sql("""
# 		SELECT
# 		SUM(di.`total_roll`)
# 		FROM `tabData Inventory` di
# 		WHERE di.`item_code_variant` = "{}"
# 		AND di.`colour` = "{}"
# 		AND di.`yard_atau_meter_per_roll` = "{}"

# 		GROUP BY di.`item_code_variant`
# 		""".format(item_code, colour, yard_atau_meter_per_roll))

# 	if get_qty_pending_order :
# 		qty_pending_order = float(get_qty_pending_order[0][0])
# 	else :
# 		qty_pending_order = 0

# 	if get_qty_terkirim :
# 		qty_terkirim = float(get_qty_terkirim[0][0])
# 	else :
# 		qty_terkirim = 0

# 	if get_qty_dialokasi :
# 		qty_dialokasi = float(get_qty_dialokasi[0][0])
# 	else :
# 		qty_dialokasi = 0

# 	if get_qty_inventory :
# 		qty_inventory = float(get_qty_inventory[0][0])
# 	else :
# 		qty_inventory = 0

# 	send_data = []

# 	if qty_terkirim == 0 :
# 		temp_qty_terkirim = 0
# 	else :
# 		temp_qty_terkirim = qty_terkirim

# 	if qty_dialokasi == 0 :
# 		temp_qty_dialokasi = 0
# 	else :
# 		temp_qty_dialokasi = qty_dialokasi - temp_qty_terkirim


# 	if qty_pending_order == 0 :
# 		temp_qty_pending_order = 0
# 	else :
# 		temp_qty_pending_order = qty_pending_order - temp_qty_dialokasi
	


# 	if qty_inventory == 0 :
# 		temp_qty_inventory = 0
# 	else :
# 		temp_qty_inventory = qty_inventory - temp_qty_dialokasi


# 	send_data.append(str(temp_qty_pending_order))
# 	send_data.append(str(temp_qty_dialokasi))
# 	send_data.append(str(temp_qty_terkirim))
# 	send_data.append(str(temp_qty_inventory))

# 	return send_data




# @frappe.whitelist()
# def projected_stock_by_colour_repack(item_code, colour, yard_atau_meter_per_roll):

# 	qty_pending_order = 0
# 	qty_terkirim = 0
# 	qty_dialokasi = 0
# 	qty_inventory = 0

# 	uom = frappe.get_doc("Item",item_code).stock_uom

# 	get_qty_pending_order = frappe.db.sql("""
# 		SELECT
# 		SUM(por.`qty_sisa`)

# 		FROM `tabPending Order` po
# 		JOIN `tabPending Order Roll` por
# 		ON po.`name` = por.`parent`
# 		WHERE po.`docstatus` < 2
# 		AND por.`docstatus` < 2
# 		AND por.`item_code_roll` = "{}"
# 		AND por.`colour` = "{}"
# 		GROUP BY por.`item_code_roll`
# 		""".format(item_code, colour))

# 	get_qty_terkirim = frappe.db.sql("""
# 		SELECT
# 		SUM(por.`roll_qty`)

# 		FROM `tabPacking List Delivery` po
# 		JOIN `tabPacking List Delivery Data` por
# 		ON po.`name` = por.`parent`
# 		WHERE po.`docstatus` < 2
# 		AND por.`docstatus` < 2
# 		AND por.`item_code_roll` = "{}"
# 		AND por.`colour` = "{}"
# 		AND por.`yard_atau_meter_per_roll` = "{}"
# 		GROUP BY por.`item_code_roll`
# 		""".format(item_code, colour, yard_atau_meter_per_roll))

# 	get_qty_dialokasi = frappe.db.sql("""
# 		SELECT
# 		SUM(por.`qty_sisa`)

# 		FROM `tabOrder Processing` po
# 		JOIN `tabOrder Processing Summary Roll` por
# 		ON po.`name` = por.`parent`
# 		WHERE po.`docstatus` < 2
# 		AND por.`docstatus` < 2
# 		AND por.`item_code_roll` = "{}"
# 		AND por.`colour` = "{}"
# 		AND por.`yard_atau_meter` = "{}"
# 		GROUP BY por.`item_code_roll`
# 		""".format(item_code, colour, yard_atau_meter_per_roll))

# 	get_qty_inventory = frappe.db.sql("""
# 		SELECT
# 		SUM(di.`total_roll`)
# 		FROM `tabData Inventory` di
# 		WHERE di.`item_code_variant` = "{}"
# 		AND di.`colour` = "{}"
# 		AND di.`yard_atau_meter_per_roll` = "{}"
# 		GROUP BY di.`item_code_variant`
# 		""".format(item_code, colour, yard_atau_meter_per_roll))


# 	if get_qty_pending_order :
# 		qty_pending_order = float(get_qty_pending_order[0][0])
# 	else :
# 		qty_pending_order = 0

# 	if get_qty_terkirim :
# 		qty_terkirim = float(get_qty_terkirim[0][0])
# 	else :
# 		qty_terkirim = 0

# 	if get_qty_dialokasi :
# 		qty_dialokasi = float(get_qty_dialokasi[0][0])
# 	else :
# 		qty_dialokasi = 0

# 	if get_qty_inventory :
# 		qty_inventory = float(get_qty_inventory[0][0])
# 	else :
# 		qty_inventory = 0

# 	send_data = []
# 	if qty_terkirim == 0 :
# 		temp_qty_terkirim = 0
# 	else :
# 		temp_qty_terkirim = qty_terkirim

# 	if qty_dialokasi == 0 :
# 		temp_qty_dialokasi = 0
# 	else :
# 		temp_qty_dialokasi = qty_dialokasi - temp_qty_terkirim


# 	if qty_pending_order == 0 :
# 		temp_qty_pending_order = 0
# 	else :
# 		temp_qty_pending_order = qty_pending_order - temp_qty_dialokasi




# 	if qty_inventory == 0 :
# 		temp_qty_inventory = 0
# 	else :
# 		temp_qty_inventory = qty_inventory - temp_qty_dialokasi

# 	send_data.append(str(temp_qty_pending_order))
# 	send_data.append(str(temp_qty_dialokasi))
# 	send_data.append(str(temp_qty_terkirim))
# 	send_data.append(str(temp_qty_inventory))

# 	return send_data



# @frappe.whitelist()
# def projected_stock_by_yard_repack(item_code, colour, yard_atau_meter_per_roll):

# 	qty_pending_order = 0
# 	qty_terkirim = 0
# 	qty_dialokasi = 0
# 	qty_inventory = 0

# 	uom = frappe.get_doc("Item",item_code).stock_uom

# 	get_qty_pending_order = frappe.db.sql("""
# 		SELECT
# 		SUM(por.`qty_sisa`)

# 		FROM `tabPending Order` po
# 		JOIN `tabPending Order Roll` por
# 		ON po.`name` = por.`parent`
# 		WHERE po.`docstatus` < 2
# 		AND por.`docstatus` < 2
# 		AND por.`item_code_roll` = "{}"
# 		AND por.`colour` = "{}"
# 		GROUP BY por.`item_code_roll`
# 		""".format(item_code, colour))

# 	get_qty_terkirim = frappe.db.sql("""
# 		SELECT
# 		SUM(por.`roll_qty`)

# 		FROM `tabPacking List Delivery` po
# 		JOIN `tabPacking List Delivery Data` por
# 		ON po.`name` = por.`parent`
# 		WHERE po.`docstatus` < 2
# 		AND por.`docstatus` < 2
# 		AND por.`item_code_roll` = "{}"
# 		AND por.`colour` = "{}"
# 		AND por.`yard_atau_meter_per_roll` = "{}"
# 		GROUP BY por.`item_code_roll`
# 		""".format(item_code, colour, yard_atau_meter_per_roll))

# 	get_qty_dialokasi = frappe.db.sql("""
# 		SELECT
# 		SUM(por.`qty_sisa`)

# 		FROM `tabOrder Processing` po
# 		JOIN `tabOrder Processing Summary Roll` por
# 		ON po.`name` = por.`parent`
# 		WHERE po.`docstatus` < 2
# 		AND por.`docstatus` < 2
# 		AND por.`item_code_roll` = "{}"
# 		AND por.`colour` = "{}"
# 		AND por.`yard_atau_meter` = "{}"
# 		GROUP BY por.`item_code_roll`
# 		""".format(item_code, colour, yard_atau_meter_per_roll))

# 	get_qty_inventory = frappe.db.sql("""
# 		SELECT
# 		SUM(di.`total_roll`)
# 		FROM `tabData Inventory` di
# 		WHERE di.`item_code_variant` = "{}"
# 		AND di.`colour` = "{}"
# 		AND di.`yard_atau_meter_per_roll` = "{}"
# 		GROUP BY di.`item_code_variant`
# 		""".format(item_code, colour, yard_atau_meter_per_roll))


# 	if get_qty_pending_order :
# 		qty_pending_order = float(get_qty_pending_order[0][0])
# 	else :
# 		qty_pending_order = 0

# 	if get_qty_terkirim :
# 		qty_terkirim = float(get_qty_terkirim[0][0])
# 	else :
# 		qty_terkirim = 0

# 	if get_qty_dialokasi :
# 		qty_dialokasi = float(get_qty_dialokasi[0][0])
# 	else :
# 		qty_dialokasi = 0

# 	if get_qty_inventory :
# 		qty_inventory = float(get_qty_inventory[0][0])
# 	else :
# 		qty_inventory = 0

# 	send_data = []
# 	if qty_terkirim == 0 :
# 		temp_qty_terkirim = 0
# 	else :
# 		temp_qty_terkirim = qty_terkirim

# 	if qty_dialokasi == 0 :
# 		temp_qty_dialokasi = 0
# 	else :
# 		temp_qty_dialokasi = qty_dialokasi - temp_qty_terkirim


# 	if qty_pending_order == 0 :
# 		temp_qty_pending_order = 0
# 	else :
# 		temp_qty_pending_order = qty_pending_order - temp_qty_dialokasi




# 	if qty_inventory == 0 :
# 		temp_qty_inventory = 0
# 	else :
# 		temp_qty_inventory = qty_inventory - temp_qty_dialokasi

# 	send_data.append(str(temp_qty_pending_order))
# 	send_data.append(str(temp_qty_dialokasi))
# 	send_data.append(str(temp_qty_terkirim))
# 	send_data.append(str(temp_qty_inventory))

# 	return send_data




# # group tool

# # repack
# @frappe.whitelist()
# def projected_stock_by_item_group_tool(item_code, colour, yard_atau_meter_per_roll):
# 	uom = frappe.get_doc("Item",item_code).stock_uom
	
# 	qty_pending_order = 0
# 	qty_terkirim = 0
# 	qty_dialokasi = 0
# 	qty_inventory = 0

# 	get_qty_pending_order = frappe.db.sql("""
# 		SELECT
# 		SUM(por.`qty_sisa`)

# 		FROM `tabPending Order` po
# 		JOIN `tabPending Order Roll` por
# 		ON po.`name` = por.`parent`
# 		WHERE po.`docstatus` < 2
# 		AND por.`docstatus` < 2
# 		AND por.`item_code_roll` = "{}"
# 		AND por.`colour` = "{}"
# 		GROUP BY por.`item_code_roll`
# 		""".format(item_code, colour))

# 	get_qty_terkirim = frappe.db.sql("""
# 		SELECT
# 		SUM(por.`roll_qty`)

# 		FROM `tabPacking List Delivery` po
# 		JOIN `tabPacking List Delivery Data` por
# 		ON po.`name` = por.`parent`
# 		WHERE po.`docstatus` < 2
# 		AND por.`docstatus` < 2
# 		AND por.`item_code_roll` = "{}"
# 		AND por.`colour` = "{}"
# 		AND por.`yard_atau_meter_per_roll` = "{}"
# 		GROUP BY por.`item_code_roll`
# 		""".format(item_code, colour, yard_atau_meter_per_roll))

# 	get_qty_dialokasi = frappe.db.sql("""
# 		SELECT
# 		SUM(por.`qty_sisa`)

# 		FROM `tabOrder Processing` po
# 		JOIN `tabOrder Processing Summary Roll` por
# 		ON po.`name` = por.`parent`
# 		WHERE po.`docstatus` < 2
# 		AND por.`docstatus` < 2
# 		AND por.`item_code_roll` = "{}"
# 		AND por.`colour` = "{}"
# 		AND por.`yard_atau_meter` = "{}"
# 		GROUP BY por.`item_code_roll`
# 		""".format(item_code, colour, yard_atau_meter_per_roll))

# 	get_qty_inventory = frappe.db.sql("""
# 		SELECT
# 		SUM(di.`total_roll`)
# 		FROM `tabData Inventory` di
# 		WHERE di.`item_code_variant` = "{}"
# 		AND di.`colour` = "{}"
# 		AND di.`yard_atau_meter_per_roll` = "{}"
# 		AND di.`group` is null
# 		GROUP BY di.`item_code_variant`
# 		""".format(item_code, colour, yard_atau_meter_per_roll))

# 	if get_qty_pending_order :
# 		qty_pending_order = float(get_qty_pending_order[0][0])
# 	else :
# 		qty_pending_order = 0

# 	if get_qty_terkirim :
# 		qty_terkirim = float(get_qty_terkirim[0][0])
# 	else :
# 		qty_terkirim = 0

# 	if get_qty_dialokasi :
# 		qty_dialokasi = float(get_qty_dialokasi[0][0])
# 	else :
# 		qty_dialokasi = 0

# 	if get_qty_inventory :
# 		qty_inventory = float(get_qty_inventory[0][0])
# 	else :
# 		qty_inventory = 0

# 	send_data = []

# 	if qty_terkirim == 0 :
# 		temp_qty_terkirim = 0
# 	else :
# 		temp_qty_terkirim = qty_terkirim

# 	if qty_dialokasi == 0 :
# 		temp_qty_dialokasi = 0
# 	else :
# 		temp_qty_dialokasi = qty_dialokasi - temp_qty_terkirim


# 	if qty_pending_order == 0 :
# 		temp_qty_pending_order = 0
# 	else :
# 		temp_qty_pending_order = qty_pending_order - temp_qty_dialokasi
	


# 	if qty_inventory == 0 :
# 		temp_qty_inventory = 0
# 	else :
# 		temp_qty_inventory = qty_inventory - temp_qty_dialokasi


# 	send_data.append(str(temp_qty_pending_order))
# 	send_data.append(str(temp_qty_dialokasi))
# 	send_data.append(str(temp_qty_terkirim))
# 	send_data.append(str(temp_qty_inventory))

# 	return send_data




# @frappe.whitelist()
# def projected_stock_by_colour_group_tool(item_code, colour, yard_atau_meter_per_roll):

# 	qty_pending_order = 0
# 	qty_terkirim = 0
# 	qty_dialokasi = 0
# 	qty_inventory = 0

# 	uom = frappe.get_doc("Item",item_code).stock_uom

# 	get_qty_pending_order = frappe.db.sql("""
# 		SELECT
# 		SUM(por.`qty_sisa`)

# 		FROM `tabPending Order` po
# 		JOIN `tabPending Order Roll` por
# 		ON po.`name` = por.`parent`
# 		WHERE po.`docstatus` < 2
# 		AND por.`docstatus` < 2
# 		AND por.`item_code_roll` = "{}"
# 		AND por.`colour` = "{}"
# 		GROUP BY por.`item_code_roll`
# 		""".format(item_code, colour))

# 	get_qty_terkirim = frappe.db.sql("""
# 		SELECT
# 		SUM(por.`roll_qty`)

# 		FROM `tabPacking List Delivery` po
# 		JOIN `tabPacking List Delivery Data` por
# 		ON po.`name` = por.`parent`
# 		WHERE po.`docstatus` < 2
# 		AND por.`docstatus` < 2
# 		AND por.`item_code_roll` = "{}"
# 		AND por.`colour` = "{}"
# 		AND por.`yard_atau_meter_per_roll` = "{}"
# 		GROUP BY por.`item_code_roll`
# 		""".format(item_code, colour, yard_atau_meter_per_roll))

# 	get_qty_dialokasi = frappe.db.sql("""
# 		SELECT
# 		SUM(por.`qty_sisa`)

# 		FROM `tabOrder Processing` po
# 		JOIN `tabOrder Processing Summary Roll` por
# 		ON po.`name` = por.`parent`
# 		WHERE po.`docstatus` < 2
# 		AND por.`docstatus` < 2
# 		AND por.`item_code_roll` = "{}"
# 		AND por.`colour` = "{}"
# 		AND por.`yard_atau_meter` = "{}"
# 		GROUP BY por.`item_code_roll`
# 		""".format(item_code, colour, yard_atau_meter_per_roll))

# 	get_qty_inventory = frappe.db.sql("""
# 		SELECT
# 		SUM(di.`total_roll`)
# 		FROM `tabData Inventory` di
# 		WHERE di.`item_code_variant` = "{}"
# 		AND di.`colour` = "{}"
# 		AND di.`yard_atau_meter_per_roll` = "{}"
# 		AND di.`group` is null
# 		GROUP BY di.`item_code_variant`
# 		""".format(item_code, colour, yard_atau_meter_per_roll))


# 	if get_qty_pending_order :
# 		qty_pending_order = float(get_qty_pending_order[0][0])
# 	else :
# 		qty_pending_order = 0

# 	if get_qty_terkirim :
# 		qty_terkirim = float(get_qty_terkirim[0][0])
# 	else :
# 		qty_terkirim = 0

# 	if get_qty_dialokasi :
# 		qty_dialokasi = float(get_qty_dialokasi[0][0])
# 	else :
# 		qty_dialokasi = 0

# 	if get_qty_inventory :
# 		qty_inventory = float(get_qty_inventory[0][0])
# 	else :
# 		qty_inventory = 0

# 	send_data = []
# 	if qty_terkirim == 0 :
# 		temp_qty_terkirim = 0
# 	else :
# 		temp_qty_terkirim = qty_terkirim

# 	if qty_dialokasi == 0 :
# 		temp_qty_dialokasi = 0
# 	else :
# 		temp_qty_dialokasi = qty_dialokasi - temp_qty_terkirim


# 	if qty_pending_order == 0 :
# 		temp_qty_pending_order = 0
# 	else :
# 		temp_qty_pending_order = qty_pending_order - temp_qty_dialokasi




# 	if qty_inventory == 0 :
# 		temp_qty_inventory = 0
# 	else :
# 		temp_qty_inventory = qty_inventory - temp_qty_dialokasi

# 	send_data.append(str(temp_qty_pending_order))
# 	send_data.append(str(temp_qty_dialokasi))
# 	send_data.append(str(temp_qty_terkirim))
# 	send_data.append(str(temp_qty_inventory))

# 	return send_data



# @frappe.whitelist()
# def projected_stock_by_yard_group_tool(item_code, colour, yard_atau_meter_per_roll):

# 	qty_pending_order = 0
# 	qty_terkirim = 0
# 	qty_dialokasi = 0
# 	qty_inventory = 0

# 	uom = frappe.get_doc("Item",item_code).stock_uom

# 	get_qty_pending_order = frappe.db.sql("""
# 		SELECT
# 		SUM(por.`qty_sisa`)

# 		FROM `tabPending Order` po
# 		JOIN `tabPending Order Roll` por
# 		ON po.`name` = por.`parent`
# 		WHERE po.`docstatus` < 2
# 		AND por.`docstatus` < 2
# 		AND por.`item_code_roll` = "{}"
# 		AND por.`colour` = "{}"
# 		GROUP BY por.`item_code_roll`
# 		""".format(item_code, colour))

# 	get_qty_terkirim = frappe.db.sql("""
# 		SELECT
# 		SUM(por.`roll_qty`)

# 		FROM `tabPacking List Delivery` po
# 		JOIN `tabPacking List Delivery Data` por
# 		ON po.`name` = por.`parent`
# 		WHERE po.`docstatus` < 2
# 		AND por.`docstatus` < 2
# 		AND por.`item_code_roll` = "{}"
# 		AND por.`colour` = "{}"
# 		AND por.`yard_atau_meter_per_roll` = "{}"
# 		GROUP BY por.`item_code_roll`
# 		""".format(item_code, colour, yard_atau_meter_per_roll))

# 	get_qty_dialokasi = frappe.db.sql("""
# 		SELECT
# 		SUM(por.`qty_sisa`)

# 		FROM `tabOrder Processing` po
# 		JOIN `tabOrder Processing Summary Roll` por
# 		ON po.`name` = por.`parent`
# 		WHERE po.`docstatus` < 2
# 		AND por.`docstatus` < 2
# 		AND por.`item_code_roll` = "{}"
# 		AND por.`colour` = "{}"
# 		AND por.`yard_atau_meter` = "{}"
# 		GROUP BY por.`item_code_roll`
# 		""".format(item_code, colour, yard_atau_meter_per_roll))

# 	get_qty_inventory = frappe.db.sql("""
# 		SELECT
# 		SUM(di.`total_roll`)
# 		FROM `tabData Inventory` di
# 		WHERE di.`item_code_variant` = "{}"
# 		AND di.`colour` = "{}"
# 		AND di.`yard_atau_meter_per_roll` = "{}"
# 		AND di.`group` is null
# 		GROUP BY di.`item_code_variant`
# 		""".format(item_code, colour, yard_atau_meter_per_roll))


# 	if get_qty_pending_order :
# 		qty_pending_order = float(get_qty_pending_order[0][0])
# 	else :
# 		qty_pending_order = 0

# 	if get_qty_terkirim :
# 		qty_terkirim = float(get_qty_terkirim[0][0])
# 	else :
# 		qty_terkirim = 0

# 	if get_qty_dialokasi :
# 		qty_dialokasi = float(get_qty_dialokasi[0][0])
# 	else :
# 		qty_dialokasi = 0

# 	if get_qty_inventory :
# 		qty_inventory = float(get_qty_inventory[0][0])
# 	else :
# 		qty_inventory = 0

# 	send_data = []
# 	if qty_terkirim == 0 :
# 		temp_qty_terkirim = 0
# 	else :
# 		temp_qty_terkirim = qty_terkirim

# 	if qty_dialokasi == 0 :
# 		temp_qty_dialokasi = 0
# 	else :
# 		temp_qty_dialokasi = qty_dialokasi - temp_qty_terkirim


# 	if qty_pending_order == 0 :
# 		temp_qty_pending_order = 0
# 	else :
# 		temp_qty_pending_order = qty_pending_order - temp_qty_dialokasi




# 	if qty_inventory == 0 :
# 		temp_qty_inventory = 0
# 	else :
# 		temp_qty_inventory = qty_inventory - temp_qty_dialokasi

# 	send_data.append(str(temp_qty_pending_order))
# 	send_data.append(str(temp_qty_dialokasi))
# 	send_data.append(str(temp_qty_terkirim))
# 	send_data.append(str(temp_qty_inventory))

# 	return send_data