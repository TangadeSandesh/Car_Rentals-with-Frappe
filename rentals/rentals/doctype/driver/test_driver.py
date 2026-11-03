# Copyright (c) 2026, Sandesh and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestDriver(FrappeTestCase):
	def test_full_name_correctly_set(self):
		test_driver = frappe.new_doc("Driver")
		test_driver.first_name = "John"
		test_driver.last_name = "Doe"
		test_driver.license_number = "ABC123"
		test_driver.save()

		self.assertEqual(test_driver.full_name, "John Doe")


	def test_full_name_correctly_set_when_last_name_not_set(self):
		test_driver = frappe.new_doc("Driver")
		test_driver.first_name = "John"
		test_driver.license_number = "ABC123"
		test_driver.save()

		self.assertEqual(test_driver.full_name, "John")