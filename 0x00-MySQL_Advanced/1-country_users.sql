-- creates a table named `users` with four colums:
-- `id`, `email`, `name`, and `country`
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') DEFAULT 'US' NOT NULL,
    PRIMARY KEY (id)
);
