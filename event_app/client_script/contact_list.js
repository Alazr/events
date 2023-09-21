frappe.listview_settings["Contact"] = {
  onload: function (list_view) {
    list_view.page.add_action_item(__("Add to Contact Group"), function () {
      const selected_contacts = list_view.get_checked_items(true);

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
            callback: function () {
              frappe.show_alert({
                message: __(
                  `Selected contacts added to ${value.contact_group}`
                ),
                indicator: "green",
                disappear_after: 3,
              });
            },
          });
        }
      );
    });
  },
};
