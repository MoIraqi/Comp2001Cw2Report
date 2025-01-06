-- Create Trail Table
CREATE TABLE CW2.Trail (
    TrailID INT PRIMARY KEY IDENTITY,
    TrailName VARCHAR(100) NOT NULL,
    Description TEXT,
    Distance DECIMAL(5,2)
);

-- Create User Table
CREATE TABLE CW2.AppUser (
    UserID INT PRIMARY KEY IDENTITY,
    NameOfUser VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL
);

-- Link Table for User and Trail Many-to-Many Relationship
CREATE TABLE CW2.TrailUser (
    TrailID INT FOREIGN KEY REFERENCES CW2.Trail(TrailID),
    UserID INT FOREIGN KEY REFERENCES CW2.AppUser(UserID),
    PRIMARY KEY (TrailID, UserID)
);
