import frappe

frappe.whitelist(allow_guest=true)
    def get_emoji():
        return "😎"

def get_conditions_for_vehicle():
    return "1=1"