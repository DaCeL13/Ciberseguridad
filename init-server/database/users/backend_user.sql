CREATE USER 'backend_user'@'localhost' IDENTIFIED BY 'Backapp@v1.';

GRANT ALL PRIVILEGES ON grupo_g.* TO 'backend_user'@'localhost';

FLUSH PRIVILEGES;
