---
id: 902
title: 'Tasker: Notfall-SMS mit GPS-Position versenden'
date: 2012-05-09T10:40:04+00:00
author: Karl Lorey
layout: post
guid: http://www.karllorey.de/?p=902
permalink: /2012/05/09/tasker-notfall-sms-mit-gps-position-versenden/
categories:
  - Android
tags:
  - Android
  - Anleitung
  - App
  - GPS
  - Notfall-SMS
  - SMS
  - Tasker
---
In einigen Senioren-Handys ist bereits eine Notfall-SMS-Funktion eingebaut. In einer misslichen Lage lässt sich so beispielsweise eine SMS an Angehörige versenden.

So eine Notfall-SMS-Funktionalität kann natürlich nicht nur für Senioren-Handys, sondern auch für Android-Smartphones durchaus nützlich sein. Deshalb habe ich, mithilfe der App Tasker Android so konfiguriert, dass beim Empfangen eines bestimmten Codeworts per SMS eine Notfall-SMS an den Absender mit der aktuellen Position versendet wird. So kann ein besorgter Angehöriger im Notfall die aktuelle Position des Android-Smartphones bestimmen. Eine weitere nützliche Funktion ist ein automatisierter Rückruf, dessen Umsetzung ich anschließend beschreiben werde.

Für die Umsetzung wird die App <a href="https://play.google.com/store/apps/details?id=net.dinglisch.android.taskerm" target="_blank">&#8222;Tasker&#8220; (bei Google Play)</a> benötigt. Tasker dient zur Automatisierung von Aufgaben in Android. Mit Tasker kann man sich beispielsweise auch <a title="Tasker: Von Android SMS vorlesen lassen" href="http://www.karllorey.de/2011/12/14/tasker-android-sms-vorlesen-lassen/" target="_blank">SMS vorlesen lassen</a> und den <a title="Tasker: Mit 3rd-Party-Apps den Funktionsumfang erweitern" href="http://www.karllorey.de/2011/11/08/tasker-mit-3rd-party-apps-den-funktionsumfang-erweitern/" target="_blank">Funktionsumfang sogar durch andere Apps noch erweitern</a>.<!--more-->

## Kontext: Der Auslöser

Zunächst sollte ein neues Tasker-Profil namens &#8222;Notfall&#8220; erstellt werden. Der Kontext, also der Auslöser für die Aufgabe, soll eine empfangene Nachricht mit dem Codewort sein. Man wählt also Ereignis &#8211; Telefon &#8211; Empfangene Nachricht. In den Optionen kann nun beliebig auf einen bestimmten Absender beschränkt werden. Als Inhalt sollte man das mit dem Angehörigen abgesprochene Wort eintragen. Zum Beispiel &#8222;Notfall&#8220; oder &#8222;Position&#8220;.

## Aufgabe: Die Ortung

Nachdem Tasker nun den Kontext (Auslöser) für den Notfall kennt, muss noch definiert werden, was im Notfall geschehen soll. Hierzu ist in Tasker eine neue Aufgabe namens &#8222;Notfall-SMS&#8220; zu erstellen.

Zur Positionsbestimmung (Ortung) mittels GPS sind folgende Schritte auszuführen:

  * Sonstige &#8211; GPS
  
    setzen An
  * Sonstige &#8211; Positionsbestimmung
  
    Quelle GPS
  
    Timeout 100s
  * Sonstige &#8211; GPS
  
    setzen Aus

## Aufgabe: Versand der Notfall-SMS mit Koordinaten

Nachdem Android nun durch Tasker eine Ortung durchgeführt hat, kann die ermittelte Position per SMS versendet werden.

  * Telefon &#8211; Sende SMS
  
    Nummer [die Nummer des Angehörigen oder %SMSRF für den Absender der SMS]
  
    Nachricht mit %LOC (für Koordinaten der aktuellen Posotion) und %LOCACC (für Ortungsgenauigkeit)

<div>
  Als SMS-Text kann zum Beispiel folgende Formulierung gewählt werden:
</div>

<pre>Die aktuelle Position meines Telefons ist %LOC mit einer Genauigkeit von circa %LOCACC Metern.</pre>

  * Weitere &#8222;Sende SMS&#8220;-Aktionen für weitere Angehörige

## Weitere Möglichkeiten

### Notfall-SMS per Shortcut

Die Notfall-SMS kann auch per Shortcut verwendet werden. Hierzu muss dem Homescreen ein neues Widget namens Task hinzugefügt werden. Nach dem Auswählen ist dann der zuvor erstellte Task &#8222;Notfall-SMS&#8220; zu wählen. So kann im Notfall per Klick auf den Shortcut die SMS versendet werden. Wichtig: Bei einem Auslösen per Shortcut ist in der Tasker-Aufgabe die Nummer des SMS-Empfängers direkt anzugeben und nicht über die Variable %SMSRF, da ja keine SMS empfangen wird und somit auch kein Absender existiert.

### Automatischer Rückruf

Neben einer Notfall-SMS kann auch ein automatischer Anruf ausgeführt werden. Nach Empfang des Codeworts wird dann der Absender der SMS angerufen und das Telefon auf &#8222;frei sprechen&#8220; gestellt. Dies geschieht folgendermaßen und kann beispielsweise direkt im Anschluss an den Notfall-SMS-Versand geschehen:

  * Telefon &#8211; Anrufen
  
    Nummer %SMSRF (für den Absender der Notfall-SMS)
  * Audio &#8211; Lautsprecher
  
    setzen An

Falls ihr weitere nützliche Ideen haben solltet, könnt ihr gerne einen Kommentar hinterlassen. Ich werde mich dann um eine Umsetzung in Tasker kümmern.

Weitere [Tasker-Anleitungen](/tag/tasker) sind übrigens unter dem Tag [Tasker](/tag/tasker) zu finden.