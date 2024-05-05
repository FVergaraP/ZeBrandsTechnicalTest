CREATE TABLE IF NOT EXISTS `users` (
    `email` varchar(100) PRIMARY KEY NOT NULL UNIQUE,
    `full_name` varchar(250) NOT NULL,
    `password` varchar(250) NOT NULL,
    `access_token` varchar(250) NULL,
    `superadmin` boolean default false,
    `disable` boolean default false
);

INSERT INTO `users` (`email`, `full_name`, `password`, `superadmin`) VALUES ('tpogacar@giro.it', 'Tadej Pogacar', '$2b$12$T64sPBGjyf6nIxHe5y74a.vHTYx4sTEu1aYASWeXpyzpVsDzRcsrO', 1);

CREATE TABLE IF NOT EXISTS `products` (
    `sku` varchar(100) PRIMARY KEY NOT NULL UNIQUE,
    `name` varchar(250) NOT NULL,
    `price` real NOT NULL,
    `brand` varchar(250) NOT NULL,
    `deleted` boolean default false

);

INSERT INTO `products`(`sku`,`name`,`price`,`brand`) VALUES ('212121', 'Colchon Signature', 29000, 'Luuna')