🔐 1. Login & Signup System
Backend: ✔ REQUIRED
 Database: ✔ REQUIRED
Why?
You must store user data securely.


Backend handles:
Register user


Login authentication


Password hashing


Session / token management


Database stores:
User ID


Username


Email


Password (hashed)


Wishlist items



❤️ 2. Wishlist Feature
Backend: ✔ REQUIRED
 Database: ✔ REQUIRED
Why?
Wishlist must be saved per user.
Flow:
User clicks ❤️ → send request to backend


Backend saves product ID linked to user


Database:
user_id


product_id



🛒 3. Cart (if you implement real cart)
Backend: ✔ REQUIRED
 Database: ✔ REQUIRED
Even if it's simple:
Store selected items


Maintain user-specific cart



🔍 4. Search Functionality (Real Search)
Backend: ✔ REQUIRED
 Database: ✔ REQUIRED
Why?
You need to search across many products.
Backend:
Query database (LIKE / full-text search)


Database:
Product name


Brand


Category



💄 5. Product Listing (Category Pages)
Backend: ✔ REQUIRED
 Database: ✔ REQUIRED
Why?
Products should not be hardcoded.
Database stores:
Product name


Brand


Image URL


Category


Price


Store info


Backend:
Fetch products by category


Apply filters



🎯 6. Filters (Brand, Price, Store)
Backend: ✔ REQUIRED
 Database: ✔ REQUIRED
Backend:
Query with conditions:


WHERE brand = ?


WHERE price BETWEEN ?



⚖️ 7. Compare Products Page
Backend: ⚠ OPTIONAL (depends)
 Database: ✔ REQUIRED
Two options:
Option A (Simple – Frontend only):
JS calculates price


Data is static


Option B (Better – Backend):
Fetch real store prices


Calculate lowest price dynamically



🎉 8. Deals Page
Backend: ✔ REQUIRED
 Database: ✔ REQUIRED
Why?
Deals change frequently.
Database:
Discount %


Start time / End time


Backend:
Filter only active deals



🕷 9. Web Scraping (Daraz, Jeevee, Foreveryng)
Backend: ✔ REQUIRED (Python)
 Database: ✔ REQUIRED
Why?
Scraping runs on server


Data must be stored


Flow:
Python script scrapes → saves to MySQL


Django reads from DB → shows in UI



🧑‍💼 10. Admin Dashboard (Store Uploads)
Backend: ✔ REQUIRED
 Database: ✔ REQUIRED
Features:
Add product


Update price


Delete product

