import frappe

def execute():
    vehicles = frappe.get_all('Vehicle', pluck= "name")
    for v in vehicles:
        vehicle_doc = frappe.get_doc('Vehicle', v)
        vehicle_doc.set_title()
        vehicle_doc.save()
