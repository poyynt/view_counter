
To create the database:
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
