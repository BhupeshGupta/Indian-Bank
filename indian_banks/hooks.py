app_name = "indian_banks"
app_title = "Indian Banks"
app_publisher = "sa"
app_description = "as"
app_icon = "octicon-zap"
app_color = "#ff8890"
app_email = "v@d.c"
app_version = "0.0.1"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/indian_banks/css/indian_banks.css"
# app_include_js = "/assets/indian_banks/js/indian_banks.js"

# include js, css files in header of web template
# web_include_css = "/assets/indian_banks/css/indian_banks.css"
# web_include_js = "/assets/indian_banks/js/indian_banks.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# "Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "indian_banks.install.before_install"
# after_install = "indian_banks.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "indian_banks.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# "Event": "frappe.core.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.core.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"indian_banks.tasks.all"
# 	],
# 	"daily": [
# 		"indian_banks.tasks.daily"
# 	],
# 	"hourly": [
# 		"indian_banks.tasks.hourly"
# 	],
# 	"weekly": [
# 		"indian_banks.tasks.weekly"
# 	]
# 	"monthly": [
# 		"indian_banks.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "indian_banks.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.core.doctype.event.event.get_events": "indian_banks.event.get_events"
# }

# doctype_js = {
#     "Account": ["indian_banks/journal_voucher_list.js"]
# }

doctype_list_js = {
"Journal Voucher": ["c_scripts/journal_voucher_list.js"]
}

jenv_filter = [
	'get_debit_entry:indian_banks.jinja_filters.get_debit_entry',
	'money_in_words:indian_banks.jinja_filters.money_in_words',
	'get_payslip_map:indian_banks.jinja_filters.get_payslip_map',
	'get_total_credit_for_jvs:indian_banks.jinja_filters.get_total_credit_for_jvs'
]