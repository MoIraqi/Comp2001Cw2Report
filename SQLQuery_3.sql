-- the point of this sample data is to test the implementation

-- I made sample data to insert into the trail
INSERT INTO CW2.Trails (TrailName, TrailSummary, Difficulty, Location, Length, ElevationGain, RouteType)
VALUES 
('Plymbridge Circular', 'A scenic loop through ancient woodlands', 'Moderate', 'Devon, UK', 5.5, 120, 'Loop');

-- Sample data to insert into Feature
INSERT INTO CW2.Feature (FeatureName)
VALUES 
('Bench'),
('Viewpoint'),
('Picnic Area');

-- sample data to insert into TrailFeature
INSERT INTO CW2.TrailFeature (TrailID, FeatureID)
VALUES 
(1, 1), -- TrailID 1 has a Bench
(1, 2); -- TrailID 1 has a Viewpoint

-- sample data insert into LocationPoint
INSERT INTO CW2.LocationPoint (Latitude, Longitude, Description, TrailID)
VALUES 
(50.3941, -4.0889, 'Starting Point', 1),
(50.3990, -4.0850, 'Woodland Area', 1);
