
import frappe
from frappe.model.document import Document
import ast


@frappe.whitelist()
def add_to_contact_group(group_name,selected_contacts):
    contact_group= frappe.get_doc("Contact Group",group_name)
    contact_list = ast.literal_eval(selected_contacts)
    if len(contact_list):
        for contact_name in contact_list:
            contact = frappe.get_doc("Contact",contact_name)
            new_Group_member = frappe.new_doc("Contact Group Member")
            new_Group_member.contact = contact.name
            new_Group_member.parent = contact_group.name
            new_Group_member.parentfield="contacts"
            new_Group_member.parenttype="Contact Group"
            new_Group_member.insert()
            
    
    
		
				

	
	