PRAGMA foreign_KEYs=ON;
BEGIN TRANSACTION;
DROP TABLE IF EXISTS user;

CREATE TABLE user(
    username VARCHAR(25) PRIMARY KEY NOT NULL,
    password VARCHAR(25) NOT NULL,
    fname TEXT,
    lname,
    UNIQUE(username)
);

CREATE INDEX idx_user ON user(username, password);

COMMIT;