from . import __version__ as app_version

app_name = "frappe_gym"
app_title = "Frappe Gym"
app_publisher = "Warren Eiserman"
app_description = "Gym Management"
app_email = "frappe@agile.co.za"
app_license = "MIT"

# Set up the custom 404 page
website_catch_all = "not_found"

portal_menu_items = [
    {"title": "My Contracts", "route": "/contracts", "role": "Gym Member"},
    {"title": "Classes", "route": "/bookings", "role": "Gym Member"},
    {"title": "My Stats", "route": "/measurements", "role": "Gym Member"}

]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/frappe_gym/css/frappe_gym.css"
# app_include_js = "/assets/frappe_gym/js/frappe_gym.js"

# include js, css files in header of web template
# web_include_css = "/assets/frappe_gym/css/frappe_gym.css"
# web_include_js = "/assets/frappe_gym/js/frappe_gym.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "frappe_gym/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

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

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# "methods": "frappe_gym.utils.jinja_methods",
# "filters": "frappe_gym.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "frappe_gym.install.before_install"
# after_install = "frappe_gym.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "frappe_gym.uninstall.before_uninstall"
# after_uninstall = "frappe_gym.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "frappe_gym.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# "Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# "Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# "ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# "*": {
# "on_update": "method",
# "on_cancel": "method",
# "on_trash": "method"
# }
# }

doc_events = {
    "Class Booking": {
        "on_update": "frappe_gym.socketIO.new_class_booking"
    }
}


# Scheduled Tasks
# ---------------
# Run this every minute for testing purposes
scheduler_events = {
    "cron": {
        "* * * * *": ["frappe_gym.tasks.cron"]}
}


# Testing
# -------

# before_tests = "frappe_gym.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# "frappe.desk.doctype.event.event.get_events": "frappe_gym.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# "Task": "frappe_gym.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
# {
# "doctype": "{doctype_1}",
# "filter_by": "{filter_by}",
# "redact_fields": ["{field_1}", "{field_2}"],
# "partial": 1,
# },
# {
# "doctype": "{doctype_2}",
# "filter_by": "{filter_by}",
# "partial": 1,
# },
# {
# "doctype": "{doctype_3}",
# "strict": False,
# },
# {
# "doctype": "{doctype_4}"
# }
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# "frappe_gym.auth.validate"
# ]
