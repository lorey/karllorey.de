---
id: 1426
title: Geheimnisse der Chrome Developer Tools
date: 2013-02-03T11:41:00+00:00
author: Karl Lorey
layout: post
guid: http://www.karllorey.de/?p=1426
permalink: /2013/02/03/geheimnisse-der-chrome-developer-tools/
categories:
  - Allgemein
tags:
  - Anleitung
  - Chrome Developer Tools
  - Google
  - Google Chrome
  - Video
  - Vimeo
  - Vortrag
---
<a href="http://dubroy.com/blog/" target="_blank">Patrick Dubroy</a> stellt in seinem Vortrag auf der <a href="http://oredev.org/" target="_blank">Øredev Conference</a> die Geheimnisse der Chrome Developer Tools vor. Jeder Web-Entwickler, der mit den Chrome Developer Tools in Google Chrome oder Chromium arbeitet, sollte die im Vortrag vorgestellten Tipps und Tricks einmal gesehen haben.

Die Developer Tools in Google Chrome/Chromium sind ein mächtiges Werkzeug, um zu verstehen, zu debuggen und Web-Anwedungen zu profilen. Während die meisten Web-Entwickler den Grund-Funktionsumfang der Chrome Developer Tools kennen, wissen nur wenige von den wertvollen Funktionen wie der Timeline und der Speicheranalyse. Dieser Vortrag über die Chrome Developer Tools bietet eine Funktions-Übersicht, zeigt zahlreiche Tipps und Tricks und demonstriert die weniger bekannten Funktionen.



Copyright: Namensnennung &#8211; NichtKommerziell &#8211; KeineBearbeitung 3.0 Unported (CC BY-NC-ND 3.0), Quelle: <a href="http://vimeo.com/53073654" target="_blank">Vimeo</a>

Wer keine Möglichkeit das Video in voller Länge zu sehen, nur ein einzelnes Feature sucht, oder alle Geheimnisse, Tipps und Tricks lieber schriftlich aufgelistet mag, für den habe ich anschließend eine kleine Liste aller erläuterten Funktionen zusammengstellt.<!--more-->

## Vorgestellte Geheimnisse, Tipps und Tricks und weniger bekannte Funktionen der Chrome Developer Tools

### Allgemeine Tipps und Tricks

#### Die Chrome Developer Tools schnell öffnen (2:15)

Die Chrome Developer Tools öffnen per &#8222;Strg + Shift + I&#8220; (2:25) oder mit einem Rechtsklick auf &#8222;Element untersuchen&#8220; (2:35).

#### Die Chrome Developer Tools als Seitenleiste anzeigen

Mit einem Klick auf den ersten Button von links in der unteren Leiste können die Chrome Developer Tools wahlweise als Seitenleiste oder in einem neuen Fenster angezeigt werden.

### Der Elements-Tab

#### HTML-Elemente untersuchen (2:50)

**Hover hebt Elemente hervor** &#8211; Elemente die man in den Chrome Developer Tools mit der Maus überfahrt (per hover), werden auf der Seite farbig hervorgehoben (2:59).

**Drag & Drop** &#8211; Elemente können per Drag & Drop verschoben und per Doppelklick bearbeitet werden (3:17). Weiterhin ist per Rechtsklick eine freie Bearbeitung des HTML-Codes möglich. (4:00)

**Änderungen rückgängig machen** &#8211; Änderungen können durch &#8222;Strg + Z&#8220; rückgängig gemacht werden (3:40).

#### Den Stil (Style) untersuchen (4:05)

Weiterer Tipp: Auf der rechten Seite können die CSS-Regeln mit den Chrome Developer Tools untersucht werden. Hier können beispielsweise einzelne Regeln aktiviert oder deaktiviert werden. Weiterhin können auch neue Regeln erstellt werden.

#### Abmessungen untersuchen (4:45)

Im Tab unter dem &#8222;Styles&#8220;-Tab können einzelne Abmessungen untersucht werden, also wie groß Elemente tatsächlich sind. Dieser Trick hilft vor allem, wenn man die berechnete Größe eines Elements genauer untersuchen will.

#### Weitere Eigenschaften untersuchen (5:05)

In den unteren Tabs können Eigenschaften von DOM-Knoten, Event Listener, und andere Eigenschaften genauer untersucht werden.

### Sources-Panel (5:38)

Im Sources-Panel der Chrome Developer Tools können CSS- und JavaScript-Dateien live untersucht, bearbeitet und sogar wieder gespeichert werden (per Rechtsklick).

Tipp/Trick: Per Rechtsklick auch lokale Änderungen untersucht und rückgängig gemacht werden (6:15).

#### Debugging (6:55)

Die Chrome Developer Tools unterstützen auch diverse Debugging-Funktionen wie Breakpoints, wie man sie aus anderen Entwicklungsumgebungen kennt.

#### Saubere JavaScript-Darstellung (statt &#8222;minified JavaScript&#8220;, 7:13)

Tipp/Trick: Durch einen Klick auf die geschweiften Klammern &#8222;{}&#8220; in der unteren Leiste wird ein möglicherweise minimierter JavaScript-Code wieder sauber formatiert und ist so deutlich lesbarer.

Tipp/Trick: Dies kann nicht nur bei minimiertem JavaScript-Code, sondern auch bei generell schlecht formatiertem Code hilfreich sein.

### Console (8:01)

Die Console zeigt Log-Nachrichten und diverse Fehler bei der Ausführung der Webseite an.

Tipp/Trick: Per Klick kann an die entsprechende Stelle gesprungen werden. Weiterhin kann in der Console auch direkt JavaScript-Code ausgeführt werden.

#### Suche von Knoten im DOM (9:01)

In der Console der Chrome Developer Tools können per _inspect_-Funktion Knoten im DOM gesucht werden. Beispielsweise kann der _<body>_-Knoten mit

<pre class="brush: plain; title: ; notranslate" title="">inspect(document.body)</pre>

gefunden werden.

### Timeline (10:10)

Die Timeline der Chrome Developer Tools dient zum genauen untersuchen der Nutzerinteraktion (Loading, Scripting, Rendering, Painting). Mithilfe des Aufnahme-Buttons in der unteren Leiste kann eine Aufnahme gestartet werden. Ab dann werden alle Interaktionen und Events zur späteren Untersuchung von den Chrome Developer Tools aufgezeichnet.

#### Events

So kann beispielsweise die Funktionsweise einer Webseite untersucht werden. Nach der Aufzeichnung werden alle Events aufgelistet.

Tipp/Trick: Mit einem Klick kann nun zur entsprechenden JavaScript-Funktion gesprungen und diese genauer untersucht werden. Dies spart das Erarbeiten des gesamten JavaScript-Codes.

#### Frames (14:55)

Zum Leistungs-Profiling der Ausführung einer Webseite in Chrome kann der Frames-Tab genutzt werden. Hier werden die Frame-Raten aller Animationen angezeigt und können so genauer inspiziert werden. So ist es möglich, Performance-Bottlenecks bei der Ausführung bzw. dem Rendering in Google Chrome/Chromium zu erkennen und zu eliminieren.

Tipp: Die Chrome Developer Tools zeigen sogar mögliche Bottlenecks per Warnung-Icon neben dem entsprechenden Event an.

#### Memory (20:30)

Im Memory-Tab kann die Speichernutzung der Webseite in Google Chrome genauer untersucht werden. So kann beispielsweise die Garbage-Collection im Verlauf der Nutzung untersucht werden. Weiterhin werden Dokumenten-Anzahl, DOM-Knoten-Anzahl und die Anzahl der Event-Listener als Diagramm im Zeitverlauf dargestellt. Auch so lassen sich durch eine mangelhafte Speichernutzung entstehende Performance-Einbußen frühzeitig erkennen.

### Profiles-Tab (28:06)

Im Profiles-Tab der Chrome Developer Tools können folgende Profile erstellt werden:

  * CPU-Profil
  * CSS-Selektor-Profil
  * Heap-Snapshot-Erstellung

#### Heap-Snapshot-Erstellung

Auf die Heap-Snapshot-Erstellung wird genauer eingegangen. Sie ermöglicht die Untersuchung des Speichers mithilfe von Snapshots. So können JavaScript-Memory-Leaks erkannt werden. JavaScript Memory-Leaks sind zum Beispiel Objekte, die von der Garbage-Collection nicht erkannt und deshalb nicht freigegeben werden (diese werden zuvor genauer erläutert, alternativ gibt es bspw. einen <a href="http://www.ibm.com/developerworks/library/wa-jsmemory/index.html" target="_blank">Artikel von IBM über JavaScript Memory-Leaks</a>).

### Resources-Tab (32:50) und Network-Tab (33:00)

Auf die beiden Tabs wird nicht weiter eingegangen. Beide sind zwar nützliche Tools, jedoch zu genüge dokumentiert und bekannt.

## Weiterer Tipp: Verschiedene Versionen der Chrome Developer Tools nutzen (33:30)

Patrick Dubroy empfiehlt als letzten Tipp noch die parallele Nutzung von zwei Google Chrome Versionen, namentlich der Stable- und der Canary-, einer täglich geupdateten Version. So können jederzeit neuste Versionen getestet werden, da beide Versionen problemlos parallel laufen.

## Weitere Informations-Quellen zu den Chrome Developer Tools

  * <a href="https://developers.google.com/chrome-developer-tools/" target="_blank">Chrome Developer Tools Dokumentation</a>
  * <a href="http://www.youtube.com/watch?v=3pxf3Ju2row" target="_blank">Google IO 2012: Chrome Developer Tools Evolution (Vortrag auf YouTube)</a>
  * Weitere Tipps und Tricks von Paul Irish: <a href="http://www.youtube.com/watch?v=nOEw9iiopwI" target="_blank">Google Chrome Developer Tools: 12 Tricks to Develop Quicker (Vortrag auf YouTube)</a>