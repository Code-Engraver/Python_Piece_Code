BEGIN TRANSACTION;
CREATE TABLE user(
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        regdate TEXT
    );
INSERT INTO "user" VALUES(1,'Erica','Erica@example.com','2020-07-07 17:12:26');
INSERT INTO "user" VALUES(2,'Frances','Frances@example.com','2020-07-07 17:12:26');
INSERT INTO "user" VALUES(4,'Edith','Edith@example.com','2020-07-07 17:12:26');
INSERT INTO "user" VALUES(5,'Cynthia','Cynthia@example.com','2020-07-07 17:12:26');
COMMIT;
