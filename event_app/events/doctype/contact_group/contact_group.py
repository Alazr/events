# Copyright (c) 2023, alazar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ContactGroup(Document):
	
	@frappe.whitelist()
	def send_emails(self,email_template):
		
		for contactData in self.contacts:
			doc = frappe.get_doc("Contact",contactData.contact)
			if doc.email_id:
				frappe.sendmail(recipients=[doc.email_id], subject="Test", as_markdown=False, content=frappe.db.get_value('Email Template',email_template,"response_html"), args=None)
				
