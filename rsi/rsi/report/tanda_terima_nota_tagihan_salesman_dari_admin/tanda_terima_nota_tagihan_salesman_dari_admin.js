// Copyright (c) 2016, myme and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Tanda Terima Nota Tagihan Salesman dari Admin"] = {
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
			"fieldname":"sales",
			"label": "Sales",
			"fieldtype": "Link",
			"options": "Sales",
			"reqd": 1,
			"width": "60px"
		},
	]
}
