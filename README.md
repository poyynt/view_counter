# view_counter
Simple view counter with Python and Flask.


Each "counter" is a uuid and its count gets updated after each request to it.

To create the database (first time only):
```
$ sqlite3 counter.db
sqlite> CREATE TABLE counters (
   ...>     id    INTEGER      PRIMARY KEY AUTOINCREMENT
   ...>                        UNIQUE
   ...>                        NOT NULL,
   ...>     uuid  VARCHAR (36) NOT NULL
   ...>                        UNIQUE,
   ...>     count INTEGER      DEFAULT (0) 
   ...>                        NOT NULL
   ...> );
sqlite> .quit
```

The svg image is made by [Alles](https://github.com/alleshq).
