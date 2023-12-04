-- Create a new table called '[TableName]' in schema '[dbo]'
-- Drop the table if it already exists
IF OBJECT_ID('[dbo].[Conferences]', 'U') IS NOT NULL
DROP TABLE [dbo].[Conferences]
GO
-- Create the table in the specified schema
CREATE TABLE [dbo].[Conferences]
(
[id] INT NOT NULL PRIMARY KEY, 
[name] NVARCHAR(50) NOT NULL,
[short_name] NVARCHAR(50) NOT NULL,
[abbreviation] NVARCHAR(50) NOT NULL,
[classification] NVARCHAR(50) NOT NULL,
);
GO


