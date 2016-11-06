---
id: 752
title: Simulation einer Turing-Maschine durch ein Python-Programm
date: 2012-01-05T19:50:16+00:00
author: Karl Lorey
layout: page
guid: http://www.karllorey.de/?page_id=752
---
<pre class="brush: python; title: ; notranslate" title="">def dr(x):
    # liefert eine Liste mit den dyadischen Ziffern von x
    # z.B. dr(20) == [1, 2, 1, 2]
    list = []
    while (x &gt; 0):
        half = (x // 2)
        if ((half + half) == x):
            list = [2] + list
            x = (half - 1)
        else:
            list = [1] + list
            x = half
    return list

def number(l):
    # liefert den Wert der durch die Liste l dargestellten dyadischen Zahl
    # z.B. Number([1, 2, 1, 2]) == 20
    k = 1
    number = 0
    i = 0
    while(i &lt; len(l)): # gehe Elemente von hinten nach vorne durch
        number = (number + (l[(len(l) - (i + 1))] * k))
        k = 2 * k
        i = (i + 1)
    return number

def main(x):
    # Zustand z0
    z = 0
    # dya(x) auf Band 1 schreiben und 0=Leerzeichen
    # anhängen, wegen dya(0) = leeres Wort
    b1 = dr(x) + [0]
    # Band 2 ist leer
    b2 = [0]
    # beide Köpfe stehen auf Position 0
    h1 = 0
    h2 = 0
    # solange Stoppzustand nicht erreicht
    while (z != 1):
        # (z0,1,_)-&gt;(z0,_,1,R,L)
        if (z == 0 and b1[h1] == 1 and b2[h2] == 0):
            z = 0 # gehe in Zustand z0
            b1[h1] = 0 # schreibe a0 auf Band 1
            b2[h2] = 1 # schreibe a1 auf Band 2
            h1 = (h1 + 1) # gehe auf Band 1 nach rechts
            h2 = (h2 - 1) # gehe auf Band 2 nach links
        # (z0,2,_)-&gt;(z0,_,2,R,L)
        elif (z == 0 and b1[h1] == 2 and b2[h2] == 0):
            z = 0 # gehe in Zustand z0
            b1[h1] = 0 # schreibe a0 auf Band 1
            b2[h2] = 2 # schreibe a2 auf Band 2
            h1 = (h1 + 1) # gehe auf Band 1 nach rechts
            h2 = (h2 - 1) # gehe auf Band 2 nach links
        # (z0,_,_)-&gt;(z2,_,_,R,R)
        elif (z == 0 and b1[h1] == 0 and b2[h2] == 0):
            z = 2 # gehe in Zustand z2
            b1[h1] = 0 # schreibe a0 auf Band 1
            b2[h2] = 0 # schreibe a0 auf Band 2
            h1 = (h1 + 1) # gehe auf Band 1 nach rechts
            h2 = (h2 + 1) # gehe auf Band 2 nach rechts
        # (z2,_,1)-&gt;(z2,1,_,R,R)
        elif (z == 2 and b1[h1] == 0 and b2[h2] == 1):
            z = 2 # gehe in Zustand z2
            b1[h1] = 1 # schreibe a1 auf Band 1
            b2[h2] = 0 # schreibe a0 auf Band 2
            h1 = (h1 + 1) # gehe auf Band 1 nach rechts
            h2 = (h2 + 1) # gehe auf Band 2 nach rechts
        # (z2,_,2)-&gt;(z2,2,_,R,R)
        elif (z == 2 and b1[h1] == 0 and b2[h2] == 2):
            z = 2 # gehe in Zustand z2
            b1[h1] = 2 # schreibe a2 auf Band 1
            b2[h2] = 0 # schreibe a0 auf Band 2
            h1 = (h1 + 1) # gehe auf Band 1 nach rechts
            h2 = (h2 + 1) # gehe auf Band 2 nach rechts
        # (z2,_,_)-&gt;(z3,_,_,L,O)
        elif (z == 2 and b1[h1] == 0 and b2[h2] == 0):
            z = 3 # gehe in Zustand z3
            b1[h1] = 0 # schreibe a0 auf Band 1
            b2[h2] = 0 # schreibe a0 auf Band 2
            h1 = (h1 - 1) # gehe auf Band 1 nach links
            h2 = (h2 + 0) # bleibe stehen auf Band 2
        # (z3,1,_)-&gt;(z3,1,_,L,O)
        elif (z == 3 and b1[h1] == 1 and b2[h2] == 0):
            z = 3 # gehe in Zustand z3
            b1[h1] = 1 # schreibe a1 auf Band 1
            b2[h2] = 0 # schreibe a0 auf Band 2
            h1 = (h1 - 1) # gehe auf Band 1 nach links
            h2 = (h2 + 0) # bleibe stehen auf Band 2
        # (z3,2,_)-&gt;(z3,2,_,L,O)
        elif (z == 3 and b1[h1] == 2 and b2[h2] == 0):
            z = 3 # gehe in Zustand z3
            b1[h1] = 2 # schreibe a2 auf Band 1
            b2[h2] = 0 # schreibe a0 auf Band 2
            h1 = (h1 - 1) # gehe auf Band 1 nach links
            h2 = (h2 + 0) # bleibe stehen auf Band 2
        # (z3,_,_)-&gt;(z1,_,_,R,O)
        elif (z == 3 and b1[h1] == 0 and b2[h2] == 0):
            z = 1 # gehe in Zustand z1
            b1[h1] = 0 # schreibe a0 auf Band 1
            b2[h2] = 0 # schreibe a0 auf Band 2
            h1 = (h1 + 1) # gehe auf Band 1 nach rechts
            h2 = (h2 + 0) # bleibe stehen auf Band 2
        # Ende erreicht
        if (h1 == len(b1)): # falls Ende auf Band 1 erreicht
            b1 = b1 + [0]
        if (h2 == len(b2)): # falls Ende auf Band 2 erreicht
            b2 = b2 + [0]
        # Anfang erreicht
        if (h1 == -1): # falls Ende auf Band 1 erreicht
            h1 = 0
            b1 = [0] + b1
        if (h2 == -1): # falls Ende auf Band 2 erreicht
            h2 = 0
            b2 = [0] + b2
    i = 0
    numlist = []
    while (b1[i] == 0):
        i = (i + 1)
    while (i &lt; len(b1) and b1[i] != 0):
        numlist = numlist + [b1[i]]
        i = (i + 1)
    while (i &lt; len(b1)):
        if (b1[i] != 0):
            return undef
        i = (i + 1)
    return number(numlist)
</pre>