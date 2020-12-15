BEGIN TRANSACTION;
CREATE TABLE users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text);
INSERT INTO "users" VALUES(1,'Lee','Lee@gmail.com','010-6271-5427','Lee.com','2020-12-15 20:13:11');
INSERT INTO "users" VALUES(2,'Kim','Kim@daum.net','010-9739-5435','Kim.com','2020-12-15 20:13:11');
INSERT INTO "users" VALUES(3,'Park','Park@naver.com','010-0000-0000','Park.com','2020-12-15 20:13:11');
INSERT INTO "users" VALUES(4,'Ko','Ko@naver.com','010-1111-1111','Ko.com','2020-12-15 20:13:11');
INSERT INTO "users" VALUES(5,'You','You@naver.com','010-2222-2222','You.com','2020-12-15 20:13:11');
COMMIT;
