# Erise Herbs - Natural Wellness E-commerce Platform

A Django-based e-commerce platform inspired by [eriseherbs.com](https://eriseherbs.com/), specializing in natural plant extracts and herbal ingredients.

## 🌿 Features

- **Modern Design**: Clean, professional interface inspired by Erise Herbs
- **Product Management**: Full CRUD operations for products and categories
- **Shopping Cart**: Add, update, and remove items with real-time updates
- **User Authentication**: Registration, login, and profile management
- **Responsive Design**: Mobile-friendly and accessible across all devices
- **Admin Panel**: Django admin interface for easy management

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Django 5.0+
- pip (Python package manager)

### Installation

1. **Clone or navigate to the project directory:**

   ```bash
   cd /Users/mac/Downloads/dev/ecommerce
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Apply database migrations:**

   ```bash
   python manage.py migrate
   ```

4. **Create a superuser (optional):**

   ```bash
   python manage.py createsuperuser
   ```

5. **Collect static files:**

   ```bash
   python manage.py collectstatic --noinput
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver 8001
   ```

7. **Access the application:**
   - Main site: http://127.0.0.1:8001/
   - Admin panel: http://127.0.0.1:8001/admin/

## 📁 Project Structure

```
ecommerce/
├── ecommerce/          # Main project settings
├── store/              # Product catalog app
├── cart/               # Shopping cart functionality
├── account/            # User authentication
├── payment/            # Payment processing
├── static/             # CSS, JS, and static assets
├── templates/          # HTML templates
├── media/              # User uploaded files
└── manage.py           # Django management script
```

## 🎨 Design Features

### Color Scheme

- Primary Green: `#2d5a3d`
- Secondary Green: `#4a7c59`
- Accent Green: `#6fa574`
- Light Green: `#a8d5ba`
- Cream Background: `#f8f6f0`

### Key Components

- **Hero Section**: Gradient background with nature-inspired messaging
- **Product Cards**: Hover effects with smooth animations
- **Navigation**: Sticky header with dropdown categories
- **Footer**: Multi-column layout with contact info and certifications

## 📸 Adding Product Images

### Method 1: Django Admin Panel

1. Access the admin panel at http://127.0.0.1:8001/admin/
2. Login with your superuser credentials
3. Navigate to "Products" under the "Store" section
4. Click "Add Product" or edit an existing product
5. Upload images using the "Image" field
6. Save the product

### Method 2: Upload via File System

1. Create product image directories:

   ```bash
   mkdir -p static/media/images
   ```

2. Copy your product images to the directory:

   ```bash
   cp your-product-image.jpg static/media/images/
   ```

3. Update the product in Django admin or database to reference the image path

### Image Requirements

- **Format**: JPG, PNG, WebP
- **Size**: Recommended 800x800px minimum
- **Aspect Ratio**: Square (1:1) preferred for best display
- **File Size**: Under 2MB for optimal loading

### Sample Image Categories

For herb/wellness products, consider these image types:

- Product packaging shots
- Ingredient close-ups
- Lifestyle/usage images
- Before/after comparisons
- Certification badges

## 🛍️ Sample Product Data

To quickly populate your store, you can add these sample categories and products:

### Categories

- **Plant Extracts**
- **Essential Oils**
- **Herbal Supplements**
- **Natural Cosmetics**
- **Wellness Teas**

### Sample Products

1. **Ginkgo Biloba Extract**

   - Category: Plant Extracts
   - Price: $24.99
   - Description: Premium quality Ginkgo Biloba extract for cognitive support

2. **Lavender Essential Oil**
   - Category: Essential Oils
   - Price: $18.99
   - Description: Pure lavender oil for relaxation and aromatherapy

## 🔧 Customization

### Updating Brand Information

1. **Company Name**: Edit templates/base.html
2. **Contact Information**: Update footer section in base.html
3. **Colors**: Modify CSS variables in static/css/main.css
4. **Logo**: Replace favicon and logo references

### Adding New Features

The project is built with Django's modular structure, making it easy to add:

- Payment gateways
- Product reviews
- Wishlist functionality
- Email notifications
- Inventory management

## 🌐 Production Deployment

### Environment Variables

Create a `.env` file for production settings:

```env
DEBUG=False
SECRET_KEY=your-secret-key
DATABASE_URL=your-database-url
AWS_ACCESS_KEY_ID=your-aws-key
AWS_SECRET_ACCESS_KEY=your-aws-secret
```

### Static Files & Media

For production, configure:

- AWS S3 for media storage
- CDN for static files
- Database (PostgreSQL recommended)

## 📞 Support

For questions or support:

- Email: shally@eriseherbs.com
- Phone: (323) 849-6556

## 📄 License

This project is inspired by Erise Herbs and built for educational/commercial purposes.

---

**Empowering Wellness with Nature** 🌿
