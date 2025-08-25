#!/usr/bin/env python
"""
Script to populate the database with Erise Herbs products
Run this with: python populate_products.py
"""
import os
import sys
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from store.models import Category, Product

def create_categories():
    """Create product categories"""
    categories = [
        {'name': 'Herbal Extracts & Powders', 'slug': 'herbal-extracts-powders'},
        {'name': 'Fisetin/Urolithin A', 'slug': 'fisetin-urolithin-a'},
        {'name': 'Immune Support', 'slug': 'immune-support'},
        {'name': 'Digestive Health', 'slug': 'digestive-health'},
        {'name': 'Antioxidant Blends', 'slug': 'antioxidant-blends'},
    ]
    
    for cat_data in categories:
        category, created = Category.objects.get_or_create(
            slug=cat_data['slug'],
            defaults={'name': cat_data['name']}
        )
        if created:
            print(f"Created category: {category.name}")
        else:
            print(f"Category already exists: {category.name}")

def create_products():
    """Create products from Erise Herbs catalog"""
    
    # Get categories
    herbal_cat = Category.objects.get(slug='herbal-extracts-powders')
    fisetin_cat = Category.objects.get(slug='fisetin-urolithin-a')
    immune_cat = Category.objects.get(slug='immune-support')
    digestive_cat = Category.objects.get(slug='digestive-health')
    antioxidant_cat = Category.objects.get(slug='antioxidant-blends')
    
    products = [
        {
            'title': 'Acai Extract – 4:1',
            'brand': 'Erise Herbs',
            'description': 'This plant, found in Central and South America, including countries like Brazil, Peru, Colombia, and Venezuela, is rich in antioxidants, vitamins, and minerals. It has potential benefits for heart and skin health, as well as aiding digestion.',
            'slug': 'acai-extract-4-1',
            'price': 29.99,
            'category': antioxidant_cat,
            'image': 'images/acai-extract.jpg'
        },
        {
            'title': 'Ashwagandha Extract – Withanoloids 2.5%',
            'brand': 'Erise Herbs',
            'description': 'Ashwagandha, a plant native to India and Southeast Asia, is renowned for its calming effects and numerous health benefits. It is widely used to alleviate stress and anxiety, not only in women but also in men.',
            'slug': 'ashwagandha-extract-withanoloids',
            'price': 34.99,
            'category': herbal_cat,
            'image': 'images/ashwagandha-extract.jpg'
        },
        {
            'title': 'Echinacea Purpurea Extract – 4% Flavones',
            'brand': 'Erise Herbs',
            'description': 'Echinacea, a North American herb, is a dietary supplement for the common cold and other infections. It\'s believed to stimulate the immune system, enhancing its ability to combat infections.',
            'slug': 'echinacea-purpurea-extract',
            'price': 24.99,
            'category': immune_cat,
            'image': 'images/echinacea-extract.jpg'
        },
        {
            'title': 'American Ginseng – Ginsenosides 10%',
            'brand': 'Erise Herbs',
            'description': 'This plant, found in eastern North America, has been studied for its potential health benefits. It is believed to enhance immune function, aiding the body in fighting off infections and diseases.',
            'slug': 'american-ginseng-ginsenosides',
            'price': 39.99,
            'category': immune_cat,
            'image': 'images/american-ginseng.jpg'
        },
        {
            'title': 'Turmeric Extract – Curcumin 95%',
            'brand': 'Erise Herbs',
            'description': 'High-potency turmeric extract standardized to 95% curcumin. Known for its powerful anti-inflammatory and antioxidant properties, supporting joint health and overall wellness.',
            'slug': 'turmeric-extract-curcumin',
            'price': 32.99,
            'category': herbal_cat,
            'image': 'images/turmeric-extract.jpg'
        },
        {
            'title': 'Ginger Extract – Gingerol 1%',
            'brand': 'Erise Herbs',
            'description': 'This plant, known for its anti-inflammatory properties, aids digestion, relieves nausea, and provides pain relief. It\'s rich in antioxidants and may support the immune system.',
            'slug': 'ginger-extract-gingerol',
            'price': 22.99,
            'category': digestive_cat,
            'image': 'images/ginger-extract.jpg'
        },
        {
            'title': 'Bacopa Extract – Bacosides 50% UV',
            'brand': 'Erise Herbs',
            'description': 'This herb, found in India, Nepal, Sri Lanka, China, Taiwan, and Vietnam, has been traditionally used to enhance memory, learning, and mental clarity. It is rich in bacosides, which provide neuroprotection.',
            'slug': 'bacopa-extract-bacosides',
            'price': 28.99,
            'category': herbal_cat,
            'image': 'images/bacopa-extract.jpg'
        },
        {
            'title': 'Elderberry Fruit – Straight Powder',
            'brand': 'Erise Herbs',
            'description': 'This herb, native to Mexico and Central America, extending to Panama, is widely used for boosting the immune system. It is effective in treating common colds, influenza, and H1N1 flu.',
            'slug': 'elderberry-fruit-powder',
            'price': 26.99,
            'category': immune_cat,
            'image': 'images/elderberry-fruit.jpg'
        },
        {
            'title': 'Fisetin',
            'brand': 'Erise Herbs',
            'description': 'Turn back the clock on aging with Fisetin, the new anti-aging weapon backed by science. High purity fisetin from Japanese Knotwood, clinically-tested to fight age-related decline.',
            'slug': 'fisetin',
            'price': 49.99,
            'category': fisetin_cat,
            'image': 'images/fisetin.jpg'
        },
        {
            'title': 'Urolithin A',
            'brand': 'Erise Herbs',
            'description': 'Get ready to experience greater energy and cognition with Urolithin. This revolutionary supplement boosts mitochondrial health to energize your cells and sharpen your mind.',
            'slug': 'urolithin-a',
            'price': 89.99,
            'category': fisetin_cat,
            'image': 'images/urolithin-a.jpg'
        },
        {
            'title': 'Garlic Extract – 1%',
            'brand': 'Erise Herbs',
            'description': 'This herb, commonly used to lower cholesterol levels and reduce blood pressure, relaxes blood vessels for individuals with high blood pressure. Garlic also eliminates infections and combats viruses.',
            'slug': 'garlic-extract',
            'price': 18.99,
            'category': herbal_cat,
            'image': 'images/garlic-extract.jpg'
        },
        {
            'title': 'Pomegranate Extract – 10:1',
            'brand': 'Erise Herbs',
            'description': 'This plant, native to the Middle East, particularly Iran and Iraq, is rich in antioxidants, including ellagic acid and anthocyanins, which are known for their potential anti-inflammatory and anti-aging benefits.',
            'slug': 'pomegranate-extract',
            'price': 31.99,
            'category': antioxidant_cat,
            'image': 'images/pomegranate-extract.jpg'
        }
    ]
    
    for product_data in products:
        product, created = Product.objects.get_or_create(
            slug=product_data['slug'],
            defaults=product_data
        )
        if created:
            print(f"Created product: {product.title}")
        else:
            print(f"Product already exists: {product.title}")

def main():
    print("Starting to populate database with Erise Herbs products...")
    create_categories()
    print("\n" + "="*50 + "\n")
    create_products()
    print("\nDatabase population completed!")
    print(f"Total categories: {Category.objects.count()}")
    print(f"Total products: {Product.objects.count()}")

if __name__ == "__main__":
    main()
