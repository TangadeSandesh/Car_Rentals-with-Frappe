# Copyright (c) 2026, Sandesh and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):

	frappe.errprint("filters")

	columns = [{
		"fieldname": "make",
		"label": "Make",
		"fieldtype": "Data",
	}, {
		"fieldname": "total_revenue",
		"label": "Total Revenue",
		"fieldtype": "Currency",
	}]

	data = frappe.get_all(
	"Ride Booking", 
	fields=["sum(total_amount) as total_revenue","vehicle.make", "count(*)"], 
	filters={"docstatus":1}, 
	group_by="make")

	chart = {
		"data": {
			"labels": [row.make for row in data],
			"datasets": [{
				"name": "Total Revenue",
				"values": [row.total_revenue for row in data]
			}],
		},
		"type": "pie",				
	}

	return columns, data, "Here is the revenue by make", chart


def execute_snapshot_report(filters: dict | None = None):
	"""Return columns and data for the report.

	This is the main entry point for snapshot report. When 'Synced
	Report' is enabled in report, framework will call this method
	every time the report is refreshed or a filter is updated. It
	accepts the same filters as normal execute. But a utility method -
	get_latest_sync, is also imported.

	"""
	from frappe.database.duckdb.database import get_latest_sync

	columns, data = [], []
	return columns, data
