CREATE TABLE [dbo].[Likes]
(
  CONSTRAINT EC_LIKES CONNECTION ([dbo].[Users] TO [dbo].[Restaurant])
) as EDGE
