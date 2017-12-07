# TODO

## Geometry and (lat,long)
Would be great to query the weather by bounding box rather than specific coords; or store by box and query by coords.
-Would probably use python's shapely lib and create 'functions' for the sqlite client that can run that code.
-Or is there something with SQLite that support geo operations?
-Need some research on how big of a box we could save at and have weather approx same within the box.
    - This probably partially depends on what weather features used - temperature is pretty evenly distributed, rain is not necessarily.

## JSON handling
Parsing JSON with SQLite - there's a lib, and we could use it and query things directly rather than spending time
deserializing a bunch of JSON.

