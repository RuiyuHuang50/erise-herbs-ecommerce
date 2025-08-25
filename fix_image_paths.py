#!/usr/bin/env python
import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from store.models import Product

# Image mapping for products
image_mapping = {
    'Acai Extract – 4:1': 'Acia-Berry.webp',
    'Ashwagandha Extract – Withanoloids 2.5%': 'Ashwagandha-Extract.webp',
    'American Ginseng – Ginsenosides 10%': 'American-Ginseng.webp',
    'Echinacea Purpurea Extract – 4% Flavones': 'Echinacea-Purpurea-Extract.webp',
    'Matcha – Straight Powder': 'Matcha.webp',
    'Pomegranate Extract – 10:1': 'Pomegranate-Powder.webp',
    'Broccoli Extract – 20:1': 'Broccoli-Extract.webp',
    'Dandelion – Straight Powder': 'Dandelion.webp',
    'Aloe Vera – Straight Powder': 'Aloe-Vera-Extract.webp',
    'Buckthorn Bark – Straight Powder': 'Buckthorn-Bark.webp',
    'Elderberry Fruit – Straight Powder': 'Elderberry.webp',
    'Amla Extract – Tannins 40%': 'Amla-Extract.webp',
    'Burdock – Straight Powder': 'Burdock.webp',
    'Andrographis Extract – Andrographolides 10%': 'Andrographis.webp',
    'Cactus Extract – 12:1': 'Cactus-Extract.webp',
    'Fenugreek – Straight Powder': 'Fenugreek.webp',
    'Artichoke Extract – 4:1': 'Artichoke-Extract.webp',
    'Fennel Seed Extract – 10:1': 'Fennel-Seed-Extract.webp',
    'Bacopa Extract – Bacosides 50% UV': 'Bacopa.webp',
    'Ginger Extract – Gingerol 1%': 'Ginger-Root.webp',
    'Garlic Extract – 1%': 'Garlic-Powder.webp',
    'Camu Camu Extract – Vitamin C 8%': 'Camu-Camu-Extract.webp',
    'Chamomile Extract – 10:1': 'Chamomile-Extract.webp',
}

def fix_image_paths():
    """Fix image paths for all products"""
    updated_count = 0
    
    for product in Product.objects.all():
        if product.title in image_mapping:
            # Set the correct image path
            image_filename = image_mapping[product.title]
            product.image = f'static/media/images/{image_filename}'
            product.save()
            print(f"Updated {product.title} -> {image_filename}")
            updated_count += 1
        else:
            print(f"No image mapping for: {product.title}")
    
    print(f"\nTotal products updated: {updated_count}")

if __name__ == '__main__':
    fix_image_paths()
