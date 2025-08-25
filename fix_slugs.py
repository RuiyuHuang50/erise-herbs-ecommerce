#!/usr/bin/env python
import os
import sys
import django
from django.utils.text import slugify

# Add the project directory to Python path
sys.path.append('/Users/mac/Downloads/dev/ecommerce')

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from store.models import Product

def generate_slugs():
    """Generate slugs for products that don't have them"""
    
    # Get products with empty slugs
    products_without_slugs = Product.objects.filter(slug='')
    
    print(f"Found {products_without_slugs.count()} products without slugs")
    
    updated_count = 0
    
    for product in products_without_slugs:
        # Generate slug from title
        base_slug = slugify(product.title)
        slug = base_slug
        
        # Ensure slug is unique
        counter = 1
        while Product.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        
        # Update the product
        product.slug = slug
        product.save()
        
        print(f"Updated: {product.title} -> slug: '{slug}'")
        updated_count += 1
    
    print(f"\nTotal products updated: {updated_count}")
    
    # Verify no more empty slugs
    remaining_empty = Product.objects.filter(slug='').count()
    print(f"Remaining products with empty slugs: {remaining_empty}")

if __name__ == "__main__":
    generate_slugs()
