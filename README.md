This is a repository that will help improve my Google Reader to Pocket workflow -
and hopefully, can improve yours too!

Workflow
========

Currently, I use (IFTTT)[http://ifttt.com] to send my starred items in Google 
Reader over to Pocket.  First, I needed a way to retrieve all my old items 
out of Google Reader and into Pocket.  Second, I needed a way to remove these 
starred items in Google Reader once I've actioned them in Pocket.  

The reason for the second workflow is because if Pocket ever does get out of
sync, you don't want it to resynchronize items you've already actioned.  Trust
me, it happens - and it stinks. :)

For example, I send items over to (https://pinboard.in/u:ryankanno/)[https://pinboard.in/u:ryankanno/] 
from Pocket - once I've deleted the item from Pocket, I need to ultimately 
remove the same item from my starred feed in Google.

retro_starred_items.py
======================

This Python script just returns all your starred items in Google Reader.  This
will be helpful once we've stood something up 

pocket_to_reader_sync
=====================

This will be a Flask site to periodically ask the Pocket API what's changed
since the last sync, then action the deleted items by removing them from the
Google Reader starred items
