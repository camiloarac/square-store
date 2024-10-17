import os
from square.client import Client

"""
ApiProvider class to interact with Square APIs.

This class initializes the Square client using the access token from the environment
and provides methods to access different Square API instances.

Attributes:
    client (Client): An instance of the Square Client initialized with the access token.

Methods:
    get_payments_api():
        Returns the Payments API instance from the Square client.
        
    get_orders_api():
        Returns the Orders API instance from the Square client.
        
    get_catalog_api():
        Returns the Catalog API instance from the Square client.
"""


class ApiProvider:
    def __init__(self):
        # Initialize the Square client
        self.client = Client(
            access_token=os.environ["SQUARE_ACCESS_TOKEN"], environment="production"
        )

    # Get the Payments API instance
    def get_payments_api(self):
        return self.client.payments

    # Get the Orders API instance
    def get_orders_api(self):
        return self.client.orders

    # Get the Catalog API instance
    def get_catalog_api(self):
        return self.client.catalog
