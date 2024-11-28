CREATE TABLE users (
    id INT IDENTITY(1,1) PRIMARY KEY,       -- Auto-incrementing primary key
    full_name NVARCHAR(150) NOT NULL,       -- Full name of the user
    email NVARCHAR(150) NOT NULL UNIQUE,    -- Unique email address
    password NVARCHAR(256) NOT NULL         -- Password (hashed)
);
