CREATE TABLE `Location` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name`	TEXT NOT NULL,
	`address`	TEXT NOT NULL
);

CREATE TABLE `Customer` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name`    TEXT NOT NULL,
    `address`    TEXT NOT NULL,
    `email`    TEXT NOT NULL,
    `password`    TEXT NOT NULL
);

CREATE TABLE `Animal` (
	`id`  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name`  TEXT NOT NULL,
	`status` TEXT NOT NULL,
	`breed` TEXT NOT NULL,
	`customer_id` INTEGER NOT NULL,
	`location_id` INTEGER,
	FOREIGN KEY(`customer_id`) REFERENCES `Customer`(`id`),
	FOREIGN KEY(`location_id`) REFERENCES `Location`(`id`)
);


CREATE TABLE `Employee` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name`	TEXT NOT NULL,
	`address`	TEXT NOT NULL,
	`location_id` INTEGER NOT NULL,
	FOREIGN KEY(`location_id`) REFERENCES `Location`(`id`)

);

INSERT INTO `Location` VALUES (null, 'Nashville North', "64 Washington Heights");
INSERT INTO `Location` VALUES (null, 'Nashville South', "101 Penn Ave");


INSERT INTO `Employee` VALUES (null, "Madi Peper", "35498 Madison Ave", 1);
INSERT INTO `Employee` VALUES (null, "Kristen Norris", "100 Main St", 1);
INSERT INTO `Employee` VALUES (null, "Meg Ducharme", "404 Unknown Ct", 2);
INSERT INTO `Employee` VALUES (null, "Hannah Hall", "204 Empty Ave", 1);
INSERT INTO `Employee` VALUES (null, "Leah Hoefling", "200 Success Way", 2);


INSERT INTO `Customer` VALUES (null, "Mo Silvera", "201 Created St", "mo@silvera.com", "password");
INSERT INTO `Customer` VALUES (null, "Bryan Nilsen", "500 Internal Error Blvd", "bryan@nilsen.com", "password");
INSERT INTO `Customer` VALUES (null, "Jenna Solis", "301 Redirect Ave", "jenna@solis.com", "password");
INSERT INTO `Customer` VALUES (null, "Emily Lemmon", "454 Mulberry Way", "emily@lemmon.com", "password");



INSERT INTO `Animal` VALUES (null, "Snickers", "Recreation", "Dalmation", 4, 1);
INSERT INTO `Animal` VALUES (null, "Jax", "Treatment", "Beagle", 1, 1);
INSERT INTO `Animal` VALUES (null, "Falafel", "Treatment", "Siamese", 4, 2);
INSERT INTO `Animal` VALUES (null, "Doodles", "Kennel", "Poodle", 3, 1);
INSERT INTO `Animal` VALUES (null, "Daps", "Kennel", "Boxer", 2, 2);
INSERT INTO `Animal` VALUES (null, "Cleo", "Kennel", "Poodle", 2, 2);
INSERT INTO `Animal` VALUES (null, "Popcorn", "Kennel", "Beagle", 3, 2);
INSERT INTO `Animal` VALUES (null, "Curly", "Treatment", "Poodle", 4, 2);

-- Get only the animal rows where the `id` field value is 3
SELECT
    a.id,
    a.name,
    a.breed,
    a.status,
    a.location_id,
    a.customer_id
FROM animal a
WHERE a.id = 8

SELECT
    a.id,
    a.name,
    a.address
FROM location a
WHERE a.id = 2

SELECT
    a.id,
    a.name
FROM customer a
WHERE a.id = 2

SELECT
    a.id,
    a.name
FROM employee a
WHERE a.id = 1

SELECT
    c.email
FROM customer c
WHERE c.email = "jenna@solis.com"

INSERT INTO `Animal` VALUES (null, "Daps", "Kennel", "Boxer", 2, 2);
INSERT INTO `Location` VALUES (null, 'Nashville South', "101 Penn Ave");
INSERT INTO `Employee` VALUES (null, "Leah Hoefling", "200 Success Way", 2);
INSERT INTO `Customer` VALUES (null, "Emily Lemmon", "454 Mulberry Way", "emily@lemmon.com", "password");

SELECT
    a.id,
    a.name,
    a.breed,
    a.customer_id pet_customer_id,
    a.status,
    a.location_id,
    l.name location_name,
    l.address location_address,
    c.id customer_id,
    c.name customer_name,
    c.address customer_address,
    c.email customer_email,
    c.password customer_password
FROM Animal a
LEFT JOIN Location l
    ON l.id = a.location_id
LEFT JOIN Customer c
    ON c.id = a.customer_id

SELECT 
    a.id,
    a.name,
    a.breed,
    a.customer_id pet_customer_id,
    a.status,
    a.location_id,
    c.id customer_id,
    c.name customer_name,
    c.address customer_address,
    c.email customer_email,
    c.password customer_password
FROM Animal a
LEFT JOIN Customer c
    ON c.id = a.customer_id

SELECT 
    e.id,
    e.name, 
    e.address,
    e.location_id,
    l.name location_name,
    l.address location_address
FROM employee e
LEFT JOIN Location l
    ON l.id = e.location_id



SELECT 
    l.id location,
    l.name, 
    l.address,
    a.name animal_name,
    a.location_id animal_location,
    e.name employee_name,
    e.location_id employee_location
FROM Location l
LEFT JOIN Animal a
    ON location = animal_location
LEFT JOIN Employee e
    ON location = employee_location


SELECT 
    l.id location,
    l.name, 
    l.address,
    a.name animal_name,
    a.location_id animal_location
FROM Location l
LEFT JOIN Animal a
    ON location = animal_location

SELECT 
    l.id location,
    l.name, 
    l.address,
    e.name employee_name,
    e.location_id employee_location
FROM Location l
LEFT JOIN Employee e
    ON location = employee_location
