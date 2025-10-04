CREATE TABLE "movies" (
	"id"	TEXT NOT NULL UNIQUE,
	"comments"	TEXT,
	"rating"	INTEGER,
	PRIMARY KEY("id")
);