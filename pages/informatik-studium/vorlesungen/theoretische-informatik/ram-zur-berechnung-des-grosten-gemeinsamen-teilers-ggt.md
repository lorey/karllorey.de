---
id: 751
title: RAM zur Berechnung des größten gemeinsamen Teilers (ggT)
date: 2012-01-05T19:50:26+00:00
author: Karl Lorey
layout: page
guid: http://www.karllorey.de/?page_id=751
---
<pre class="brush: plain; title: ; notranslate" title="">0 R2 &lt;- R0 - R1
1 IF R2 &gt; 0 GOTO 3
2 R2 &lt;- R1 - R0
3 R0 &lt;- R1
4 R1 &lt;- R2
5 IF R1 &gt; 0 GOTO 0
6 STOP
</pre>