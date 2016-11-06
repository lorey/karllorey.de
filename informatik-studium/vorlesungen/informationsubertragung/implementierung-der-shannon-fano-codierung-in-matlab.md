---
id: 732
title: Implementierung der Shannon-Fano-Codierung in MATLAB
date: 2012-01-05T19:30:41+00:00
author: Karl Lorey
layout: page
guid: http://www.karllorey.de/?page_id=732
---
_codeShannonFano_ nimmt die Auftrittswahrscheinlichkeit der Buchstaben eines beliebigen Alphabets als Eingabe und erzeugt eine Codierung nach Shannon-Fano als Ausgabe.

## Aufruf der Shannon-Fano-Codierung

<pre class="brush: plain; title: ; notranslate" title="">codeShannonFano([0.5 0.2 0.2 0.1]);
</pre>

## Implementierung der Shannon-Fano-Codierung

<pre class="brush: plain; title: ; notranslate" title="">function [ codewoertersf ] = codeShannonFano( codewoerter )
%codeShannonFano Codiert nach dem Shannon-Fano-Verfahren
%   Liefert die codierten CWs zurueck
if (length(codewoerter) == 1)
    codewoertersf = {''};
else
    %% divide
    half = 1;
    % ermittle ungefaehre Mitte der Wahrscheinlichkeiten
    while (sum(codewoerter(1:half))) &lt; (0.5 * sum(codewoerter))
        half = half + 1;
    end

    %% conquer
    % rufe die Methode rekursiv auf und speichere die sf-codewoerter
    ersterteil = codeShannonFano(codewoerter(1:half));
    zweiterteil = codeShannonFano(codewoerter((half+1):end));

    %% combine
    % erstelle eine cell mit der selben groesse wie die variable
    % codewoerter
    codewoertersf = cell(size(codewoerter));
    % setze an anfang der sf-codewoerter des ersten teils eine 0
    j = 1;
    for i=1:half
        codewoertersf{i} = ['0', ersterteil{j}];
        j = j + 1;
    end

    %setze an anfang der sf-codewoerter des zweiten teils eine 1
    j = 1;
    for i=(half+1):length(codewoerter)
        codewoertersf{i} = ['1', zweiterteil{j}];
        j= j + 1;
    end
end
end

</pre>