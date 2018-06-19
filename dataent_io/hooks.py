# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "dataent_io"
app_title = "Dataent Framework"
app_publisher = "Dataent"
app_description = "dataent.io"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@dataent.io"
app_version = "0.0.1"

required_apps = ["dataent_theme"]

fixtures = ["Contact Us Settings", "Web Form"]

website_context = {
	"brand_html": "<img class='mr-2 d-inline-block align-top' src='/assets/dataent_theme/img/dataent-logo-white.svg' width='30px' height='30px' />Dataent",
	"top_bar_items": [
		{"label": "Products", "right": 1, "child_items": [
			{"label": "Dataent Framework", "url":"/dataent"},
			{"label": "EPAAS", "url":"/epaas"},
			{"label": "Bench", "url":"/bench"},
			{"label": "Gantt", "url":"/gantt"},
			{"label": "Charts", "url":"/charts"},
			{"label": "DataTable", "url":"/datatable"},
		]},
		{"label": "About", "right": 1, "child_items": [
			{"label": "Team", "url":"/about"},
			{"label": "Jobs", "url":"/jobs"},
			{"label": "Inspiration", "url":"/inspiration"},
			{"label": "Story", "url":"/story"},
			{"label": "Contact", "url":"/about#contact"},
		]},
		{"label": "Blog", "url":"/blog", "right": 1},
	],
	"favicon": "/assets/dataent_theme/img/dataent-logo.png",
	"hide_login": 1
}

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/dataent_io/css/dataent_io.css"
# app_include_js = "/assets/dataent_io/js/dataent_io.js"

# include js, css files in header of web template
# web_include_css = "/assets/dataent_io/css/dataent_io.css"
web_include_js = "/assets/dataent_io/js/docs.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "dataent_io.install.before_install"
# after_install = "dataent_io.install.after_install"

# Desk Notifications
# ------------------
# See dataent.core.notifications.get_notification_config

# notification_config = "dataent_io.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "dataent.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "dataent.desk.doctype.event.event.has_permission",
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
# 		"dataent_io.tasks.all"
# 	],
# 	"daily": [
# 		"dataent_io.tasks.daily"
# 	],
# 	"hourly": [
# 		"dataent_io.tasks.hourly"
# 	],
# 	"weekly": [
# 		"dataent_io.tasks.weekly"
# 	]
# 	"monthly": [
# 		"dataent_io.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "dataent_io.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"dataent.desk.doctype.event.event.get_events": "dataent_io.event.get_events"
# }
