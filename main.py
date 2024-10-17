import shop
import shop.api_provider
import shop.order_processor

if __name__ == "__main__":
    api_provider = shop.api_provider.ApiProvider()
    payments_api = api_provider.get_payments_api()
    orders_api = api_provider.get_orders_api()
    catalog_api = api_provider.get_catalog_api()

    order_processor = shop.order_processor.OrderProcessor(
        payments_api, orders_api, catalog_api
    )
    orders_dict = {}
    for order_id in order_processor.get_list_of_orders():
        print(f"Processing order: {order_id}")
        list_products = order_processor.get_sku_and_qty_list(order_id)
        for product in list_products:
            print(f"SKU and quantity: {product}")