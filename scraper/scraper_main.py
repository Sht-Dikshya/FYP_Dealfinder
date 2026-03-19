import os
import sys
import django
import requests
from bs4 import BeautifulSoup
from decimal import Decimal
import time

# Ensure we can import the django project
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import Store, Category, Brand, Product, ProductPrice

def get_or_create_store(name, url):
    store, created = Store.objects.get_or_create(
        name=name,
        defaults={'website_url': url}
    )
    return store

def fetch_jeevee_products():
    """
    Mock/Template for Jeevee Scraper.
    Actual implementation would use Selenium or their internal API,
    because Jeevee is heavily JS relying.
    """
    print("Scraping Jeevee...")
    store = get_or_create_store('Jeevee', 'https://jeevee.com/')
    
    # Example simulated data
    products = [
        {'name': 'CeraVe Moisturizing Cream', 'brand': 'CeraVe', 'category': 'Skincare', 'price': 2500, 'discounted_price': 2300, 'url': 'https://jeevee.com/product/cerave-cream'},
        {'name': 'Maybelline Fit Me Foundation', 'brand': 'Maybelline', 'category': 'Makeup', 'price': 1500, 'discounted_price': 1400, 'url': 'https://jeevee.com/product/maybelline-fitme'},
    ]
    
    save_products(products, store)
    
def fetch_daraz_products():
    """
    Mock/Template for Daraz Scraper.
    Daraz requires handling of dynamic content and pagination.
    """
    print("Scraping Daraz...")
    store = get_or_create_store('Daraz', 'https://daraz.com.np/')
    
    # Example simulated data
    products = [
        {'name': 'CeraVe Moisturizing Cream', 'brand': 'CeraVe', 'category': 'Skincare', 'price': 2500, 'discounted_price': 2400, 'url': 'https://daraz.com.np/products/cerave-cream'},
        {'name': 'Maybelline Fit Me Foundation', 'brand': 'Maybelline', 'category': 'Makeup', 'price': 1500, 'discounted_price': 1350, 'url': 'https://daraz.com.np/products/maybelline-fitme'},
    ]
    
    save_products(products, store)


def save_products(scraped_data, store):
    for item in scraped_data:
        category, _ = Category.objects.get_or_create(
            name=item['category'], 
            defaults={'slug': item['category'].lower().replace(' ', '-')}
        )
        
        brand, _ = Brand.objects.get_or_create(
            name=item['brand']
        )
        
        product, _ = Product.objects.get_or_create(
            name=item['name'],
            category=category,
            brand=brand
        )
        
        # Add or update price
        ProductPrice.objects.update_or_create(
            product=product,
            store=store,
            defaults={
                'price': Decimal(item['price']),
                'discounted_price': Decimal(item['discounted_price']) if item.get('discounted_price') else None,
                'product_url': item['url']
            }
        )
        print(f"Saved price for {product.name} at {store.name}")

if __name__ == "__main__":
    fetch_jeevee_products()
    fetch_daraz_products()
    print("Scraping completed.")
