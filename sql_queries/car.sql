CREATE TABLE Car (
    id INT IDENTITY(1,1) PRIMARY KEY,  -- Auto-incrementing ID for each car
    brand VARCHAR(50) NOT NULL,        -- Brand of the car
    make VARCHAR(50) NOT NULL,         -- Make of the car
    model VARCHAR(50) NOT NULL,        -- Model of the car
    year INT NOT NULL,                 -- Manufacturing year
    price DECIMAL(10, 2) NOT NULL,     -- Price of the car
    availability BIT NOT NULL,         -- Whether the car is available (BIT is used for BOOLEAN)
    description TEXT,                  -- Description of the car
    image VARCHAR(100)                 -- Path or name of the car image
);
