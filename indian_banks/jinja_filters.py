from frappe.utils import data
import frappe


def get_debit_entry(entries):
	for entry in entries:
		if entry.debit > 0:
			return entry


def get_payslip_map(payment_details):
	jvs = [x.jv for x in payment_details]

	map = {}
	for jv in jvs:
		jv_object = frappe.get_doc("Journal Voucher", jv)
		for entry in jv_object.entries:
			if entry.credit > 0:
				map.setdefault(entry.account, [])
				map[entry.account].append(jv_object)
				break

	return map


def get_total_credit_for_jvs(jvs):
	return sum([x.total_credit for x in jvs])


def money_in_words(amount):
	return data.money_in_words(amount)