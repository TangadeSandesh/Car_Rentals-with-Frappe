import frappe

@frappe.whitelist(allow_guest=True)
def get_emoji():
        return "😎"

def get_conditions_for_vehicle():
    return "1=1"

def send_payment_reminders():
    pass