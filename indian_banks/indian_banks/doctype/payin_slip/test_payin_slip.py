# Copyright (c) 2013, sa and Contributors
# See license.txt

import unittest

import frappe


test_records = frappe.get_test_records('Payin Slip')


class TestPayinSlip(unittest.TestCase):
	pass
