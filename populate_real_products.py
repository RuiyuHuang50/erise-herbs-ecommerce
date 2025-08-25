#!/usr/bin/env python
import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from store.models import Product, Category
from decimal import Decimal

def clear_existing_products():
    """Clear existing products to start fresh"""
    Product.objects.all().delete()
    print("Cleared existing products")

def populate_real_products():
    """Populate database with real Erise Herbs products"""
    
    # Get or create categories
    herbal_extracts, _ = Category.objects.get_or_create(
        name='Herbal Extracts',
        defaults={'slug': 'herbal-extracts'}
    )
    fisetin_category, _ = Category.objects.get_or_create(
        name='Fisetin/Urolithin A',
        defaults={'slug': 'fisetin-urolithin-a'}
    )
    
    # Real products from Erise Herbs website
    products_data = [
        {
            'title': 'Acai Extract – 4:1',
            'category': herbal_extracts,
            'description': 'Acai Extract from Euterpe oleracea, found in Central and South America. Rich in antioxidants, vitamins, and minerals with potential benefits for heart and skin health, as well as aiding digestion. Often considered a superfood.',
            'price': Decimal('89.99'),
            'image': 'static/media/images/Acia-Berry.webp',
            'slug': 'acai-extract-4-1'
        },
        {
            'title': 'Ashwagandha Extract – Withanoloids 2.5%',
            'category': herbal_extracts,
            'description': 'Ashwagandha from Withania somnifera, native to India and Southeast Asia. Renowned for its calming effects, widely used to alleviate stress and anxiety. Studies suggest it can enhance energy levels.',
            'price': Decimal('79.99'),
            'image': 'media/images/Ashwagandha-Extract.webp',
            'slug': 'ashwagandha-extract-withanoloids-25'
        },
        {
            'title': 'American Ginseng – Ginsenosides 10%',
            'category': herbal_extracts,
            'description': 'American Ginseng from Panax quinquefolius, found in eastern North America. Believed to enhance immune function, increase energy levels, lower blood sugar and cholesterol levels.',
            'price': Decimal('99.99'),
            'image': 'media/images/American-Ginseng.webp',
            'slug': 'american-ginseng-ginsenosides-10'
        },
        {
            'title': 'Echinacea Purpurea Extract – 4% Flavones',
            'category': herbal_extracts,
            'description': 'Echinacea Purpurea (purple coneflower) from North America. Dietary supplement for common cold and infections. Stimulates immune system and aids in wound healing.',
            'price': Decimal('69.99'),
            'image': 'media/images/Echinacea-Purpurea-Extract.webp',
            'slug': 'echinacea-purpurea-extract-4-flavones'
        },
        {
            'title': 'Matcha – Straight Powder',
            'category': herbal_extracts,
            'description': 'Matcha from Camellia sinensis, native to Japan. Known for energizing properties. Contains catechins - potent antioxidants that may help maintain hormonal balance.',
            'price': Decimal('59.99'),
            'image': 'media/images/Matcha.webp',
            'slug': 'matcha-straight-powder'
        },
        {
            'title': 'Pomegranate Extract – 10:1',
            'category': herbal_extracts,
            'description': 'Pomegranate Extract from Punica Granatum, native to Middle East. Rich in antioxidants including ellagic acid and anthocyanins. Known for anti-inflammatory and anti-aging benefits.',
            'price': Decimal('84.99'),
            'image': 'media/images/Pomegranate-Powder.webp',
            'slug': 'pomegranate-extract-10-1'
        },
        {
            'title': 'Broccoli Extract – 20:1',
            'category': herbal_extracts,
            'description': 'Broccoli Extract from Brassica Oleracea Italica, Mediterranean plant. Enhances digestion, fights stomach ulcers, lowers cholesterol. Anti-inflammatory properties improve brain health.',
            'price': Decimal('74.99'),
            'image': 'media/images/Broccoli-Extract.webp',
            'slug': 'broccoli-extract-20-1'
        },
        {
            'title': 'Dandelion – Straight Powder',
            'category': herbal_extracts,
            'description': 'Dandelion (Taraxacum) from Eurasia. Known for diuretic properties, stimulates appetite and digestion. Detoxifying abilities, aids in relieving constipation. Packed with antioxidants.',
            'price': Decimal('49.99'),
            'image': 'media/images/Dandelion.webp',
            'slug': 'dandelion-straight-powder'
        },
        {
            'title': 'Aloe Vera – Straight Powder',
            'category': herbal_extracts,
            'description': 'Aloe Vera from Aloe Barbadensis, found in Saudi Arabia, Yemen, and Oman. Known for soothing and healing properties. Has antioxidant and anti-inflammatory effects.',
            'price': Decimal('54.99'),
            'image': 'media/images/Aloe-Vera-Extract.webp',
            'slug': 'aloe-vera-straight-powder'
        },
        {
            'title': 'Buckthorn Bark – Straight Powder',
            'category': herbal_extracts,
            'description': 'Buckthorn Bark from Rhamnus frangula, native to Eurasia. Commonly known as a laxative. Used to alleviate digestive issues, particularly constipation and hemorrhoids.',
            'price': Decimal('64.99'),
            'image': 'media/images/Buckthorn-Bark.webp',
            'slug': 'buckthorn-bark-straight-powder'
        },
        {
            'title': 'Elderberry Fruit – Straight Powder',
            'category': herbal_extracts,
            'description': 'Elderberry from Sambucus, native to Mexico and Central America. Used for boosting immune system. Effective for treating colds, influenza, and H1N1 flu.',
            'price': Decimal('69.99'),
            'image': 'media/images/Elderberry.webp',
            'slug': 'elderberry-fruit-straight-powder'
        },
        {
            'title': 'Amla Extract – Tannins 40%',
            'category': herbal_extracts,
            'description': 'Amla Extract from Emblica officinalis, native to India, Nepal, Sri Lanka, and Pakistan. Rich in tannins with antioxidant properties. Supports immune system and healthy hair.',
            'price': Decimal('79.99'),
            'image': 'media/images/Amla-Extract.webp',
            'slug': 'amla-extract-tannins-40'
        },
        {
            'title': 'Burdock – Straight Powder',
            'category': herbal_extracts,
            'description': 'Burdock root vegetable from Europe and Northern Asia. Stronger antioxidant activity than common vegetables. Used as diuretic and blood purifier.',
            'price': Decimal('59.99'),
            'image': 'media/images/Burdock.webp',
            'slug': 'burdock-straight-powder'
        },
        {
            'title': 'Andrographis Extract – Andrographolides 10%',
            'category': herbal_extracts,
            'description': 'Andrographis from Andrographis Paniculata, native to India and Sri Lanka. Alleviates sore throats, coughs, bronchitis, colds, flu, and upper respiratory infections.',
            'price': Decimal('89.99'),
            'image': 'media/images/Andrographis.webp',
            'slug': 'andrographis-extract-andrographolides-10'
        },
        {
            'title': 'Cactus Extract – 12:1',
            'category': herbal_extracts,
            'description': 'Cactus Extract from Cactaceae family, found throughout America. Benefits include managing diabetes, high cholesterol, obesity. Excellent source of vitamin C.',
            'price': Decimal('74.99'),
            'image': 'media/images/Cactus-Extract.webp',
            'slug': 'cactus-extract-12-1'
        },
        {
            'title': 'Fenugreek – Straight Powder',
            'category': herbal_extracts,
            'description': 'Fenugreek from Trigonella foenum-graecum, native to Iran. Helps regulate blood sugar levels, enhance testosterone production, and reduce cholesterol levels.',
            'price': Decimal('49.99'),
            'image': 'media/images/Fenugreek.webp',
            'slug': 'fenugreek-straight-powder'
        },
        {
            'title': 'Artichoke Extract – 4:1',
            'category': herbal_extracts,
            'description': 'Artichoke Extract from Cynara scolymus, found in Italy, Spain, France, and Greece. Supports digestive health, liver function, cholesterol regulation.',
            'price': Decimal('69.99'),
            'image': 'media/images/Artichoke-Extract.webp',
            'slug': 'artichoke-extract-4-1'
        },
        {
            'title': 'Fennel Seed Extract – 10:1',
            'category': herbal_extracts,
            'description': 'Fennel Seed Extract from Foeniculum vulgare Mill, found in Egypt, India, and Turkey. Stimulates digestive juices, anti-inflammatory properties.',
            'price': Decimal('64.99'),
            'image': 'media/images/Fennel-Seed-Extract.webp',
            'slug': 'fennel-seed-extract-10-1'
        },
        {
            'title': 'Bacopa Extract – Bacosides 50% UV',
            'category': herbal_extracts,
            'description': 'Bacopa from Bacopa Monnieri, found in India, Nepal, Sri Lanka, China, Taiwan, and Vietnam. Enhances memory, learning, and mental clarity.',
            'price': Decimal('94.99'),
            'image': 'media/images/Bacopa.webp',
            'slug': 'bacopa-extract-bacosides-50-uv'
        },
        {
            'title': 'Ginger Extract – Gingerol 1%',
            'category': herbal_extracts,
            'description': 'Ginger Extract from Zingiber Officinale. Known for anti-inflammatory properties, aids digestion, relieves nausea, and provides pain relief.',
            'price': Decimal('59.99'),
            'image': 'media/images/Ginger-Root.webp',
            'slug': 'ginger-extract-gingerol-1'
        },
        {
            'title': 'Garlic Extract – 1%',
            'category': herbal_extracts,
            'description': 'Garlic Extract from Allium sativum. Used to lower cholesterol levels and reduce blood pressure. Eliminates infections and combats viruses.',
            'price': Decimal('54.99'),
            'image': 'media/images/Garlic-Powder.webp',
            'slug': 'garlic-extract-1'
        },
        {
            'title': 'Camu Camu Extract – Vitamin C 8%',
            'category': herbal_extracts,
            'description': 'Camu Camu Extract from Myrciaria dubia, native to Brazil. Anti-inflammatory and blood sugar-lowering properties. High concentration of Vitamin C.',
            'price': Decimal('84.99'),
            'image': 'media/images/Camu-Camu-Extract.webp',
            'slug': 'camu-camu-extract-vitamin-c-8'
        },
        {
            'title': 'Chamomile Extract – 10:1',
            'category': herbal_extracts,
            'description': 'Chamomile Extract from Matricaria recutita, native to Europe, Africa, and Asia. Digestive relaxant to alleviate gastrointestinal issues.',
            'price': Decimal('64.99'),
            'image': 'media/images/Chamomile-Extract.webp',
            'slug': 'chamomile-extract-10-1'
        },
        {
            'title': 'Fisetin',
            'category': fisetin_category,
            'description': 'Turn back the clock on aging with Fisetin, the new anti-aging weapon backed by science. High purity fisetin from Japanese Knotwood. Clinically-tested to fight age-related decline.',
            'price': Decimal('129.99'),
            'image': 'media/images/Fennel-Seed-Extract.webp',  # Using available image
            'slug': 'fisetin'
        },
        {
            'title': 'Urolithin A',
            'category': fisetin_category,
            'description': 'Experience greater energy and cognition with Urolithin A. Boosts mitochondrial health to energize cells and sharpen mind. Activates mitophagy for improved cellular health.',
            'price': Decimal('149.99'),
            'image': 'media/images/Buckthorn-Bark.webp',  # Using available image
            'slug': 'urolithin-a'
        },
    ]
    
    # Create products
    created_count = 0
    for product_data in products_data:
        try:
            product, created = Product.objects.get_or_create(
                title=product_data['title'],
                defaults=product_data
            )
            if created:
                print(f"Created: {product.title}")
                created_count += 1
            else:
                print(f"Already exists: {product.title}")
        except Exception as e:
            print(f"Error creating {product_data['title']}: {e}")
    
    print(f"\nTotal new products created: {created_count}")
    print(f"Total products in database: {Product.objects.count()}")

if __name__ == '__main__':
    clear_existing_products()
    populate_real_products()
