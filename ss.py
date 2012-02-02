#!/usr/bin/env python
from datetime import date
import nextevent

dates = {
  (2012,  2,  2): ('Recrudescence', 'Bricklayers Arms', 'W1T 1QS'),
}

def next_meet(fromd):
  fromd = fromd.year, fromd.month, fromd.day
  future = [d for d in dates if d >= fromd]
  if not future:
    return None
  return date(*min(future))

start, end = nextevent.get(next_meet, '18:00')

name, venue, postcode = dates[(start.year, start.month, start.day)]

print 'Substandards %s: %s at %s, %s (%s until beer!)' % (
  name,
  nextevent.date_nice(start),
  venue,
  postcode,
  nextevent.untilmsg(start),
)

