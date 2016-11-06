---
id: 1594
title: 'Java: Hello World &#8211; verblüffend statt einfach'
date: 2013-03-19T15:42:14+00:00
author: Karl Lorey
layout: post
guid: http://www.karllorey.de/?p=1594
permalink: /2013/03/19/java-hello-world-verbluffend-statt-einfach/
categories:
  - Informatik-Studium
tags:
  - Anleitung
  - Code
  - Hello World
  - Informatik
  - Java
  - Stack Overflow
---
Wer statt dem doch relativ langweiligen Hello-World-Programm

<pre class="brush: java; title: ; notranslate" title="">System.out.println("hello world");
</pre>

einmal außergewöhnlichen Java-Code nutzen will, um in Java &#8222;hello world&#8220; auf der Konsole auszugeben, der wird sich wahrscheinlich über folgendes Hello-World-Beispiel in Java freuen:

<pre class="brush: java; title: ; notranslate" title="">System.out.println(randomString(-229985452) + " "
    + randomString(-147909649));
</pre>

<!--more-->Die 

_randomString_-Methode sieht dabei folgendermaßen aus:

<pre class="brush: java; title: ; notranslate" title="">public static String randomString(int i)
{
    Random ran = new Random(i);
    StringBuilder sb = new StringBuilder();
    for (int n = 0; ; n++)
    {
        int k = ran.nextInt(27);
        if (k == 0)
            break;

        sb.append((char)('`' + k));
    }

    return sb.toString();
}
</pre>

Das angegebene Beispiel gibt, wie der Standard-Code für Hello World in Java, genauso &#8222;hello world&#8220; auf der Konsole aus.

Diese Ausgabe von &#8222;hello world&#8220; wird umständlicher, jedoch auf sehr verblüffende Weise erreicht &#8211; nämlich mit Zufallszahlen (durch ein _Random_-Objekt -> java.util.Random).

Doch wie funktioniert es, dass trotz der Nutzung von Zufallszahlen jedes Mal &#8222;hello world&#8220; erzeugt wird?

## Warum wird so &#8222;Hello World&#8220; ausgegeben?

Mit den zwei Methodenaufrufen _randomString(-229985452)_ und _randomString(-147909649)_ wird jeweils als Parameter ein Integer-Wert _i_ zur Initialisierung der Random-Objekte übergeben. Was bewirkt eine Initialisierung von _Random_ mit einem Integer?

### Zufallszahlen sind nicht zufällig

Zur Ausgabe von &#8222;hello world&#8220; wird die Tatsache ausgenutzt, dass Zufallszahlen in Computern nie wirklich zufällig, sondern nur pseudozufällig sind. Pseudozufällig heißt, dass diese Zufallszahlen nicht wirklich zufällig entstehen, sondern von einem Algorithmus generiert (also berechnet) werden müssen. Dieser Algorithmus wird normalerweise (ohne Übergabe eines Integers bei new Random()) mit einem möglichst zufälligen Wert, dem Seed, initialisiert. Mit diesem Seed berechnet der Zufallszahlen-Generator dann jede Zahl. Bei einer Initialisierung mit dem gleichen Seed werden so also auch gleiche &#8222;Zufallszahlen&#8220; erzeugt. In der Praxis wird der Seed aus einer Kombination der Uhrzeit und einem Counter berechnet, so dass er relativ zufällig, schwer zu erraten und die Generierung von zwei gleichen Seeds sehr unwahrscheinlich ist.

In diesem Fall wird der Seed aber manuell übergeben und nicht möglichst zufällig berechnet. **Es wird die Eigenschaft genutzt, dass durch die Initalisierung von Random mit einer festen Zahl, in diesem Fall -229985452, immer die selben Zahlen generiert werden.** Bei einem Aufruf sind die Zahlen dann immer gleich:

<pre class="brush: java; title: ; notranslate" title="">Random r = new Random(-229985452);
int acht = r.nextInt(27);
int fuenf = r.nextInt(27);
int zwoelf = r.nextInt(27);
// usw.
</pre>

So kann man also nacheinander und zwar jedes Mal und auf jedem Rechner folgende Zahlen generieren:

<pre class="brush: plain; title: ; notranslate" title="">8
5
12
12
15
0
</pre>

Und bei der Initialisierung mit -147909649 immer folgende Zahlen generieren:

<pre class="brush: plain; title: ; notranslate" title="">23
15
18
12
4
0
</pre>

Doch wie ist es möglich, dass &#8222;hello world&#8220; aus diesen Zahlen wird?

## Wie wird aus Zufallszahlen &#8222;hello world&#8220;?

Innerhalb der Schleife werden also bei beiden Aufrufen immer die oben genannten Zahlen generiert. Die Zahlen werden dann zu dem Zeichen &#8222;\`&#8220; (Nr. 96) addiert. Das Ergebnis dieser Addition ist ein Integer, der für ein Zeichen im Alphabet steht. Mit einem Casting zu char wird aus dem Integer dann schlussendlich ein Zeichen, welches an den String angehängt werden kann. So entsteht char für char erst beim ersten Aufruf der String &#8222;hello&#8220; und beim zweiten Aufruf dann &#8222;world&#8220;:

### Generierung von &#8222;hello world&#8220;

<table>
  <tr>
    <td>
      Generierte Zahl
    </td>
    
    <td>
      Offset
    </td>
    
    <td>
      Ergebnis der Addition: &#8218;`&#8216; + k
    </td>
    
    <td>
      Buchstabe (char)
    </td>
  </tr>
  
  <tr>
    <td>
      8
    </td>
    
    <td>
      96
    </td>
    
    <td>
      104
    </td>
    
    <td>
      h
    </td>
  </tr>
  
  <tr>
    <td>
      5
    </td>
    
    <td>
      96
    </td>
    
    <td>
      101
    </td>
    
    <td>
      e
    </td>
  </tr>
  
  <tr>
    <td>
      12
    </td>
    
    <td>
      96
    </td>
    
    <td>
      108
    </td>
    
    <td>
      l
    </td>
  </tr>
  
  <tr>
    <td>
      12
    </td>
    
    <td>
      96
    </td>
    
    <td>
      108
    </td>
    
    <td>
      l
    </td>
  </tr>
  
  <tr>
    <td>
      15
    </td>
    
    <td>
      96
    </td>
    
    <td>
      111
    </td>
    
    <td>
      o
    </td>
  </tr>
  
  <tr>
    <td>
    </td>
    
    <td>
    </td>
    
    <td>
      break -> return &#8222;hello&#8220;
    </td>
    
    <td>
    </td>
  </tr>
  
  <tr>
    <td>
      23
    </td>
    
    <td>
      96
    </td>
    
    <td>
      119
    </td>
    
    <td>
      w
    </td>
  </tr>
  
  <tr>
    <td>
      15
    </td>
    
    <td>
      96
    </td>
    
    <td>
      111
    </td>
    
    <td>
      o
    </td>
  </tr>
  
  <tr>
    <td>
      18
    </td>
    
    <td>
      96
    </td>
    
    <td>
      114
    </td>
    
    <td>
      r
    </td>
  </tr>
  
  <tr>
    <td>
      12
    </td>
    
    <td>
      96
    </td>
    
    <td>
      108
    </td>
    
    <td>
      l
    </td>
  </tr>
  
  <tr>
    <td>
      4
    </td>
    
    <td>
      96
    </td>
    
    <td>
      100
    </td>
    
    <td>
      d
    </td>
  </tr>
  
  <tr>
    <td>
    </td>
    
    <td>
    </td>
    
    <td>
      break -> return &#8222;world&#8220;
    </td>
    
    <td>
    </td>
  </tr>
</table>

Die erzeugten Strings werden dann verkettet und am Schluss als &#8222;hello world&#8220; auf der Konsole ausgegeben.

Vielleicht gelingt es einigen von euch mit diesem Hello-World-Programm in Java andere zu verblüffen&#8230;

Quelle: <a href="http://stackoverflow.com/questions/15182496/why-does-this-code-print-hello-world" target="_blank">Stack Overflow</a>
  
Lizenz: <a href="http://creativecommons.org/licenses/by-sa/3.0/" target="_blank">CC BY-SA 3.0</a>. Ich würde mich über eine Verlinkung freuen!