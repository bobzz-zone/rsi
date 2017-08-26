// Copyright (c) 2016, myme and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Summary Pembelian"] = {
	"filters": [
		{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.add_days(frappe.datetime.get_today(), -7),
			"reqd": 1,
			"width": "60px"
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.get_today(),
			"reqd": 1,
			"width": "60px"
		},
		{
			"fieldname":"supplier",
			"label": "Supplier",
			"fieldtype": "Link",
			"options": "Supplier",
			"reqd": 0,
			"width": "60px"
		},
		{
			"fieldname":"warehouse",
			"label": "Warehouse",
			"fieldtype": "Link",
			"options": "Warehouse",
			"reqd": 0,
			"width": "60px"
		},
		{
			"fieldname":"remark",
			"label": "Remark",
			"fieldtype": "Data",
			"reqd": 0,
			"width": "60px"
		},
	]
}
