frappe.ui.form.on("Contact Group", {
  refresh: function (frm) {
    // Add a custom button
    frm.add_custom_button(__("Send Email"), function () {
      frappe.prompt(
        {
          fieldtype: "Link",
          label: __("Email Template"),
          fieldname: "email_template",
          options: "Email Template",
          reqd: true,
        },
        (value) => {
          frm.call("send_emails", value);
        }
      );
    });
  },
});
