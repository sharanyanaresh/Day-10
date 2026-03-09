from collections import defaultdict

# Product catalog with 15 products
catalog = {
    'SKU001': {'name': 'Laptop', 'price': 65000, 'category': 'electronics', 'stock': 15, 'rating': 4.5, 'tags': ['computer', 'work']},
    'SKU002': {'name': 'Headphones', 'price': 2000, 'category': 'electronics', 'stock': 30, 'rating': 4.2, 'tags': ['audio', 'music']},
    'SKU003': {'name': 'Smartphone', 'price': 40000, 'category': 'electronics', 'stock': 10, 'rating': 4.6, 'tags': ['mobile', 'tech']},
    'SKU004': {'name': 'Tablet', 'price': 25000, 'category': 'electronics', 'stock': 5, 'rating': 4.4, 'tags': ['tech', 'portable']},

    'SKU005': {'name': 'T-shirt', 'price': 800, 'category': 'clothing', 'stock': 50, 'rating': 3.9, 'tags': ['casual', 'cotton']},
    'SKU006': {'name': 'Jeans', 'price': 1500, 'category': 'clothing', 'stock': 25, 'rating': 4.1, 'tags': ['denim', 'casual']},
    'SKU007': {'name': 'Jacket', 'price': 3000, 'category': 'clothing', 'stock': 0, 'rating': 4.3, 'tags': ['winter', 'fashion']},
    'SKU008': {'name': 'Sneakers', 'price': 2500, 'category': 'clothing', 'stock': 12, 'rating': 4.2, 'tags': ['shoes', 'fashion']},

    'SKU009': {'name': 'Novel', 'price': 500, 'category': 'books', 'stock': 40, 'rating': 4.8, 'tags': ['fiction', 'reading']},
    'SKU010': {'name': 'Python Book', 'price': 900, 'category': 'books', 'stock': 20, 'rating': 4.7, 'tags': ['programming', 'learning']},
    'SKU011': {'name': 'Cookbook', 'price': 700, 'category': 'books', 'stock': 15, 'rating': 4.0, 'tags': ['food', 'recipe']},

    'SKU012': {'name': 'Chocolate', 'price': 150, 'category': 'food', 'stock': 100, 'rating': 4.6, 'tags': ['sweet', 'snack']},
    'SKU013': {'name': 'Coffee', 'price': 400, 'category': 'food', 'stock': 60, 'rating': 4.5, 'tags': ['drink', 'energy']},
    'SKU014': {'name': 'Biscuits', 'price': 120, 'category': 'food', 'stock': 80, 'rating': 4.1, 'tags': ['snack', 'tea']},
    'SKU015': {'name': 'Protein Bar', 'price': 200, 'category': 'food', 'stock': 0, 'rating': 3.8, 'tags': ['health', 'snack']}
}


# Search products by tag
def search_by_tag(tag):
    tag_groups = defaultdict(list)

    for sku, product in catalog.items():
        for t in product.get("tags", []):
            tag_groups[t].append(product.get("name"))

    return tag_groups.get(tag, [])


# Find out of stock products
def out_of_stock():
    return {
        sku: product
        for sku, product in catalog.items()
        if product.get("stock", 0) == 0
    }


# Filter products by price range
def price_range(min_price, max_price):
    return {
        sku: product
        for sku, product in catalog.items()
        if min_price <= product.get("price", 0) <= max_price
    }


# Generate category summary
def category_summary():
    category_data = defaultdict(list)

    for product in catalog.values():
        category = product.get("category")
        category_data[category].append(product)

    summary = {}

    for cat, products in category_data.items():
        count = len(products)

        avg_price = sum(p.get("price", 0) for p in products) / count
        avg_rating = sum(p.get("rating", 0) for p in products) / count

        summary[cat] = {
            "count": count,
            "avg_price": avg_price,
            "avg_rating": avg_rating
        }

    return summary


# Apply discount to a category
def apply_discount(category, percent):
    for sku, product in catalog.items():
        if product.get("category") == category:
            price = product.get("price", 0)
            product["price"] = price * (1 - percent / 100)

    return catalog


# Merge two catalogs
def merge_catalogs(catalog1, catalog2):
    return catalog1 | catalog2


# Example function calls
if __name__ == "__main__":

    print("Search by tag 'snack':")
    print(search_by_tag("snack"))

    print("\nOut of stock products:")
    print(out_of_stock())

    print("\nProducts between ₹100 and ₹1000:")
    print(price_range(100, 1000))

    print("\nCategory summary:")
    print(category_summary())