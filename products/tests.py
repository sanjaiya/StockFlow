from django.test import TestCase


class StockFlowTests(TestCase):

    def test_home_page_loads(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_supplier_page_loads(self):
        response = self.client.get("/suppliers/")
        self.assertEqual(response.status_code, 200)

    def test_stock_page_loads(self):
        response = self.client.get("/stock/")
        self.assertEqual(response.status_code, 200)