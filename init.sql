CREATE TABLE IF NOT EXISTS `users` (
    `email` varchar(100) PRIMARY KEY NOT NULL UNIQUE,
    `full_name` varchar(250) NOT NULL,
    `password` varchar(250) NOT NULL,
    `access_token` varchar(250) NULL,
    'disable' boolean default false
);

INSERT INTO `users` (`email`, `full_name`, `password`) VALUES ('tpogacar@giro.it', 'Tadej Pogacar', '12345678');
