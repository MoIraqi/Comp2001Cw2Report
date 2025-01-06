CREATE TABLE CW2.Trails (
    TrailID INT PRIMARY KEY IDENTITY(1,1), -- This is theprimary key
    TrailName VARCHAR(100) NOT NULL,      -- Name of the trail
    TrailSummary TEXT,                    -- the brief description of the trail
    TrailDescription TEXT,                -- Full description of the trial
    Difficulty VARCHAR(20),               -- Difficulty level (e.g., Easy, Moderate etc.)
    Location VARCHAR(100),                -- Location name
    Length DECIMAL(5,2),                  -- This is trail length in km
    ElevationGain DECIMAL(5,2),           -- This is the total elevation gain in meters
    RouteType VARCHAR(50),                -- This is the type of trail (e.g., Loop, Out-and-Back)
    OwnerID INT                           -- this is the ID of the trail's owner
);

CREATE TABLE CW2.Feature (
    FeatureID INT PRIMARY KEY IDENTITY(1,1), -- Auto-incrementing primary key
    FeatureName VARCHAR(100) NOT NULL       -- Name of the feature (e.g., "Bench")
);

CREATE TABLE CW2.TrailFeature (
    TrailID INT NOT NULL,                   -- this is the foreign key referencing Trail table
    FeatureID INT NOT NULL,                 -- this is the foreign key referencing Feature table
    PRIMARY KEY (TrailID, FeatureID),       -- this is the composite primary key
    FOREIGN KEY (TrailID) REFERENCES CW2.Trails(TrailID),
    FOREIGN KEY (FeatureID) REFERENCES CW2.Feature(FeatureID)
);

CREATE TABLE CW2.LocationPoint (
    LocationPointID INT PRIMARY KEY IDENTITY(1,1), -- this is the auto-incrementing primary key
    Latitude DECIMAL(9,6) NOT NULL,               -- this is the latitude coordinate
    Longitude DECIMAL(9,6) NOT NULL,              -- this the longitude coordinate
    Description TEXT,                             -- this is the description of the location point
    TrailID INT NOT NULL,                         -- this is the foreign key referencing Trail table
    FOREIGN KEY (TrailID) REFERENCES CW2.Trails(TrailID)
);
