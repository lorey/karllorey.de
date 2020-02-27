---
id: 750
title: While-Programm zur Binärdarstellung
date: 2012-01-05T19:50:23+00:00
author: Karl Lorey
layout: page
guid: http://www.karllorey.de/?page_id=750
---
<pre class="brush: python; title: ; notranslate" title="">def divtwo(n):
    if (n &lt; 2):
         half = 0
     else:
         half = n
         while ((half + half) &gt; n):
            half = (half - 1)
    return half

def bin(n): # Vorgehen wie in Vorlesung
    if (n &lt; 1):
        print(0)
    else:
        half = divtwo(n)

        if (half != 0): # Entfernt überflüssige 0
            bla = bin(half)

        if ((half + half) &lt; n): # Prüfe ob Rest bei Division enstanden ist
             print(1) # rest -&gt; 1
        else:
            print(0) # kein rest -&gt; 0

    return -1
</pre>