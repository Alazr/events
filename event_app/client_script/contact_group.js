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
          frm.call("send_emails", value, function () {
            frappe.show_alert({
              message: __(
                `${value.email_template} sent successfully to the ${cur_frm.doc.name}`
              ),
              indicator: "green",
              disappear_after: 3,
            });
          });
        }
      );
    });
  },

  before_save: function (frm) {
    frm.new_document = frm.doc.__islocal ? true : false;
  },

  after_save: function (frm) {
    if (frm.new_document) {
      frm.save_alert = false;

      frappe.show_alert({
        message: __(`${frm.doc.group_name} created successfully`),
        indicator: "green",
        disappear_after: 3,
      });
    }
  },
});
