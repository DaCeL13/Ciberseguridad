CREATE SCHEMA IF NOT EXISTS grupo_g;

CREATE TABLE IF NOT EXISTS grupo_g.users (
    id SERIAL,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

ALTER TABLE grupo_g.users ADD CONSTRAINT pk_users PRIMARY KEY (id);
ALTER TABLE grupo_g.users ADD CONSTRAINT uq_username UNIQUE (username);