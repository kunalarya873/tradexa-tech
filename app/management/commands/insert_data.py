import threading
import json
from django.core.management.base import BaseCommand
from app.models import User, Product, Order

# Define the path to the JSON file
DATA_FILE_PATH = "data.json"

def load_data():
    """Load data from the JSON file."""
    with open(DATA_FILE_PATH, "r") as file:
        return json.load(file)

def insert_users(users):
    for user in users:
        User.objects.using('users').create(**user)

def insert_products(products):
    for product in products:
        Product.objects.using('products').create(**product)

def insert_orders(orders):
    for order in orders:
        Order.objects.using('orders').create(**order)

class Command(BaseCommand):
    help = "Insert data into multiple databases concurrently"

    def handle(self, *args, **kwargs):
        # Load data from the JSON file
        data = load_data()

        # Create threads for concurrent insertion
        user_thread = threading.Thread(target=insert_users, args=(data['users'],))
        product_thread = threading.Thread(target=insert_products, args=(data['products'],))
        order_thread = threading.Thread(target=insert_orders, args=(data['orders'],))

        # Start threads
        user_thread.start()
        product_thread.start()
        order_thread.start()

        # Wait for threads to complete
        user_thread.join()
        product_thread.join()
        order_thread.join()

        self.stdout.write(self.style.SUCCESS("Data inserted successfully!"))
