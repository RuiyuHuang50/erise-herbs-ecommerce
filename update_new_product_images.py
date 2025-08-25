#!/usr/bin/env python
import os
import sys
import django

# Add the project directory to Python path
sys.path.append('/Users/mac/Downloads/dev/ecommerce')

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from store.models import Product

def update_product_images():
    """Update product images with appropriate URLs for each product type"""
    
    # Define product image mappings with high-quality, relevant images
    product_images = {
        # Herbal Extracts & Powders
        'Ashwagandha Root Extract Powder': 'https://images.unsplash.com/photo-1609840114035-3c981b782dfe?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',  # Ashwagandha roots
        'Turmeric Curcumin Extract Powder': 'https://images.unsplash.com/photo-1615485500704-8e990f9900f7?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',  # Turmeric powder
        'Reishi Mushroom Extract Powder': 'https://images.unsplash.com/photo-1518435935093-89f9b9a48b1f?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',  # Reishi mushrooms
        'Rhodiola Rosea Extract Powder': 'https://images.unsplash.com/photo-1544787219-7f47ccb76574?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',  # Mountain herbs
        
        # Fisetin/Urolithin A
        'Pure Fisetin 100mg Capsules': 'https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',  # White capsules
        'Urolithin A 250mg Capsules': 'https://images.unsplash.com/photo-1559757148-5c350d0d3c56?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',  # Clear capsules
        'Fisetin + Quercetin Complex': 'https://images.unsplash.com/photo-1471193945509-9ad0617afabf?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',  # Natural capsules
        
        # Immune Support
        'Elderberry Extract Capsules': 'https://images.unsplash.com/photo-1599665463123-e9bbac90c610?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',  # Elderberries
        'Echinacea Goldenseal Complex': 'https://images.unsplash.com/photo-1595121345037-27ff9ea67fcf?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',  # Echinacea flowers
        'Turkey Tail Mushroom Extract': 'https://images.unsplash.com/photo-1603184017968-953f59cd2e37?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',  # Turkey tail mushrooms
        'Astragalus Root Extract': 'https://images.unsplash.com/photo-1618556819263-9c7c533b4c34?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',  # Astragalus roots
        
        # Digestive Health
        'Digestive Enzyme Complex': 'https://images.unsplash.com/photo-1559181567-c3190ca9959b?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',  # Enzyme capsules
        'Slippery Elm Bark Powder': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',  # Tree bark
        'Marshmallow Root Extract': 'https://images.unsplash.com/photo-1578662996442-48f60103fc96?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',  # Marshmallow plant
        'Ginger Root Extract Capsules': 'https://images.unsplash.com/photo-1553166094-9db5cff0f3c4?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',  # Fresh ginger
        
        # Antioxidant Blends
        'Super Berry Antioxidant Blend': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',  # Mixed berries
        'Green Tea EGCG Complex': 'https://images.unsplash.com/photo-1556881286-62284d628e67?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',  # Green tea leaves
        'Resveratrol + Grape Seed Extract': 'https://images.unsplash.com/photo-1537640538966-79f369143f8f?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',  # Grapes
        'Alpha Lipoic Acid Complex': 'https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',  # ALA capsules
    }
    
    updated_count = 0
    
    for product_title, image_url in product_images.items():
        try:
            product = Product.objects.get(title=product_title)
            product.image = image_url
            product.save()
            print(f"Updated: {product_title}")
            updated_count += 1
        except Product.DoesNotExist:
            print(f"Product not found: {product_title}")
    
    print(f"\nTotal products updated: {updated_count}")
    
    # Show some examples of updated products
    print("\nSample of updated products:")
    sample_products = Product.objects.filter(title__in=list(product_images.keys())[:5])
    for product in sample_products:
        print(f"  - {product.title}: {product.image}")

if __name__ == "__main__":
    update_product_images()
