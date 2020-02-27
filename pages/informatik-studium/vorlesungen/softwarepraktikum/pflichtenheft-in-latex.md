---
id: 916
title: Pflichtenheft in LaTeX
date: 2012-03-04T22:09:01+00:00
author: Karl Lorey
layout: page
guid: http://www.karllorey.de/?page_id=916
---
Hier befindet sich der Quelltext für ein Pflichtenheft in LaTeX nach dem &#8222;Lehrbuch der Objektmodellierung&#8220; von Heide Balzert. In den einzelnen Kapiteln findet sich eine Kurzbeschreibung des geforderten Inhalts.

Eine Pflichtenheft nach Helmut Balzerts &#8222;Lehrbuch der Softwaretechnik&#8220; wird in den nächsten Tagen folgen. Es ist etwas umfangreicher als Heide Balzerts Version.

Der LaTeX-Quelltext für das Pflichtenheft findet sich anschließend oder auf <a href="https://github.com/lorey/pflichtenheft" target="_blank">GitHub</a>. Weiterhin existiert auch eine [Vorschau des Pflichtenheft in Latex (Version 0.2)](http://www.karllorey.de/wp-content/uploads/2012/03/pflichtenheft_v0-2.pdf).

## <span style="font-size: 1.285714286rem; line-height: 1.6;">LaTeX-Quelltext</span>

<pre class="brush: latex; title: ; notranslate" title="">% Version 0.2
\documentclass[a4paper]{scrreprt}

\usepackage[german]{babel}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{ae}
\usepackage[bookmarks,bookmarksnumbered]{hyperref}

\begin{document}

\title{Pflichtenheft mit LaTeX}
\author{Karl Lorey}
\maketitle

% Die abstract-Umgebung kann bei Bedarf aus dem Pflichtenheft entfernt werden
\begin{abstract}
Dies ist ein beispielhaftes Pflichtenheft in \LaTeX. Das Pflichtenheft
beschreibt in konkreter Form, wie der Auftragnehmer die Anforderungen des
Auftraggebers zu lösen gedenkt - das sogenannte wie und womit. Der Auftraggeber
beschreibt vorher im Lastenheft möglichst präzise die Gesamtheit der
Forderungen - was er entwickelt oder produziert haben möchte. Erst wenn der
Auftraggeber das Pflichtenheft akzeptiert, sollte die eigentliche Arbeit beim
Auftragnehmer beginnen.
\vspace{1cm}

Quelle: \url{http://de.wikipedia.org/wiki/Pflichtenheft} und Lehrbuch der
Objektmodellierung von Heide Balzert
\vspace{0.5cm}

Quellcode: \url{http://www.karllorey.de/informatik-studium/vorlesungen/softwarepraktikum/pflichtenheft-in-latex/}
\end{abstract}

% Platzierung des Inhaltsverzeichnisses
\tableofcontents

\chapter{Zielbestimmung}
Dieses Kapitel dient der Bestimmung von Zielen und nicht für deren Verwendung
notwendige Funktionen.

\section{Musskriterien}
Musskriterien: Für das Produkt unabdingbare Leistungen, die in jedem Fall
erfüllt werden müssen \footnote{gezwungen sein, etwas zu tun (Dies ist eine
beispielhafte Fußnote).}. Das System ist ohne diese Funktionen für seinen
gedachten Zweck nicht einsetzbar.

\section{Kannkriterien}
Kannkriterien: Die Erfüllung der Kannkriterien ist erwünscht, jedoch nicht
unbedingt notwendig. Sie sollten nur angestrebt werden, falls noch ausreichend
Kapazitäten vorhanden sind.

\section{Abgrenzungskriterien}
Abgrenzungskriterien: Diese Kriterien sollen bewusst nicht erreicht werden.

\chapter{Einsatz}
Der geplante Einsatz des Systems ist die Grundlage für Benutzungsoberfläche und
Qualitätsanforderungen.

\section{Anwendungsbereiche}
Ein Pflichtenheft wird bspw. in einer IT-Abteilung genutzt.

\section{Zielgruppen}
Die Zielgruppe besteht also aus Informatikern, die mit der Projektplanung
beauftragt wurden.

\section{Betriebsbedingungen}
Betriebsbedingungen: Die Betriebsbedingungen spezifiziert die physikalische
Umgebung des Systems, die tägliche Betriebszeit, und ob das System ständiger
Beobachtung durch Bediener ausgesetzt ist, oder ein unbeaufsichtigter Betrieb
beabsichtigt ist.

\chapter{Umgebung}

\section{Software}
Software: Gibt an, welche Software zum Betrieb vorhanden sein muss. Eine
Aufteilung für Server und Client ist ggf. sinnvoll. Weiterhin sind unbedingt die
kleinsten benötigten Versionsnummern anzugeben.

\section{Hardware}
Hardware: Hardware-Anforderungen des Systems.

\section{Orgware}
Orgware: Angabe der organisatorische Rahmenbedingungen, die vor Projektstart
erfüllt sein müssen.

\chapter{Funktionalität}
Funktionalität: Spezifikation der einzelnen Produktfunktionen mit genauer und
detaillierter Beschreibung.

\begin{itemize}
  \item Typische Arbeitsabläufe
  \item Keine Angabe von typischen Verwaltungsfunktionen (CRUD \footnote{Create,
Read, Update, Delete}
\end{itemize}

\chapter{Daten}
Daten: Angabe der Daten, die langfristig aus Benutzersicht zu speichern sind.

\chapter{Leistungen}
Leistungen: Anforderungen bezüglich Zeit und Genauigkeit

\chapter{Benutzungsoberfläche}
Benutzungsoberfläche: grundlegende Anforderungen, Zugriffsrechte

\begin{figure}[ht]
  \centering
  \rule{8cm}{6cm}
  \caption{Dies könnte ein Bild der Benutzungsoberfläche sein}
\end{figure}

\chapter{Qualitätsziele}
Qualiätsziele: Allgemeine Ziele sind meistens Änderbarkeit und Wartbarkeit.
Ziele sollten jedoch grundsätzlich messbar, spezifisch und relevant sein.

\chapter{Ergänzungen}
Hier ist Platz für nicht im Pflichtenheft abgedeckte Themengebiete oder ein
Glossar.

% Abbildungsverzeichnis
\listoffigures

\end{document}
</pre>

Gefällt dir das Pflichtenheft? Was kann ich verbessern? Ich würde mich sehr über Kommentare und Anregungen freuen!