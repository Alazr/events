frappe.ui.form.on("Email Group", {
  refresh: function (frm) {
    // Add a custom button
    frm.add_custom_button(__("Send Email"), function () {
      frappe.msgprint("Button clicked!");
    });
  },
});
