---
id: 818
title: Übungsblatt 4
date: 2012-01-15T19:00:33+00:00
author: Karl Lorey
layout: page
guid: http://www.karllorey.de/?page_id=818
---
## Aufgabe 8 (Projektion)

Gegeben: Ein Relationenschema R = (U,F) mit

  * U = {A, B, C, D, E, F}
  * F = {A->E, BE->F, CF->D}

Zu bestimmen: Die Projektion von F auf V = {A, B, C, D}

Man startet mit ABC als Teilmenge von ABCD und kommt so auf folgenden Rechenweg: ABC->BCE->CF->D
  
Die Projektion von F auf V ist also {ABC->D}

## Aufgabe 9 (3NF-Synthese)

a)

K ist der eindeutige Schlüssel, daher folgt:
  
K->N, K->I, K->P, K->F, K->S, K->B

Ist die Postleitzahl gleich, dann hat ein Kunde auch die gleiche Filiale:
  
P->F

Ist die Filiale, der Status und der Anfangsbuchstabe gleich, so ist auch der Berater gleich:
  
FSI->B

Bei gleichem Namen haben zwei Kunden natürlich auch den gleichen Anfangsbuchstaben:
  
N->I

b)

  1. K->P->K
  2. K->FSI->B
  3. K->N->I

R ist also nicht in 3NF.

c) F* = BASIS(F) und damit sind nur noch die Variablen jeder Abhängigkeit (fd) als Projektionsmenge zu wählen.

## Aufgabe 10 (BCNF-Dekomposition)

a) Eine Menge aus Variablen V ist ein Schlüssel, wenn sie auf alle Variablen U eines Datenbankschemas R = (U, F) abbildet: {V}+ = U.

Die gibt für alle Mengen mit der Teilmenge {G,H,I} und mindestens einem Element aus {A,B,C}

b) Nein, da A, B oder C von nicht von Schlüsselkandidaten abhängig sind.

c) Es ist eine BCNF-Zerlegung mittels des BCNF-Dekompositionsalgorithmus zu erzeugen.

Statt den Baum zu visualisieren, erkläre ich kurz die Schritte von der Wurzel zu den Blättern.

  * ABCGHI (Wurzel) nach ABGH (linker Ast) und ACGHI (rechter Ast) mittels AGH->B (angewandte Regel)
  * ACGHI nach ACGI und CGHI mit CGI->A
  * Die Blätter entsprechen nun einer korrekten BCNF-Zerlegung

d) Es ist mit dem Tableau-Algorithmus zu zeigen, dass D verlustfrei ist.

<table>
  <tr>
    <th>
      A
    </th>
    
    <th>
      B
    </th>
    
    <th>
      C
    </th>
    
    <th>
      G
    </th>
    
    <th>
      H
    </th>
    
    <th>
      I
    </th>
  </tr>
  
  <tr>
    <td>
      a
    </td>
    
    <td>
      a
    </td>
    
    <td>
      b1
    </td>
    
    <td>
      a
    </td>
    
    <td>
      a
    </td>
    
    <td>
      b1
    </td>
  </tr>
  
  <tr>
    <td>
      a
    </td>
    
    <td>
      b2
    </td>
    
    <td>
      a
    </td>
    
    <td>
      a
    </td>
    
    <td>
      b2
    </td>
    
    <td>
      a
    </td>
  </tr>
  
  <tr>
    <td>
      b3
    </td>
    
    <td>
      b3
    </td>
    
    <td>
      a
    </td>
    
    <td>
      a
    </td>
    
    <td>
      a
    </td>
    
    <td>
      a
    </td>
  </tr>
</table>

Die unterste Zeile lässt sich mit Hilfe von CGI->A und anschließend AGH->B in eine a-Zeile transformieren und ist somit verlustfrei.

e) Die Zerlegung ist nicht unabhängig, da BHI->C verloren geht und per Join ermittelt werden muss.