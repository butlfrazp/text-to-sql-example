CREATE TABLE [dbo].[Menu](
  [Id] INT NOT NULL PRIMARY KEY,
  [RestaurantId] INT FOREIGN KEY REFERENCES [dbo].[Restaurant](Id) NOT NULL 
)