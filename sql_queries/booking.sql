CREATE TABLE booking (
    id INT IDENTITY(1,1) PRIMARY KEY,                 -- Auto-incrementing primary key
    user_id INT NOT NULL,                             -- Foreign key to the users table
    car_id INT NOT NULL,                              -- Foreign key to the cars table
    booking_date DATETIME NOT NULL,                   -- Booking date
    return_date DATETIME NOT NULL,                    -- Return date
    status NVARCHAR(50) DEFAULT 'Pending',            -- Status with default value 'Pending'
    CONSTRAINT FK_User FOREIGN KEY (user_id) REFERENCES users (id),
    CONSTRAINT FK_Car FOREIGN KEY (car_id) REFERENCES Car (id)
);