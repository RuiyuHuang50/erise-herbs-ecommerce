#!/usr/bin/env python
import os
import sys
import django
from decimal import Decimal

# Add the project directory to Python path
sys.path.append('/Users/mac/Downloads/dev/ecommerce')

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from store.models import Product, Category

def create_category_products():
    """Create products for empty categories"""
    
    # Get categories
    categories = {
        'Herbal Extracts & Powders': Category.objects.get(name='Herbal Extracts & Powders'),
        'Fisetin/Urolithin A': Category.objects.get(name='Fisetin/Urolithin A'),
        'Immune Support': Category.objects.get(name='Immune Support'),
        'Digestive Health': Category.objects.get(name='Digestive Health'),
        'Antioxidant Blends': Category.objects.get(name='Antioxidant Blends'),
    }
    
    # Products for Herbal Extracts & Powders
    herbal_products = [
        {
            'title': 'Ashwagandha Root Extract Powder',
            'brand': 'Erise Herbs',
            'description': 'Premium organic Ashwagandha root extract powder, standardized to 5% withanolides. Known for stress relief and adaptogenic properties.',
            'price': Decimal('29.99'),
            'image': 'ashwagandha_powder.jpg'
        },
        {
            'title': 'Turmeric Curcumin Extract Powder',
            'brand': 'Erise Herbs',
            'description': 'High-potency turmeric extract powder with 95% curcuminoids. Natural anti-inflammatory and antioxidant support.',
            'price': Decimal('24.99'),
            'image': 'turmeric_powder.jpg'
        },
        {
            'title': 'Reishi Mushroom Extract Powder',
            'brand': 'Erise Herbs',
            'description': 'Organic Reishi mushroom extract powder, standardized to 30% polysaccharides. Supports immune function and relaxation.',
            'price': Decimal('34.99'),
            'image': 'reishi_powder.jpg'
        },
        {
            'title': 'Rhodiola Rosea Extract Powder',
            'brand': 'Erise Herbs',
            'description': 'Siberian Rhodiola rosea extract powder, 3% rosavins and 1% salidroside. Adaptogenic herb for stress and fatigue.',
            'price': Decimal('39.99'),
            'image': 'rhodiola_powder.jpg'
        }
    ]
    
    # Products for Fisetin/Urolithin A
    fisetin_products = [
        {
            'title': 'Pure Fisetin 100mg Capsules',
            'brand': 'Erise Herbs',
            'description': 'High-purity fisetin extracted from Japanese wax tree. Powerful senolytic flavonoid for cellular health and longevity.',
            'price': Decimal('49.99'),
            'image': 'fisetin_capsules.jpg'
        },
        {
            'title': 'Urolithin A 250mg Capsules',
            'brand': 'Erise Herbs',
            'description': 'Bioavailable Urolithin A for mitochondrial health and muscle function. Supports cellular renewal and healthy aging.',
            'price': Decimal('79.99'),
            'image': 'urolithin_capsules.jpg'
        },
        {
            'title': 'Fisetin + Quercetin Complex',
            'brand': 'Erise Herbs',
            'description': 'Synergistic blend of fisetin and quercetin for enhanced senolytic activity and antioxidant protection.',
            'price': Decimal('44.99'),
            'image': 'fisetin_quercetin.jpg'
        }
    ]
    
    # Products for Immune Support
    immune_products = [
        {
            'title': 'Elderberry Extract Capsules',
            'brand': 'Erise Herbs',
            'description': 'Concentrated elderberry extract with vitamin C and zinc. Traditional immune support for seasonal wellness.',
            'price': Decimal('19.99'),
            'image': 'elderberry_capsules.jpg'
        },
        {
            'title': 'Echinacea Goldenseal Complex',
            'brand': 'Erise Herbs',
            'description': 'Powerful combination of echinacea and goldenseal root extracts. Classic herbal immune system support.',
            'price': Decimal('24.99'),
            'image': 'echinacea_goldenseal.jpg'
        },
        {
            'title': 'Turkey Tail Mushroom Extract',
            'brand': 'Erise Herbs',
            'description': 'Organic turkey tail mushroom extract, rich in PSK and PSP. Supports immune function and gut health.',
            'price': Decimal('32.99'),
            'image': 'turkey_tail.jpg'
        },
        {
            'title': 'Astragalus Root Extract',
            'brand': 'Erise Herbs',
            'description': 'Traditional Chinese astragalus root extract. Adaptogenic herb for immune resilience and energy.',
            'price': Decimal('27.99'),
            'image': 'astragalus_extract.jpg'
        }
    ]
    
    # Products for Digestive Health
    digestive_products = [
        {
            'title': 'Digestive Enzyme Complex',
            'brand': 'Erise Herbs',
            'description': 'Comprehensive blend of plant-based digestive enzymes including amylase, protease, and lipase for optimal digestion.',
            'price': Decimal('29.99'),
            'image': 'digestive_enzymes.jpg'
        },
        {
            'title': 'Slippery Elm Bark Powder',
            'brand': 'Erise Herbs',
            'description': 'Pure slippery elm bark powder for soothing digestive tract support. Traditional remedy for stomach comfort.',
            'price': Decimal('18.99'),
            'image': 'slippery_elm.jpg'
        },
        {
            'title': 'Marshmallow Root Extract',
            'brand': 'Erise Herbs',
            'description': 'Organic marshmallow root extract with mucilage compounds. Gentle digestive tract and throat support.',
            'price': Decimal('22.99'),
            'image': 'marshmallow_root.jpg'
        },
        {
            'title': 'Ginger Root Extract Capsules',
            'brand': 'Erise Herbs',
            'description': 'Concentrated ginger root extract, standardized to 5% gingerols. Supports healthy digestion and nausea relief.',
            'price': Decimal('16.99'),
            'image': 'ginger_extract.jpg'
        }
    ]
    
    # Products for Antioxidant Blends
    antioxidant_products = [
        {
            'title': 'Super Berry Antioxidant Blend',
            'brand': 'Erise Herbs',
            'description': 'Powerful blend of acai, goji, blueberry, and pomegranate extracts. Rich in anthocyanins and vitamin C.',
            'price': Decimal('34.99'),
            'image': 'berry_antioxidant.jpg'
        },
        {
            'title': 'Green Tea EGCG Complex',
            'brand': 'Erise Herbs',
            'description': 'Standardized green tea extract with 50% EGCG plus vitamin E and selenium for comprehensive antioxidant support.',
            'price': Decimal('26.99'),
            'image': 'green_tea_egcg.jpg'
        },
        {
            'title': 'Resveratrol + Grape Seed Extract',
            'brand': 'Erise Herbs',
            'description': 'Premium resveratrol from Japanese knotweed with grape seed proanthocyanidins. Cardiovascular and cellular protection.',
            'price': Decimal('42.99'),
            'image': 'resveratrol_grape.jpg'
        },
        {
            'title': 'Alpha Lipoic Acid Complex',
            'brand': 'Erise Herbs',
            'description': 'R-Alpha lipoic acid with vitamin C and E. Universal antioxidant for cellular energy and detoxification support.',
            'price': Decimal('38.99'),
            'image': 'alpha_lipoic.jpg'
        }
    ]
    
    # Create products for each category
    category_products = {
        'Herbal Extracts & Powders': herbal_products,
        'Fisetin/Urolithin A': fisetin_products,
        'Immune Support': immune_products,
        'Digestive Health': digestive_products,
        'Antioxidant Blends': antioxidant_products,
    }
    
    created_count = 0
    
    for category_name, products in category_products.items():
        category = categories[category_name]
        
        for product_data in products:
            # Check if product already exists
            if not Product.objects.filter(title=product_data['title']).exists():
                product = Product.objects.create(
                    title=product_data['title'],
                    brand=product_data['brand'],
                    description=product_data['description'],
                    price=product_data['price'],
                    image=product_data['image'],
                    category=category
                )
                print(f"Created: {product.title} in {category.name}")
                created_count += 1
            else:
                print(f"Skipped (already exists): {product_data['title']}")
    
    print(f"\nTotal products created: {created_count}")
    
    # Print final category counts
    print("\nFinal category distribution:")
    for cat in Category.objects.all():
        count = Product.objects.filter(category=cat).count()
        print(f'{cat.name}: {count} products')

if __name__ == "__main__":
    create_category_products()
