---
id: 1313
title: Klausur-Checkliste für die Betriebssysteme-Klausur
date: 2012-11-08T13:31:47+00:00
author: Karl Lorey
layout: page
guid: http://www.karllorey.de/?page_id=1313
---
Nachfolgend finden sich diverse Fragen, die bei der Überprüfung des gelernten Stoffes helfen sollen. Die meisten dieser Fragen könnten meines Erachtens so auch in einer Betriebssysteme-Klausur gestellt werden (zusätzlich zur Algorithmen-Anwendung).

## Einführung

  * Welche der unten aufgeführten Punkte zählen zu dem Aufgabenbereich eines Betriebssystems?
  *   1. Anzeigen von Web-Pages
      2. Starten, Ausführen und Beenden von Programmen
      3. Erkennen von Viren
      4. Speicherverwaltung
      5. Verschicken von E-Mails
      6. Dateiverwaltung
      7. Verwalten von Netzwerkdiensten
      8. Verwalten von Datenbanken
      9. Ein-/Ausgabe-Verwaltung
     10. Ressourcenverwaltung
     11. Accounting
  * Was sind die Vorteile und was sind die Nachteile des VM-Konzepts?
  * Nennen Sie drei Vor- und drei Nachteile von verteilten gegenüber zentralen Systemen.

## Computer-System Structures

  * Nennen Sie sieben Arten von Speicher und sortieren Sie diese nach ihrer Geschwindigkeit.
  * Nennen Sie drei Arten von Speicher, die flüchtig sind, und sortieren Sie diese nach ihrer Geschwindigkeit.
  * Wie verhalten sich im Allgemeinen die Kosten einer Speicherart im Verhältnis zur Geschwindigkeit?

## Operating-System Structures

  * Warum bietet Java die Möglichkeit aus einem Java-Programm heraus native Methoden aufzurufen, die zum Beispiel in C oder C++ geschrieben sind? Geben Sie ein Beispiel für eine native Methode an.
  * Nennen Sie Sicherheitsaspekte, die beim Entwurf einer VM zu bedenken sind.

## Processes

  * Nennen Sie die verschiedenen Prozess-Zustände.
  * Zeichnen Sie ein Diagramm, welches den &#8222;Life-cycle&#8220; eines Prozesses darstellt.
  * Wie unterscheiden sich die Zustände wartend und bereit?
  * Was kann man tun, wenn die Prozesse zusammen mehr Hauptspeicher benötigen als vorhanden ist?

## Threads

  * Nennen Sie Vorteile von Threads
  * Wie unterscheiden sich Prozesse und Threads?
  * Welche Nachteile hat ein Multi-Thread-Programm auf einem PC mit nur einer CPU mit nur einem Kern?
  * Was sind die Vorteile für den Endbenutzer eines Programms, das rechenintensive Operationen mithilfe von Threads erledigt?

## CPU Scheduling

  * Was ist CPU-Scheduling und wofür ist es nötig?
  * Was bedeutet der Begriff Turnaround Time bezogen auf CPU-Scheduling?

## Process Synchronisation

  * Woraus besteht das Critical Section Problem? Nennen Sie Beispiele dafür aus dem PC-Alltag.
  * Wie kann wechselseitiger Ausschluss (mutual exclusion) mit Hardware realisiert werden? Wie kann es mit Java gelöst werden?
  * Bedingungen für &#8222;Critical-Sections&#8220;
  * Beschreiben Sie einen Algorithmus, der das Critical-Section-Problem für zwei Prozesse löst.
  * Welches Problem löst der Bakery Algorithmus?

## Deadlocks

  * Kriterien zur Deadlock-Charakterisierung
  * Enthält ein &#8222;Resource Allocation Graph&#8220; einen Kreis, dann existiert ein Deadlock, wenn&#8230;
  * Enthält ein &#8222;Resource Allocation Graph&#8220; einen Kreis, dann&#8230;
  * Welches Problem löst der Banker&#8217;s Algorithmus?
  * Beschreiben Sie die vier Arrays (ein Vektor und drei Matrizen) des Banker&#8217;s Algorithm

## Memory Management

  * Wodurch unterscheiden sich &#8222;Virtual adress&#8220; und &#8222;Physical adress&#8220;?
  * Geben Sie drei Verfahren zur Lösung des &#8222;Dynamic Storage-Allocation&#8220;-Problems an und beschreiben Sie diese jeweils kurz.
  * Was ist Internal Fragmentation, was External Fragmentation? Welche der beiden Arten lässt sich einfacher beheben und wie?
  * Nennen Sie drei Strukturen für Page Tables.

## Virtual Memory

## Quellen

  1. Vorlesungsfolien
  2. Übungsblätter