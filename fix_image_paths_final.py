#!/usr/bin/env python
import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from store.models import Product

def fix_image_paths_final():
    """Fix image paths to point directly to media/images/"""
    updated_count = 0
    
    for product in Product.objects.all():
        # Get current image path
        current_path = str(product.image)
        if 'static/media/images/' in current_path:
            # Extract just the filename
            filename = current_path.split('/')[-1]
            # Set the correct path for Django's MEDIA_URL
            product.image = f'images/{filename}'
            product.save()
            print(f"Updated {product.title} -> images/{filename}")
            updated_count += 1
    
    print(f"\nTotal products updated: {updated_count}")

if __name__ == '__main__':
    fix_image_paths_final()
