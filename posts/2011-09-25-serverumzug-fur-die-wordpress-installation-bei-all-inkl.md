---
id: 44
title: Serverumzug für die WordPress-Installation bei all-inkl
date: 2011-09-25T15:38:34+00:00
author: Karl Lorey
layout: post
guid: http://www.karllorey.de/?p=44
permalink: /2011/09/25/serverumzug-fur-die-wordpress-installation-bei-all-inkl/
categories:
  - Allgemein
tags:
  - all-inkl
  - Blog
  - Erlebnisbericht
  - Webhosting
  - WordPress
---
Als ich vor einigen Wochen auf meinem all-inkl-Webspace WordPress 3 installieren wollte, wurde ich bei der 5-Minuten-Installation zunächst mit folgender Fehlermeldung begrüßt:

> You cannot install because WordPress 3.2.1 requires MySQL version 5 or higher. You are running Version 4.1.22

Nach kurzer Frustation entschied ich mich für einen kurzen Faktencheck und fand durch PhpMyAdmin heraus, dass in der Tat noch die alte MySQL-Version installiert war. Ich entschied mich also an den [all-inkl-Support](http://all-inkl.com/wichtig/kontakt/) zu schreiben und zu fragen, weshalb noch diese Version installiert ist, denn ich war eigentlich davon ausgegangen, dass der Server regelmäßig geupdatet werden würde.<!--more-->

Die Mail schickte ich dann um kurz vor 00:00 Uhr ab. Bereits um 00:14 Uhr erhielt ich bereits eine Antwort vom Support: Mitten in der Nacht, nur eine Viertel Stunde später, dazu ausführlich und hilfreich:

> Hallo Herr Lorey,
> 
> Wir bieten auch Server mit PHP 5.3 und MySQL 5.1 (MySQL 4.1 wird nicht unterstützt!) an und können Ihren Account kostenlos auf einen solchen Server umziehen. Dazu benötigen wir von Ihnen als Identifizierungsnachweis die letzten 3 Zeichen des MembersArea-Passworts.
> 
> Bei einem Umzug Ihres Accounts werden grundsätzlich alle Domains oder Subdomains des Accounts und evtl. Unteraccounts mit umgezogen. Alle Daten (FTP, MySQL, KAS-Einstellungen etc.) bleiben bei dem Umzug erhalten. Der Serverumzug findet Nachts ab 2 Uhr statt und Ihre Webseite(n) sind ca. 4 Stunden wegen der Nameserveraktualisierung nicht erreichbar. Ein Umzug am Tage ist aus Performancegründen leider nicht möglich. [&#8230;]

Angefügt waren noch Hinweise auf die [Erstellung von Backups](http://all-inkl.com/wichtig/anleitungen/#anleitungen_datensicherung) und das weitere Procedere. (Als Bestätigung müssen die letzten drei Zeichen des MembersArea-Passworts gesendet werden). Nachdem ich den Serverumzug bestätigt hatte, konnte ich dann schon am nächsten Morgen WordPress installieren. Nun auf einem Server mit PHP 5.3 und MySQL 5.1 und diesmal ohne Installationsprobleme.
  
Es ist zwar ein bisschen schade, dass all-inkl nicht von sich aus ein Update anbietet, jedoch kann ich darüber bei einer solchen Response Time des Supports getrost hinwegsehen. Hier hat sich die Wahl des Hosters all-inkl eindeutig als die richtige Wahl erwiesen!