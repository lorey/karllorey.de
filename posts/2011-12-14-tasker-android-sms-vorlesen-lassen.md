---
id: 665
title: 'Tasker: Von Android SMS vorlesen lassen'
date: 2011-12-14T19:00:50+00:00
author: Karl Lorey
layout: post
guid: http://www.karllorey.de/?p=665
permalink: /2011/12/14/tasker-android-sms-vorlesen-lassen/
categories:
  - Android
tags:
  - Anleitung
  - SMS
  - Tasker
---
Wer oft mit dem Auto oder mit dem Rad unterwegs ist, der weiß, wie nützlich es manchmal wäre, wenn Android einem die SMS vorlesen könnte. Mit dieser Anleitung für Tasker könnt ihr eurem Android genau das beibringen &#8211; nämlich euch die SMS vorzulesen.

## Anleitung

Als Erstes sollte Tasker geöffnet werden und ein neues Profil erstellt werden, welches Kontext (Ereignis) und Task (auszuführende Aufgaben) zusammenfasst. Diesem gibt man am besten einen aussagekräftigen Namen wie &#8222;SMS vorlesen&#8220;.<!--more-->


  
Anschließend muss ein erster Kontext gewählt werden, also ein Ereignis, welches in Tasker den später definierten Task auslöst, der die SMS vorliest. In diesem Fall ist das der Empfang einer SMS. Dieser Kontext ist unter &#8222;Ereignis &#8211; Telefon &#8211; Empfangene Nachricht&#8220; zu finden.
  
In den sich nun öffnenden Einstellungen kann das Ereignis eingeschränkt werden. Hier ist unter Typ &#8222;SMS&#8220; zu wählen, da Tasker gelegentlich mit MMS Probleme hat. Hier kann nach Wunsch auch ein Absender oder ein bestimmter Inhalt gewählt werden, sodass Tasker nur dann die SMS vorliest.

**Zwischenstand:** Tasker weiß bisher zwar, dass es etwas tun soll, falls eine SMS ankommt, jedoch noch nicht was.

Anschließend soll deswegen eine Aufgabe ausgewählt werden. Wir erstellen einen neuen Task mit dem Namen &#8222;Letzte SMS vorlesen&#8220;. Dieser soll die gerade empfangene SMS vorlesen.
  
Der neuen Aufgabe muss nun mit einem Klick auf &#8222;+&#8220; eine neue Aktion hinzugefügt werden. Man wählt hier &#8222;Sonstige &#8211; Vorlesen&#8220;. Tasker soll also etwas Vorlesen.
  
In den sich öffnenden Einstellungen sollte folgender Text angegeben werden:

> Neue SMS von %SMSRN. %SMSRB

Diesen Text wird Tasker später beim Empfang einer SMS vorlesen. Hier ist %SMSRN der Anrufername und %SMSRB der SMS-Inhalt. Der Rest der Nachricht kann natürlich nach Belieben angepasst werden. Drei Punkte fügen übrigens eine längere Pause ein. Die Stimme kann beliebig gewählt werden, der Rest auch. Als Stream habe ich Medien gewählt, alles andere habe ich bisher noch nicht getestet.

Nach diesem Schritt sind wir fertig und bei der nächsten SMS sollte Tasker nun die SMS vorlesen.

## Tipp

Um SMS nur Zuhause vorlesen zu lassen, kann als zweiter Kontext beispielsweise das heimische WLAN gewählt werden (Status &#8211; Netzwerk &#8211; WiFi verbunden). Dann liest Tasker die SMS nur dann vor, wenn eine Verbindung zum WLAN besteht.

Für weitere Anleitungen und Tipps kannst du dir gerne [alle Artikel mit dem Tag &#8222;Tasker&#8220;](/tag/tasker) ansehen.