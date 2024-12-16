CREATE TABLE CW2.Trail (
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

