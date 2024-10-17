class OrderProcessor:
    def __init__(self, payments_api, orders_api, catalog_api):
        self.payments_api = payments_api
        self.orders_api = orders_api
        self.catalog_api = catalog_api

    def get_list_of_orders(self):
        query_result = self.payments_api.list_payments()
        result = []
        if query_result.is_success():
            for payment in query_result.body["payments"]:
                if payment["status"] == "COMPLETED":
                    result.append(payment["order_id"])
            return result
        elif query_result.is_error():
            for error in query_result.errors:
                print(error["category"])
                print(error["code"])
                print(error["detail"])
            return []

    def get_sku_and_qty_list(self, order_id):
        query_result = self.orders_api.retrieve_order(order_id)
        if query_result.is_success():
            order = query_result.body["order"]
            result = []
            for item in order["line_items"]:
                qty = item["quantity"]
                sku = self.get_sku(item["catalog_object_id"])
                result.append((sku, qty))
            return result
        elif query_result.is_error():
            for error in query_result.errors:
                print(error["category"])
                print(error["code"])
                print(error["detail"])
            return []

    def get_sku(self, catalog_object_id):
        query_result = self.catalog_api.retrieve_catalog_object(catalog_object_id)
        if query_result.is_success():
            return query_result.body["object"]["item_variation_data"]["sku"]
        elif query_result.is_error():
            for error in query_result.errors:
                print(error["category"])
                print(error["code"])
                print(error["detail"])
            return ""
