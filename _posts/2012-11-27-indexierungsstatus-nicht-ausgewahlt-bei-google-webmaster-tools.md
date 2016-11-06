---
id: 1387
title: 'Indexierungsstatus: &#8222;Nicht ausgewählt&#8220; bei Google Webmaster-Tools'
date: 2012-11-27T21:10:39+00:00
author: Karl Lorey
layout: post
guid: http://www.karllorey.de/?p=1387
permalink: /2012/11/27/indexierungsstatus-nicht-ausgewahlt-bei-google-webmaster-tools/
categories:
  - Allgemein
tags:
  - Google
  - Google Webmaster-Tools
  - SEO
  - WordPress
---
**Achtung:** Der [Indexierungsstatus &#8222;Nicht ausgewählt&#8220; ist seit dem neusten Update der Google Webmaster Tools nicht mehr vorhanden](http://www.karllorey.de/2013/02/09/google-webmaster-tools-indexierungsstatus-nicht-ausgewahlt-mit-update-entfernt/ "Google Webmaster Tools: Indexierungsstatus “Nicht ausgewählt” mit Update entfernt").

Wer sich bei Google Webmaster-Tools über viele Seiten oder sogar alle Seite mit dem Indexierungsstatus &#8222;Nicht ausgewählt&#8220; wundert, dem sei empfohlen zu prüfen, ob er seine eigene Seite mit &#8222;www.&#8220; oder ohne &#8222;www.&#8220; bei den Google Webmaster-Tools eingetragen hat. Einzusehen ist ein detaillierter Indexierungsstatus unter:

> Menü: Status
  
> &#8211; Untermenü: Indexierungsstatus
  
> &#8211; Button: Erweitert

Google unterscheidet nämlich beispielsweise die Seite karllorey.de von www.karllorey.de, da diese prinzipiell auf unterschiedliche Inhalte verweisen könnten. <!--more-->Deshalb werden auch für beide Schreibweisen unterschiedliche Statistiken in den Google Webmaster-Tools angelegt. Die Webmaster-Tools erkennen dann zum Beispiel den Inhalt der Seite mit &#8222;www.&#8220; als duplizierten Content der Seite ohne &#8222;www.&#8220;, was zum Indexierungsstatus &#8222;Nicht ausgewählt&#8220; für sehr viele Seiten führt.

## Vermeidung von &#8222;nicht ausgewählt&#8220; als Indexierungsstatus vieler Seiten<figure id="attachment_1401" style="width: 300px" class="wp-caption alignright">

[<img class="size-medium wp-image-1401" alt="Google Webmaster-Tools: Indexierungsstatus &quot;nicht ausgewählt&quot; vor und nach der Lösung des Problems" src="http://www.karllorey.de/wp-content/uploads/2012/11/google_webmaster_tools_indexierungsstatus_nicht_ausgewählt-300x235.png" width="300" height="235" />](http://www.karllorey.de/wp-content/uploads/2012/11/google_webmaster_tools_indexierungsstatus_nicht_ausgewählt.png)<figcaption class="wp-caption-text">Google Webmaster-Tools: Indexierungsstatus &#8222;nicht ausgewählt&#8220; vor und nach der Lösung des Problems</figcaption></figure> 

Zunächst sollte man prinzipiell beide Versionen in den Google Webmaster-Tools als eigene Webseite eingetragen haben. So lässt sich prüfen, ob das Problem wirklich nur ein Problem der Seiten-Schreibweise, oder doch ein Problem des Seiten-Content ist.

Sind in den Webmaster-Tools zumindest unter einer der beiden Schreibweisen Seiten indexiert (&#8222;Gesamt indexiert&#8220; also größer als 0), so liegt es wahrscheinlich an der Schreibweise. Ob überhaupt Seiten indexiert sind, kann übrigens auch mit einer Google-Suche nach &#8222;site:example.com&#8220; und &#8222;site:www.example.com&#8220; geprüft werden. Existieren für eine der beiden Varianten Ergebnisse, so sind Seiten im Google-Index.

Um das Problem jedoch langfristig zu lösen, sollte man sich für eine Version der beiden Schreibweisen entschieden. In den Google Webmaster-Tools ist dann unter

> Menü: Konfiguration
  
> &#8211; Untermenü: Einstellungen
  
> &#8211; Bevorzugte Domain

bei jeweils beiden Schreibweisen der Seite die bevorzugte Schreibweise einzutragen. Weiterhin kann es von Vorteil sein, von der nicht bevorzugten Schreibweise auf die bevorzugte Schreibweise mit einem Redirect (Moved Permanently Redirect, 301) umzuleiten. Weitere Details zu diesem Problem finden sich im <a href="http://googlewebmastercentral.blogspot.de/2006/09/setting-preferred-domain.html" target="_blank">Webmaster Central Blog von Google selbst</a>.

## Indexierungsstatus: &#8222;Nicht ausgewählt&#8220; bei einer Wordpress-Installation

In WordPress ist dieser Redirect übrigens bereits integriert, je nachdem, ob unter

> Einstellungen &#8211; Allgemein

die WordPress-Adresse bzw. die Seiten-Adresse mit oder ohne &#8222;www&#8220; eingetragen ist. Am einfachsten ist also in den Google Webmaster-Tools die bereits in WordPress eingetragene Schreibweise zu wählen.