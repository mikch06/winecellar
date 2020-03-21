# cat data/wine_wine.sql |sqlite3 db.sqlite3

BEGIN TRANSACTION;
DROP TABLE IF EXISTS "wine_wine";
CREATE TABLE IF NOT EXISTS "wine_wine" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"winename"	varchar(200) NOT NULL,
	"producer"	varchar(200) NOT NULL,
	"drinkfrom"	varchar(200) NOT NULL,
	"drinkto"	varchar(200) NOT NULL,
	"grapes"	varchar(200) NOT NULL,
	"nmbrbottles"	integer NOT NULL,
	"year"	varchar(200) NOT NULL,
	"country"	varchar(200) NOT NULL,
	"notes"	varchar(400) NOT NULL,
	"region"	varchar(200) NOT NULL,
	"editdate"	date NOT NULL,
	"purchase"	date
);
INSERT INTO "wine_wine" ("id","winename","producer","drinkfrom","drinkto","grapes","nmbrbottles","year","country","notes","region","editdate","purchase") VALUES (161,'John''s Blend Cab 2009','John Glazer','','2030','Cabernet Sauvignon',2,'2009','AU','-','','2020-03-20','2013-11-13');
INSERT INTO "wine_wine" ("id","winename","producer","drinkfrom","drinkto","grapes","nmbrbottles","year","country","notes","region","editdate","purchase") VALUES (162,'Zweigelt Prädium','Scheibelhofer','2017','2022','100% Zweigelt',1,'2014','AT','','Burgenland','2020-03-20','2015-11-01');
INSERT INTO "wine_wine" ("id","winename","producer","drinkfrom","drinkto","grapes","nmbrbottles","year","country","notes","region","editdate","purchase") VALUES (163,'Chateau Belgrave, Haut Médoc','Chateau Belgrave','2019','2030','74% Cab, 23% Merlot, 3% Petit Verdot',1,'2009','FR','Magnum, Geschenk von Probtsts Weihnachten 2018','','2020-03-20',NULL);
INSERT INTO "wine_wine" ("id","winename","producer","drinkfrom","drinkto","grapes","nmbrbottles","year","country","notes","region","editdate","purchase") VALUES (164,'Chateau Larrivet Haut-Brion Pessac-Leognan','Chateau Belgarve','2019','2024','74% Cab, 23% Merlot, 3% Petit Verdot',6,'2009','FR','Coop Weinschiff
20','','2020-03-20',NULL);
INSERT INTO "wine_wine" ("id","winename","producer","drinkfrom","drinkto","grapes","nmbrbottles","year","country","notes","region","editdate","purchase") VALUES (165,'Amarone del Maestro Fornaser Riserva','Fornaser','2015','2040','',1,'2010','IT','Geschenk','Valpolicella','2020-03-20','2016-03-11');
INSERT INTO "wine_wine" ("id","winename","producer","drinkfrom","drinkto","grapes","nmbrbottles","year","country","notes","region","editdate","purchase") VALUES (166,'Barbera d’Alba La Soprana','Marco Brangero','2018','2030','100% Barbera d''Alba',11,'2015','IT','Ab Hof','Piemont','2020-03-20',NULL);
INSERT INTO "wine_wine" ("id","winename","producer","drinkfrom","drinkto","grapes","nmbrbottles","year","country","notes","region","editdate","purchase") VALUES (167,'Chateau La Garde','Chateau La Garde','2023','2036','52% Cabernet Sauvignon, 45% Merlot, 3% Petit Verdot',6,'2016','FR','Mövenpick Rotkreuz','Bordeaux, Pessac Léonan','2020-03-20',NULL);
INSERT INTO "wine_wine" ("id","winename","producer","drinkfrom","drinkto","grapes","nmbrbottles","year","country","notes","region","editdate","purchase") VALUES (168,'Astrales Ribera del Duero','Bodegas Los Astrales','2020','2030','100% Tempranillo',6,'2016','SP','Rabatt, wäre 36.00','Ribera del Duero','2020-03-20',NULL);
INSERT INTO "wine_wine" ("id","winename","producer","drinkfrom","drinkto","grapes","nmbrbottles","year","country","notes","region","editdate","purchase") VALUES (169,'Vernaccia di San Gimignano','Bonacchi','2018','2020','',1,'2018','IT','In der Toscana gekauft','Toscana','2020-03-20','2019-08-07');
INSERT INTO "wine_wine" ("id","winename","producer","drinkfrom","drinkto","grapes","nmbrbottles","year","country","notes","region","editdate","purchase") VALUES (170,'Big John Cuvee Reserve','Scheibelhofer','2020','2025','60% Zweigelt, 20% Cabernet Sauvignon, 20% Pinot Noir',6,'2017','AT','Wäre 21.00 CHF','Burgenland','2020-03-20','2020-01-02');
COMMIT;
