---
id: 652
title: Tennisdatenbank
date: 2011-12-14T16:50:45+00:00
author: Karl Lorey
layout: page
guid: http://www.karllorey.de/?page_id=652
---
Die Aufgaben der Übungsblätter 1 und 3 behandeln eine Datenbank, die ein Tennis-Match erfassen kann. Hierzu wurde dann in Übungblatt 3 die folgende Struktur vorgegeben:

  * Spieler (ID, Name), Key(ID)
  * Schlag (Satznr, Spielnr, Punktnr, Schlagnr, Schlagart, Typ, Fehler), Key(Satznr, Spielnr, Punktnr, Schlagnr)
  * Aufschlag (Satznr, Spielnr, SpielerID), Key(Satznr, Spielnr)

## Aufgabe 2

Aus dieser Struktur ergibt sich der SQL-Dump (bzw. MySQL-Dump) folgender Tabellen. Achtung: Ich habe die Anforderungen beider Übungsblätter zusammengeworfen.

<pre class="brush: sql; title: ; notranslate" title="">CREATE DATABASE IF NOT EXISTS tennis;
USE tennis;

CREATE TABLE spieler (
id INT NOT NULL,
name VARCHAR(50) NOT NULL,
PRIMARY KEY(id)
);

CREATE TABLE aufschlag (
satznr INT NOT NULL,
spielnr INT NOT NULL,
spielerid INT NOT NULL,
PRIMARY KEY(satznr, spielnr),
FOREIGN KEY(spielerid) REFERENCES spieler(id)
);

CREATE TABLE schlag (
satznr INT NOT NULL,
spielnr INT NOT NULL,
punktnr INT NOT NULL,
schlagnr INT NOT NULL,
x INT NOT NULL,
y INT NOT NULL,
zeitpunkt DATETIME NOT NULL,
typ VARCHAR(20) NOT NULL,
schlagart VARCHAR(20) NOT NULL,
fehler TINYINT(1) NOT NULL,
PRIMARY KEY(satznr, spielnr, punktnr, schlagnr),
FOREIGN KEY(satznr, spielnr) REFERENCES aufschlag(satznr, spielnr)
);
</pre>

## Aufgabe 3

Spiele, in denen Volleys gespielt wurden

<pre class="brush: sql; title: ; notranslate" title="">SELECT DISTINCT
  aufschlag.satznr, aufschlag.spielnr
FROM
  aufschlag, schlag
WHERE
  schlag.typ = 'Volley'
  AND schlag.spielnr = aufschlag.spielnr
  AND schlag.satznr = aufschlag.satznr
;
</pre>

Spieler mit dem ersten Aufschlag des Matches

<pre class="brush: sql; title: ; notranslate" title="">SELECT
  spieler.name
FROM
  aufschlag, spieler
WHERE
  aufschlag.satznr = 1
  AND aufschlag.spielnr = 1
  AND aufschlag.spielerid = spieler.id
;
</pre>

Anzahl der gespielten Schläge pro Satz

<pre class="brush: sql; title: ; notranslate" title="">SELECT
  aufschlag.satznr, count(*) AS schlaganzahl
FROM
  aufschlag, schlag
WHERE
  aufschlag.spielnr = schlag.spielnr
  AND aufschlag.satznr = schlag.satznr
GROUP BY
	aufschlag.satznr
;
</pre>

Punkte, in denen der Spieler Sampras einen Volley gespielt hat

<pre class="brush: sql; title: ; notranslate" title="">SELECT
  aufschlag.satznr, aufschlag.spielnr AS spielnr, schlag.punkt
FROM
  schlag, aufschlag
WHERE
  aufschlag.spielnr = schlag.spielnr
  AND aufschlag.satznr = schlag.satznr
  AND schlag.typ = 'Volley'
  AND (schlag.schlagnr MOD 2) = (aufschlag.spielerid = (SELECT id FROM spieler WHERE name = 'Sampras'))
;
</pre>

## Aufgabe 5

Spiele ohne Volleys

<pre class="brush: sql; title: ; notranslate" title="">SELECT
  satznr, spielnr
FROM
  schlag
WHERE
  schlag.Typ &lt;&gt; 'Volley'
GROUP BY
  schlag.Satznr, schlag.Spielnr
HAVING
  count(*) &gt; 0
</pre>

Punkte mit mind. 10 Rückhandschlägen

<pre class="brush: sql; title: ; notranslate" title="">SELECT
  satznr, spielnr, punktnr
FROM
  schlag
WHERE
  schlag.Schlagart = 'Rückhand'
GROUP BY
  satznr, spielnr, punktnr
HAVING
  count(*) &gt;= 10
</pre>

Punkte, die Sampras trotz gegnerischem Aufschlag gewonnen hat. Teilweise fehlerhaft (2,5 von 3 Punkten)

<pre class="brush: sql; title: ; notranslate" title="">SELECT
  schlag.satznr, schlag.spielnr, schlag.punktnr
FROM
  aufschlag,
  (
    SELECT
      satznr, spielnr, punktnr, max(schlagnr) AS schlagnr, fehler
    FROM
      schlag
    GROUP BY
      satznr, schlagnr, punktnr
  ) AS schlag,
  spieler as asspieler
WHERE
  aufschlag.Satznr = schlag.satznr
  AND aufschlag.Spielnr = schlag.Spielnr
  AND aufschlag.SpielerID = asspieler.ID
  AND asspieler.name &lt;&gt; 'Sampras'
  AND ((schlag.Schlagnr MOD 2) = schlag.Fehler)
GROUP BY
  schlag.Satznr,
  schlag.Spielnr,
  schlag.Punktnr
</pre>

Gewinner des Matches ermitteln. Teilweise fehlerhaft (2,5 von 3 Punkten). Korrekt wäre es, den letzten fehlerfreien Schlag zu berechnen, da dies laut Übungsleiter immer der Gewinner des Tennis-Matches ist.

<pre class="brush: sql; title: ; notranslate" title="">SELECT
  gewinner.name
FROM
  (
  SELECT
    satznr, spielnr, punktnr, MAX(schlagnr) as lschlagnr
  FROM
    schlag
  GROUP BY
    satznr, spielnr, punktnr
  ) AS lschlag,
  schlag,
  aufschlag,
  spieler AS gewinner
WHERE
  aufschlag.Satznr = lschlag.satznr
  AND aufschlag.Spielnr = lschlag.spielnr
  AND schlag.satznr = lschlag.satznr
  AND schlag.spielnr = lschlag.spielnr
  AND schlag.punktnr = lschlag.punktnr
  AND schlag.schlagnr = lschlag.lschlagnr
  AND (
    ((schlag.fehler + schlag.schlagnr) MOD 2) = 1 AND aufschlag.SpielerID = gewinner.ID
    OR
    ((schlag.fehler + schlag.schlagnr) MOD 2) = 0 AND aufschlag.SpielerID &lt;&gt; gewinner.ID
  )
GROUP BY gewinner.name
ORDER BY count(*) DESC
LIMIT 1
</pre>

## Aufgabe 6

Einfügen des Spielern namens Sampras.

<pre class="brush: sql; title: ; notranslate" title="">INSERT INTO spieler VALUES (3, "Sampras")
</pre>

Den Spieler namens Becker in Müller umbenennen.

<pre class="brush: sql; title: ; notranslate" title="">UPDATE
  spieler
SET
  name = "Müller"
WHERE
  name = "Becker"
</pre>

Schlagart des zweiten Schlags des Matches auf Rückhand ändern. Annahme: Aufschlag wird immer angenommen.

<pre class="brush: sql; title: ; notranslate" title="">UPDATE
  schlag
SET
  schlagart = "Rückhand"
WHERE
  satznr = 1
  AND spielnr = 1
  AND punktnr = 1
  AND schlagnr = 2
</pre>

Letzten Satz des Matches löschen.

<pre class="brush: sql; title: ; notranslate" title="">DELETE FROM
  aufschlag
WHERE
  satznr = (SELECT satznr FROM schlag ORDER BY satznr DESC LIMIT 1);

DELETE FROM
  schlag
WHERE
  satznr = ((SELECT satznr FROM aufschlag ORDER BY satznr DESC LIMIT 1) + 1)
</pre>