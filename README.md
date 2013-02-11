This is a repository that will help improve my Google Reader to Pocket workflow
and hopefully can improve yours too!

Workflow
========

Currently, I use [IFTTT](http://ifttt.com) to send my starred items in Google 
Reader over to [Pocket](http://getpocket.com/). This may be unique to living 
in a big city, but not having service in the subways stinks. Pocket solves 
this problem by caching the content of all my starred items. Not to mention,
Pocket syncs with my cell phone over my wi-fi network (keeping my cell-phone 
data usage down).

I needed a way to retrieve all my old items out of Google Reader and send them 
to Pocket. Once in Pocket, I need a way to remove these starred items in 
Google Reader once I've actioned them in Pocket.  

In Pocket, I typically send items over to [https://pinboard.in/u:ryankanno/](https://pinboard.in/u:ryankanno/)
to permanently archive all my personal favs. Once the item has been deleted 
from Pocket, I need to ultimately remove the same item from my starred feed in Google.

I know the reason for the second workflow is subjective. I just want to have a 
clean Google Reader starred items list. I guess I'm OCD like that. :D


retro_starred_items.py
======================

This Python script returns all your starred items in Google Reader to a csv
file.  Once we have the "Pocket-to-Reader" sync going, we'll push all these
items over to Pocket.


pocket_to_reader_sync
=====================

This will be a Flask site to periodically query Pocket's API to determine 
what's changed since the previous sync.  Ideally, we'll action the deleted 
items by removing them from the Google Reader starred items.
