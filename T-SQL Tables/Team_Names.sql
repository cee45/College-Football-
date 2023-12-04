-- Create a new table called '[TableName]' in schema '[dbo]'
-- Drop the table if it already exists
IF OBJECT_ID('[dbo].[Team_Names]', 'U') IS NOT NULL
DROP TABLE [dbo].[Team_Names]
GO
-- Create the table in the specified schema
CREATE TABLE [dbo].[Team_Names]
(
    [id] INT NOT NULL PRIMARY KEY, -- Primary Key column
    [school NVARCHAR(50) NOT NULL,
    [abbreviation] NVARCHAR(50) NOT NULL,
    [conference] NVARCHAR(50) NOT NULL
    -- Specify more columns here
);
GO