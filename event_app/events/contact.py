
import frappe
from frappe.model.document import Document
import ast
from frappe.integrations.utils import  make_request

@frappe.whitelist()
def add_to_contact_group(group_name,selected_contacts):
    contact_group= frappe.get_doc("Contact Group",group_name)
    contact_list = ast.literal_eval(selected_contacts)
    if len(contact_list):
        for contact_name in contact_list:
            contact = frappe.get_doc("Contact",contact_name)
            filtered_contacts= [i for i in contact_group.contacts if i.contact == contact.name]
            if not len(filtered_contacts):
                new_Group_member = frappe.new_doc("Contact Group Member")
                new_Group_member.contact = contact.name
                new_Group_member.parent = contact_group.name
                new_Group_member.parentfield="contacts"
                new_Group_member.parenttype="Contact Group"
                new_Group_member.insert()
               
           
            

@frappe.whitelist()
def update_contact_events():
    
    url="https://riekol-api.azurewebsites.net/api/member/detail"
    
    contacts = frappe.get_all("Contact")

    for contact in contacts:
        try:
            response = make_request("GET",f"{url}/{id}")
            user_data=response['userData']
            for e in user_data["deepDive"]:
                if not check_event_in_event_list(e,contact["deepdive"]):
                    new_deep_event = frappe.new_doc("Deep Dive Event")
                    new_deep_event._id =e._id,
                    new_deep_event.eventDate = e.eventDate
                    new_deep_event.speakerName = e.speakerName
                    new_deep_event.themeName = e.themeName
                    new_deep_event.topicName = e.topicName
                    new_deep_event.parent=contact.name
                    new_deep_event.parenttype = "Contact"
                    new_deep_event.parentfield = "deepdive"
                    new_deep_event.insert()
            for e in user_data["keyNote"]:
                if not check_event_in_event_list(e,contact["keynote"]):
                    new_key_note_event = frappe.new_doc("key Note Events")
                    new_key_note_event._id =e._id,
                    new_key_note_event.eventDate = e.eventDate
                    new_key_note_event.speakerName = e.speakerName
                    new_key_note_event.themeName = e.themeName
                    new_key_note_event.topicName = e.topicName
                    new_key_note_event.parent=contact.name
                    new_key_note_event.parenttype = "Contact"
                    new_key_note_event.parentfield = "keynote"
                    new_key_note_event.insert()
            for e in user_data["myEo"]:
                if not check_event_in_event_list(e,contact["myeo"]):
                    new_eo_event = frappe.new_doc("key Note Events")
                    new_eo_event._id =e._id,
                    new_eo_event.name = e.name
                    new_eo_event.eodate = e.eoDate
                    new_eo_event.parent=contact.name
                    new_eo_event.parenttype = "Contact"
                    new_eo_event.parentfield = "myeo"
                    new_eo_event.insert()
            
        
       
        except Exception as e:
            res = frappe.flags.integration_request.json()['error']
            error_message = res.get('error_user_msg', res.get("message"))
            frappe.throw(
                msg=error_message,
                title=res.get("error_user_title", "Error"),
            )
    



def check_event_in_event_list(event,event_list):
    for e in event_list:
        if e._id == event._id:
            return True
    return False