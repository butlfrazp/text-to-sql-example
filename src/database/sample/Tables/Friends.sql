CREATE TABLE [dbo].[Friends] (
  CONSTRAINT EC_FRIENDS CONNECTION ([dbo].[Users] TO [dbo].[Users])
) AS EDGE
