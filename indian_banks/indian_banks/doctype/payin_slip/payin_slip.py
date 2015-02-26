# Copyright (c) 2013, sa and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from frappe.model.document import Document
import frappe
from frappe import _
from frappe.utils import comma_and


class PayinSlip(Document):
	def before_print(self):
		jvs_not_submitted = frappe.db.sql("""
        SELECT name FROM `tabJournal Voucher`
        WHERE name IN ({jvs}) and docstatus != 1
        """.format(jvs=', '.join(['"{}"'.format(d.jv) for d in self.payin_slip_details])))

		if jvs_not_submitted:
			frappe.throw(_("JV's needs to be submitted before they can be printed. Following are not \n{}").format(
				comma_and([result[0] for result in jvs_not_submitted]))
			)