#!/usr/bin/env python
import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from store.models import Product

# Mapping of product titles to image file names
product_image_mapping = {
    'Acai Extract – 4:1': 'Acia-Berry.webp',
    'Ashwagandha Extract – Withanoloids 2.5%': 'Ashwagandha-Extract.webp',
    'Echinacea Purpurea Extract – 4% Flavones': 'Echinacea-Purpurea-Extract.webp',
    'American Ginseng – Ginsenosides 10%': 'American-Ginseng.webp',
    'Turmeric Extract – Curcumin 95%': 'Cinnamon-Powder.webp',  # Using available image
    'Ginger Extract – Gingerol 1%': 'Ginger-Root.webp',
    'Bacopa Extract – Bacosides 50% UV': 'Bacopa.webp',
    'Elderberry Fruit – Straight Powder': 'Elderberry.webp',
    'Fisetin': 'Fennel-Seed-Extract.webp',  # Using available image
    'Urolithin A': 'Buckthorn-Bark.webp',  # Using available image
    'Garlic Extract – 1%': 'Garlic-Powder.webp',
    'Pomegranate Extract – 10:1': 'Pomegranate-Powder.webp',
}

def update_product_images():
    products = Product.objects.all()
    updated_count = 0
    
    for product in products:
        # Check if we have a matching image for this product
        if product.title in product_image_mapping:
            image_filename = product_image_mapping[product.title]
            # Update the image field to point to the correct path
            product.image = f'media/images/{image_filename}'
            product.save()
            print(f"Updated {product.title} with image: {image_filename}")
            updated_count += 1
        else:
            print(f"No image mapping found for: {product.title}")
    
    print(f"\nTotal products updated: {updated_count}")

if __name__ == '__main__':
    update_product_images()
