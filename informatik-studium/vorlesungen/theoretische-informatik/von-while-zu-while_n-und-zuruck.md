---
id: 1555
title: Von WHILE zu WHILE_N und zurück
date: 2013-02-25T14:44:58+00:00
author: Karl Lorey
layout: page
guid: http://www.karllorey.de/?page_id=1555
---
<pre class="brush: python; title: ; notranslate" title="">def divtwo(x):
    d = 0
    while(x &gt;= 2):
        z1 = 1
        z2 = 2
        while((z2 + z2) &lt;= x):
            z1 = z2
            z2 = (z1 + z1)
        x = (x - z2)
        d = (d + z1)
    return d

# codeZ(x)
def z2n(z):
    n = (z + z)
    if (z &lt; 0):
        n = ((0 - n) - 1)
    return n

# codeZ^-1(x)
def n2z(n):
    z = divtwo(n)
    if ((z + z) &lt; n):
        z = ((0 - z) - 1)
    return z

def fn(x,y):
    return z2n(f(n2z(x),n2z(y)))

def h(x,y):
    return n2z(g(z2n(x),z2n(y)))
</pre>