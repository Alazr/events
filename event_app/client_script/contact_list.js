frappe.listview_settings["Contact"] = {
  onload: function (list_view) {
    list_view.page.add_inner_button(__("Add to Contact Group"), function () {
      const selected_contacts = list_view.get_checked_items(true);

      if (selected_contacts.length === 0) {
        frappe.msgprint(__("No document is selected"));
      } else {
        frappe.prompt(
          {
            fieldtype: "Link",
            label: __("Contact Group"),
            fieldname: "contact_group",
            options: "Contact Group",
            reqd: true,
          },
          (value) => {
            frappe.call({
              method: "event_app.events.contact.add_to_contact_group",
              args: {
                group_name: value.contact_group,
                selected_contacts: selected_contacts,
              },
            });
          }
        );
      }
    });
  },
};
