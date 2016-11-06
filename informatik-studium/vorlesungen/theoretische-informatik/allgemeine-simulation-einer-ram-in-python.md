---
id: 1556
title: Allgemeine Simulation einer RAM in Python
date: 2013-02-25T14:43:23+00:00
author: Karl Lorey
layout: page
guid: http://www.karllorey.de/?page_id=1556
---
Die Funktionen _read_ und _write_ müssen aus den Folien entnommen werden, da diese nicht von mir, sondern von <a href="http://theoretische.informatik.uni-wuerzburg.de/mitarbeiter/christian_glasser/" target="_blank">Dr. Glaßer</a> stammen und ich sie deshalb nicht veröffentlichen kann und darf.

<pre class="brush: python; title: ; notranslate" title=""># vgl. VL
def read(u,v,a): # liefert den Inhalt von Ra
    # siehe VL

# vlg. VL
def write(u,v,a,b): # schreibt b in Ra
    # siehe VL

def ramsimn(ramcode,params):
    #initialisierung der listen
    u = []
    v = []
    i = 0
    for value in params:
        write(u,v,i,value)
        i = i + 1

    br = 0
    while (ramcode[br][0] != 9):
        # Auslesen der Ram-Befehls-Nummer
        command = ramcode[br][0]

        # Parameter zur Vereinfachung setzen
        i = ramcode[br][1]
        j = ramcode[br][2]
        k = ramcode[br][3]

        # command 0: Ri &lt;- Rj
        if (command == 0):
            x = read(u,v,j)
            write(u,v,i,x)
            br = br + 1

        # command 1: Ri &lt;- RRj
        elif (command == 1):
            x = read(u,v,j)
            y = read(u,v,x)
            write(u,v,i,y)
            br = br + 1

        # command 2: RRi &lt;- Rj
        elif (command == 2):
            ri = read(u,v,i)
            rj = read(u,v,j)
            write(u,v,ri,rj)
            br = br + 1

        # command 3: Ri &lt;- j
        elif (command == 3):
            write(u,v,i,j)
            br = br + 1

        # command 4: Ri &lt;- Rj + Rk
        elif (command == 4):
            x = read(u,v,j) + read(u,v,k)
            write(u,v,i,x)
            br = br + 1

        # command 5: Ri &lt;- Rj - Rk
        elif (command == 5):
            x = read(u,v,j) - read(u,v,k)
            if (x &lt; 0):
                x = 0
            write(u,v,i,x)
            br = br + 1

        # command 6: GOTO i
        elif (command == 6):
            br = i

        # command 7: IF Ri = 0 GOTO j
        elif (command == 7):
            if (read(u,v,i) == 0):
                br = j
            else:
                br = br + 1

        # command 8: IF Ri &gt; 0 GOTO j
        elif (command == 8):
            if (read(u,v,i) &gt; 0):
                br = j
            else:
                br = br + 1

    return v[0]
</pre>