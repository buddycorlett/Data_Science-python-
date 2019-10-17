Update customers
Set Email = 'ppicasso@gmail.com'
Where Name = 'Pablo Picasso'

Update customers
SET Email = CASE
WHEN Name = 'Abraham Lincoln' THEN 'lincoln@us.gov'
WHEN Name = 'Napoléon Bonaparte' THEN 'hello@napoleon.me'
else Email
END

WHERE Name in ('Abraham Lincoln', 'Napoléon Bonaparte');