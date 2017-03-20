# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "rsi"
app_title = "rsi"
app_publisher = "myme"
app_description = "rsi"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "techinal@erpsonic.com"
app_license = "MIT"
doc_events = {
	"Stock Entry": {
		"validate": "rsi.rsi.doctype.custom_method.payment_entry_discount"
	}
}
# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/rsi/css/rsi.css"
# app_include_js = "/assets/rsi/js/rsi.js"

# include js, css files in header of web template
# web_include_css = "/assets/rsi/css/rsi.css"
# web_include_js = "/assets/rsi/js/rsi.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "rsi.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "rsi.install.before_install"
# after_install = "rsi.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "rsi.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events



# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"rsi.tasks.all"
# 	],
# 	"daily": [
# 		"rsi.tasks.daily"
# 	],
# 	"hourly": [
# 		"rsi.tasks.hourly"
# 	],
# 	"weekly": [
# 		"rsi.tasks.weekly"
# 	]
# 	"monthly": [
# 		"rsi.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "rsi.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "rsi.event.get_events"
# }

