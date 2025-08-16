USE alx_book_store;

INSERT INTO authors (author_id, author_name) VALUES
(1, 'Chinua Achebe'),
(2, 'Chimamanda Ngozi Adichie'),
(3, 'Ngugi wa Thiong''o'),
(4, 'Ama Ata Aidoo'),
(5, 'Wole Soyinka');

INSERT INTO books (book_id, title, author_id, price, publication_date) VALUES
(1, 'Things Fall Apart', 1, 49.99, '1958-06-17'),
(2, 'Half of a Yellow Sun', 2, 59.50, '2006-09-12'),
(3, 'Weep Not, Child', 3, 39.95, '1964-01-01'),
(4, 'A Grain of Wheat', 3, 44.00, '1967-10-01'),
(5, 'Our Sister Killjoy', 4, 35.00, '1977-01-01'),
(6, 'The Interpreters', 5, 42.75, '1965-01-01'),
(7, 'Americanah', 2, 54.25, '2013-05-14'),
(8, 'Anthills of the Savannah', 1, 47.50, '1987-09-01');

INSERT INTO customers (customer_id, customer_name, email, address) VALUES
(1, 'Kofi Mensah', 'kofi.mensah@example.com', 'Accra, Ghana'),
(2, 'Ama Serwaa', 'ama.serwaa@example.com', 'Kumasi, Ghana'),
(3, 'John Doe', 'john.doe@example.com', 'Lagos, Nigeria'),
(4, 'Sarah Adebayo', 'sarah.adebayo@example.com', 'Abuja, Nigeria'),
(5, 'Kwame Nkrumah', 'kwame.nkrumah@example.com', 'Cape Coast, Ghana');

INSERT INTO orders (order_id, customer_id, order_date) VALUES
(1, 1, '2025-08-01'),
(2, 2, '2025-08-03'),
(3, 3, '2025-08-05'),
(4, 1, '2025-08-10'),
(5, 4, '2025-08-12'),
(6, 5, '2025-08-15');

INSERT INTO order_details (orderdetailid, order_id, book_id, quantity) VALUES
(1, 1, 1, 1),
(2, 1, 7, 1),
(3, 2, 2, 1),
(4, 2, 5, 2),
(5, 3, 3, 1),
(6, 3, 4, 1),
(7, 4, 8, 2),
(8, 4, 6, 1),
(9, 5, 7, 1),
(10, 6, 1, 1);
