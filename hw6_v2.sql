CREATE SCHEMA HW6_v2;

USE  HW6_v2; 


CREATE TABLE login(
	userName VARCHAR (30) NOT NULL, 
    userPw VARCHAR (30) NOT NULL,
    PRIMARY KEY (userName)); 
    
CREATE TABLE accounts(
	userName VARCHAR (30) NOT NULL, 
    accountNumber VARCHAR(8) NOT NULL,
    actualName VARCHAR (40) NOT NULL, 
    balance DOUBLE,
    PRIMARY KEY (accountNumber), 
    UNIQUE KEY (userName),
	CONSTRAINT FK_userName FOREIGN KEY (userName) REFERENCES login(userName)
    ); 

INSERT INTO login VALUES('mr.rooney', 'D@y_0ff'); 
INSERT INTO accounts VALUES('mr.rooney', 81659231, 'Ferris Bueller', 8156.57); 

INSERT INTO login VALUES('calvin_klein', '0ut@T!me');
INSERT INTO accounts VALUES('calvin_klein', 65122348, 'Marty McFly', 56894.83); 

INSERT INTO login VALUES('Wyld', 'Exce11ent!'); 
INSERT INTO accounts VALUES('Wyld', 23964511, 'Ted Logan', 23.58); 

INSERT INTO login VALUES('Stallyns', 'B0gu$'); 
INSERT INTO accounts VALUES('Stallyns', 58456326, 'Bill Preson, Esq.', 17.88); 

SELECT * FROM login; 
SELECT * FROM accounts; 

SELECT accounts.userName, actualName, accountNumber, balance, userPw FROM login JOIN accounts ON login.userName = accounts.userName; 

CREATE USER 'new_user'@'localhost' IDENTIFIED BY 'password';

GRANT SELECT ON HW6_v2.* TO 'new_user'@'localhost';
GRANT SELECT (userName) ON  login TO 'new_user'; 
-- GRANT SELECT(Host,User) ON mysql.db TO u1; -- grant column privileges

DROP USER 'new_user'@'localhost';
    