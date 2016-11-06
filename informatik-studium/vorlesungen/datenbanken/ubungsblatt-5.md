---
id: 816
title: Übungsblatt 5
date: 2012-01-15T18:59:16+00:00
author: Karl Lorey
layout: page
guid: http://www.karllorey.de/?page_id=816
---
## Zusatzaufgabe 12 (Azyklische 3NF-Zerlegung)

Gegeben: Ein Relationenschema R = (U,F) mit

  * U = {A, B, C, D, E}
  * F = {B->A, C->B, CD->E}

a) Es ist mit dem GYO-Algorithmus zu zeigen, dass die gegebene 3NF-Zerlegung D={AB, BC, CDE} azyklisch ist. Dies ist der Fall, da der resultierende Hypergraph leer ist. (Grafiken bzw. PDFs reiche ich nach)

b) Es ist ein Join-Tree und ein voll reduzierendes Semi-Join-Programm anzugeben.
  
Join Tree: AB->BC->CDE, wobei U1=AB, U2=BC und U3=CDE
  
Daraus ergibt sich folgendes Semi-Join-Programm:
  
r2 = r2 >< r3
  
r1 = r1 >< r2
  
&#8211;
  
r2 = r2 >< r1
  
r3 = r3 >< r2

d) Es ist eine erlaubte Datenbankinstanz d von D anzugeben, die nicht global konsistent
  
ist, wobei jede Relation aus der Reduktion mindestens 3 Tupel zu enthalten hat.

**U1**

<table>
  <tr>
    <th>
      A
    </th>
    
    <th>
      B
    </th>
  </tr>
  
  <tr>
    <td>
      1
    </td>
    
    <td>
      1
    </td>
  </tr>
  
  <tr>
    <td>
      2
    </td>
    
    <td>
      2
    </td>
  </tr>
  
  <tr>
    <td>
      3
    </td>
    
    <td>
      3
    </td>
  </tr>
  
  <tr>
    <td>
      4
    </td>
    
    <td>
      4
    </td>
  </tr>
</table>

**U2**

<table>
  <tr>
    <th>
      B
    </th>
    
    <th>
      C
    </th>
  </tr>
  
  <tr>
    <td>
      1
    </td>
    
    <td>
      1
    </td>
  </tr>
  
  <tr>
    <td>
      2
    </td>
    
    <td>
      2
    </td>
  </tr>
  
  <tr>
    <td>
      3
    </td>
    
    <td>
      3
    </td>
  </tr>
  
  <tr>
    <td>
      5
    </td>
    
    <td>
      4
    </td>
  </tr>
</table>

**U3**

<table>
  <tr>
    <th>
      C
    </th>
    
    <th>
      D
    </th>
    
    <th>
      E
    </th>
  </tr>
  
  <tr>
    <td>
      1
    </td>
    
    <td>
      1
    </td>
    
    <td>
      1
    </td>
  </tr>
  
  <tr>
    <td>
      2
    </td>
    
    <td>
      2
    </td>
    
    <td>
      2
    </td>
  </tr>
  
  <tr>
    <td>
      3
    </td>
    
    <td>
      3
    </td>
    
    <td>
      3
    </td>
  </tr>
  
  <tr>
    <td>
      6
    </td>
    
    <td>
      6
    </td>
    
    <td>
      6
    </td>
  </tr>
</table>

## Aufgabe 13 (Zyklische 3NF- und BCNF-Zerlegungen)

Gegeben: Relationenschema R = (U,F) mit

  * U = {A, B, C, G, H, I}
  * F = {AGH->B, BHI->C, CGI->A}

a) Es ist eine 3NF-Zerlegung mit dem Synthese-Algorithmus zu bestimmen.

F* = F = {AGH->B, BHI->C, CGI->A}

Die Zerlegungen sind ABGH, BCHI, ACGI und AGHI (AGHI wird im letzten Schritt als Oberschlüssel hinzugefügt)

b) Mit dem GYO-Algorithmus ist zu zeigen, dass die erzeugte Zerlegung zylisch ist.

Keine der Regeln des GYO-Algorithmus kann angewendet werden. Der Hypergraph ist also zyklisch.

c) Es ist zu zeigen, dass die Zerlegung ABGH, BCHI und AGHI mit dem BCNF-Dekompositionsalgorithmus erzeugt werden kann.

Statt den Baum zu visualisieren, erkläre ich kurz die Schritte von der Wurzel zu den Blättern.

  * ABCGHI (Wurzel) nach ABGH (linker Ast) und ACGHI (rechter Ast) mittels AGH->B (angewandte Regel)
  * ACGHI nach BCHI und AGHI mit BHI->C
  * Die Blätter entsprechen nun der angegebenen Zerlegung.

d) Es ist mit dem GYO-Algorithmus zu zeigen, dass die erzeugte Zerlegung zyklisch ist.

Der GYO-Algorithmus liefert keinen leeren Hypergraphen. Die gegebene Zerlegung ist also zyklisch.