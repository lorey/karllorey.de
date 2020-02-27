---
id: 728
title: Rückgekoppeltes Schieberegister in MATLAB
date: 2012-01-05T19:29:34+00:00
author: Karl Lorey
layout: page
guid: http://www.karllorey.de/?page_id=728
---
Aufgabe: Nachbau des rückgekoppelten Schieberegisters aus der
  
Vorlesung. Das Generator-Polynom M(u) und der Initialzustand
  
des Schieberegisters sollen frei wählbar sein.

## Ausgabe bzw. Aufruf des Schieberegisters

<pre class="brush: plain; title: ; notranslate" title="">polynom = [1 0 1 1];
inhalt = [0 0 1];
for i=0:16
    disp(['Takt ', num2str(i, 2), ', Schieberegisterinhalt ', num2str(inhalt)]);
    inhalt = ShiftSR(inhalt, polynom);
end
</pre>

## Simulation des Schieberegisters

<pre class="brush: plain; title: ; notranslate" title="">polynom = [1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1];
inhalt = [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1];
%% Initialisierung
for i=1:5000
    inhalt = ShiftSR(inhalt, polynom);
end
%% Ausgabe der zehn Takte
for i=1:10
    zufallszahl = [0 0 0 0 0 0 0 0];
    for j=1:8
        inhalt = ShiftSR(inhalt, polynom);
        zufallszahl(j) = inhalt(end);
    end
    disp([num2str(zufallszahl(1)),' ', num2str(zufallszahl(2)),' ', ...
        num2str(zufallszahl(3)),' ', num2str(zufallszahl(4)),' ', ...
        num2str(zufallszahl(5)),' ', num2str(zufallszahl(6)),' ', ...
        num2str(zufallszahl(7)),' ', num2str(zufallszahl(8))]);
end
</pre>

## ShiftSR-Funktion

<pre class="brush: plain; title: ; notranslate" title="">function [ inhalt ] = ShiftSR( inhalt, polynom )
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
inhalt = fliplr(inhalt); % polynom und inhalt invertieren
polynom = fliplr(polynom);
inhaltAlt = inhalt;
    for i=1:length(inhalt)
        if (polynom(i) == 1 && i~= 1) %rueckkopplung vorhanden
            inhalt(i) = bitxor(inhaltAlt(i-1), inhaltAlt(length(inhalt)));
        else %erstes element oder keine rk
            inhalt(i) = inhaltAlt(mod((i-2), length(inhalt)) + 1);
        end
    end
inhalt = fliplr(inhalt);
end
</pre>

## ShiftSRfast als Alternative zu ShiftSR

<pre class="brush: plain; title: ; notranslate" title="">function [ inhalt ] = ShiftSRfast( inhalt, polynom )
%ShiftSRfast Schneller Shift des LFSR
%   Implementierung ohne Schleife

% Verschieben des Polynoms um eins nach links (= multiplikation mal u)
% wenn letztes element inhalt(1) == 1, dann addition modulo 2 bzw. XOr mit
% Polynom, da dieses die Rückschaltungen darstellt
inhalt = mod(([inhalt(2:end) 0] + inhalt(1) * polynom(2:end)), 2);
end
</pre>