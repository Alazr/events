const add_custom_action = function (list_view) {
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
              message: __(`Selected contacts added to ${value.contact_group}`),
              indicator: "green",
              disappear_after: 3,
            });
          },
        });
      }
    );
  });
};
frappe.listview_settings["Contact"] = {
  onload: function (list_view) {
    add_custom_action(list_view);
  },
  refresh: function (list_view) {
    if (list_view.page.title === "Report: Contact") {
      const action_button = $(`.actions-btn-group`);

      setTimeout(() => {
        action_button.addClass("hide");
      }, 1);
      add_custom_action(list_view);
    }
  },
};
