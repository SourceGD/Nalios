-- On crée les tables

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    price NUMERIC(10,2) NOT NULL,
    creation_date DATE NOT NULL
);

CREATE TABLE categories (
    category_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    is_public BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE product_categories (
    product_id INT NOT NULL REFERENCES products(product_id),
    category_id INT NOT NULL REFERENCES categories(category_id),
    PRIMARY KEY (product_id, category_id)
);


-- test en insert des données

-- Produits
INSERT INTO products (name, price, creation_date) VALUES
('Laptop', 1200.00, '2025-01-15'),
('Mouse', 25.50, '2025-02-10'),
('Keyboard', 45.00, '2025-03-05'),
('Monitor', 300.00, '2025-01-20');

-- Categories
INSERT INTO categories (name, is_public) VALUES
('Electronics', TRUE),
('Computer Accessories', TRUE),
('Office', TRUE),
('Gaming', TRUE),
('Private Deals', FALSE),
('New Arrivals', TRUE),
('On Sale', TRUE),
('Premium', TRUE);

-- on lie les produits aux categories
-- Laptop
INSERT INTO product_categories (product_id, category_id) VALUES
(1,1),(1,4),(1,6),(1,7),(1,8); -- 5

-- Mouse
INSERT INTO product_categories (product_id, category_id) VALUES
(2,2),(2,3),(2,4),(2,7),(2,5); -- 4 + 1 privée

-- Keyboard
INSERT INTO product_categories (product_id, category_id) VALUES
(3,2),(3,3),(3,7),(3,6),(3,8),(3,1); -- 6

-- Monitors
INSERT INTO product_categories (product_id, category_id) VALUES
(4,1),(4,4),(4,7); -- 3

-- requête bonus => products that belong to more than 5 public categories : Nous devrions obtenir que les Keyboards ( ok ! )

SELECT p.product_id, p.name, COUNT(pc.category_id) AS public_category_count
FROM products p
JOIN product_categories pc ON p.product_id = pc.product_id
JOIN categories c ON pc.category_id = c.category_id
WHERE c.is_public = TRUE
GROUP BY p.product_id, p.name
HAVING COUNT(pc.category_id) > 5;