CREATE TABLE "movies" (
	"id"	TEXT NOT NULL UNIQUE,
	"comments"	TEXT,
	"rating"	INTEGER,
	PRIMARY KEY("id")
);
CREATE TABLE "comments" (
	"id"	INTEGER NOT NULL,
	"movie_id"	TEXT,
	"comment"	TEXT,
	"user"	TEXT,
	"date"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);	