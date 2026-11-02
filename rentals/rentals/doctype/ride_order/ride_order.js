// Copyright (c) 2026, Sandesh and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Order", {
    onload(frm) {
        console.log("running load.....");
    },
    setup(frm) {
        console.log("running setup.....");
    },
	refresh(frm) {
        console.log("running refresh.....");

        if (frm.doc.status === "New") {
            frm.add_custom_button("Accept", () => {
                // frappw.show_alert("Ride Accepted")
                frm.set_value("status", "Accepted")
                frm.save();
	        }, "Actions")

            frm.add_custom_button("Reject", () => {
                // frappw.show_alert("Ride Accepted")
                frm.set_value("status", "Rejected")
                frm.save();
	        }, "Actions") 
        }
    },
    status(frm){
        console.log("Status is changed to: " + frm.doc.status);
	},
});
