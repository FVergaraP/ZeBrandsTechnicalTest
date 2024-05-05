CREATE TABLE IF NOT EXISTS `users` (
    `email` varchar(100) PRIMARY KEY NOT NULL UNIQUE,
    `full_name` varchar(250) NOT NULL,
    `password` varchar(250) NOT NULL,
    `access_token` varchar(250) NULL,
    `superadmin` boolean default false,
    `disable` boolean default false
);

INSERT INTO `users` (`email`, `full_name`, `password`, `superadmin`) VALUES ('tpogacar@giro.it', 'Tadej Pogacar', '$2b$12$T64sPBGjyf6nIxHe5y74a.vHTYx4sTEu1aYASWeXpyzpVsDzRcsrO', 1);
