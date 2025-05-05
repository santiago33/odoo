from odoo.tests.common import TransactionCase


class TestASOrder(TransactionCase):

    def setUp(self):
        super().setUp()
        # Створюємо партнера
        self.product = self.env['product.template'].create({
            'name': 'Test Product',
        })
        self.product2 = self.env['product.template'].create({
            'name': 'Test Product 2',
        })
        self.partner = self.env['res.partner'].create({
            'name': 'Test Partner',
        })
        # Створюємо автомобіль
        self.vehicle = self.env['as.vehicle'].create({
            'license_plate': 'KA7777KA',
            'partner_id': self.partner.id,
        })
        # Створюємо замовлення
        self.order = self.env['as.order'].create({
            'partner_id': self.partner.id,
            'vehicle_id': self.vehicle.id,
            'date_start': '2025-04-28 10:00:00',
        })
        # Створюємо елементи замовлення
        self.item1 = self.env['as.order.item'].create({
            'order_id': self.order.id,
            'product_id': self.product.id,
            'price': 100,
            'qty': 1,
        })
        self.item2 = self.env['as.order.item'].create({
            'order_id': self.order.id,
            'product_id': self.product2.id,
            'price': 200,
            'qty': 1,
        })

    def test_compute_total_cost(self):
        self.order._compute_total_cost()
        self.assertEqual(float(self.order.total_cost), 300.0,
                         "Total cost should be the sum of item subtotals")
