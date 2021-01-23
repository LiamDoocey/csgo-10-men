# csgo-10-men

This discord bot helps oragnise CSGO 5v5 games in a server

A user will use the ~q command to join the game queue and will use the ~l command to leave the queue, the ~lp or ~players command can show what users are already in the queue

Once the queue reaches 10 users the bot will send a DM to everybody in the queue with a link to a popflash room which is a CSGO scrimage (Practice match) site, 
the sites match rooms are dynamically created so the use of random.randint(100, 100000) at the end of the link makes it a very low chance of the bot giving a match room
thats is already in use

Teams are then decided on the popflash site as of now but picking teams using the bot is a hope of mine in the near future.
