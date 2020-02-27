---
id: 1481
title: Varianztypen bei generischen Klassen in Java
date: 2013-02-07T19:40:27+00:00
author: Karl Lorey
layout: page
guid: http://www.karllorey.de/?page_id=1481
---
Es gibt insgesamt vier verschiedene Varianztypen bei generischen Klassen in Java.

  1. Invarianz
  2. Bivarianz
  3. Kovarianz
  4. Kontravarianz

Diese erläutere ich im weiteren Verlauf kurz.

## Invarianz: Class<Type>

Es sind nur Objekte zuweisungskompatibel, die selbst vom Typ _Class<Type>_ sind.

  * Geschrieben werden können nur Objekte des Typs _Type_.
  * Gelesen werden Objekte des Typs _Type_.

### Codebeispiel: Invarianz

<pre class="brush: java; title: ; notranslate" title="">ArrayList&lt;Integer&gt; l = new ArrayList&lt;Integer&gt;();
l.add(3);

// Es sind alle Integer-Methoden verfügbar
 double d = l.get(0).doubleValue()
</pre>

## Bivarianz: Class<?>

Es sind nur Objekte zuweisungskompatibel, die vom Typ _Class<X>_ sind, wobei _X_ ein beliebiger Typ sein kann.

  * Geschrieben werden können beliebige Typen.
  * Gelesen werden Objekte des Typs _Object_.

### Codebeispiel: Bivarianz

<pre class="brush: java; title: ; notranslate" title="">ArrayList&lt;?&gt; l = new ArrayList&lt;Integer&gt;();
 l.add(null);
 l.add("Good Times");
 Object o = l.get(0); // Es kann nur Object zugesichert werden
 </pre>

## Kovarianz: Class<? extends Type>

Es sind nur Objekte zuweisungskompatibel, die vom Typ _Class<X>_ sind, wobei _X_ vom Typ _Type_ &#8211; _X_ also Unterklasse von _Type_ &#8211; sein muss.

  * Geschrieben werden können Objekte des Typs _Type_.
  * Gelesen werden Objekte des Typs _Type_.

### Codebeispiel: Kovarianz

<pre class="brush: java; title: ; notranslate" title="">ArrayList&lt;? extends Number&gt; l = new ArrayList&lt;Integer&gt;();
 l.add(new Integer(3));
 l.add(null);
 Number n = l.get(0);
 </pre>

## Kontravarianz: Class<? super Type>

Es sind nur Objekte zuweisungskompatibel, die vom Typ _Class<X>_ sind, wobei _Type_ vom Typ _X_ &#8211; _X_ also Oberklasse von _Type_ &#8211; sein muss.

  * Geschrieben werden können Objekte des Typs Type.
  * Gelesen werden Objekte des Typs Object.

### Codebeispiel: Kontravarianz

<pre class="brush: java; title: ; notranslate" title="">//ArrayList&lt;? super Number&gt; l = new ArrayList&lt;Integer&gt;(); //funktioniert hier nicht
 ArrayList&lt;? super Number&gt; l = new ArrayList&lt;Object&gt;();
 l.add(73);
 l.add(3.8);
 Object o = l.get(0);
 </pre>