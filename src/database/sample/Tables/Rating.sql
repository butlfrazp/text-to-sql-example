CREATE TABLE [dbo].[Rating] (
  [Id] INT PRIMARY KEY,
  [RestaurantId] INT FOREIGN KEY REFERENCES [dbo].[Restaurant](Id) NOT NULL,
  [Stars] INT NOT NULL,
  [Comment] NVARCHAR(MAX)
)
