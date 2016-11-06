---
id: 1640
title: 'Java 8: Features und Änderungen im neuen Java'
date: 2013-03-28T10:39:22+00:00
author: Karl Lorey
layout: post
guid: http://www.karllorey.de/?p=1640
permalink: /2013/03/28/java-8-features-und-anderungen-im-neuen-java/
categories:
  - Allgemein
  - Informatik-Studium
tags:
  - Code
  - Informatik
  - Java
  - Java 8
  - Liste
---
Java 8, das im <a href="http://openjdk.java.net/projects/jdk8/" target="_blank">September 2013</a> erscheinen soll, bietet zahlreiche neue Features, diverse Änderungen und kleinere Neuerungen im Detail. Dieser Artikel soll eine grobe Übersicht über die Features und Änderungen in Java 8 geben. <a href="http://www.techempower.com/blog/2013/03/26/everything-about-java-8/" target="_blank">TechEmpower</a> hat hierzu eine detaillierte Liste aller Java 8 Features und Änderungen ausgearbeitet, die ich auf wesentliche Features gekürzt habe.

## Interface-Verbesserungen

Interfaces können in Java 8 nun statische Methoden definieren. Bisher mussten Interfaces aus Libraries stets eine Utility-Klasse mit sich bringen, um eine Grundfunktionalität anbieten zu können. Diese an Interfaces gebundene Utility-Klassen sind fortan aber überflüssig, da die statischen Methoden nun direkt in den Interfaces implementiert werden können, um auf diesen zu arbeiten. Sie müssen nicht mehr in eine extra Utility-Klasse ausgelagert werden.

Weiterhin können in Interfaces nun default-Methoden implementiert werden. Dies wurde auch in vielen Klassen der Java-Standard-Packages direkt umgesetzt. Die Methoden _override_, _equals_, _hashCode_ und _toString_ können jedoch nicht überschrieben werden, da diese von _Object_ bereits implementiert werden.<!--more-->

## Funktionale Interfaces

Eine weitere grundlegende Änderung in Java 8 sind funktionale Interfaces. Funktionale Interfaces sind Interfaces, die genau eine abstrakte Methode definieren. Ein Beispiel hierfür ist _java.lang.Runnable_, da nur eine abstrakte Methode definiert wird:

<pre class="brush: java; title: ; notranslate" title="">public abstract void run();</pre>

Hierzu wurde die Annotation _@FunctionalInterface_ eingeführt, die eine Nutzung als funktionales Interface erzwingt.

## Lambdas

Weitere Neuerung in Java 8 sind Lambdas, die mittels funktionalen Interfaces deklariert werden können. Zum Beispiel kann ein Lambda folgendermaßen aussehen:

<pre class="brush: java; title: ; notranslate" title="">(int x, int y) -&gt; { return x + y; }</pre>

## java.util.function

Neben der Umsetzung von Lambdas in bereits existierenden funktionalen Interfaces, existieren auch neue und womöglich sehr nützliche funktionale Interfaces. Sie wurden im neuen Paket _java.util.function_ untergebracht. Folgende Interfaces stehen also ab Java 8 in diesem Paket zur Verfügung:

  * **Function<T, R>** &#8211; T als Eingabe, R als Rückgabe
  * **Predicate<T>** &#8211; T als Eingabe, boolean als Rückgabe
  * **Consumer<T>** &#8211; T als Eingabe(, Berechnung auf der Eingabe), keine Rückgabe
  * **Supplier<T>** &#8211; keine Eingabe, T als Rückgabe
  * **BinaryOperator<T>** &#8211; Zwei T als Eingabe, Rückgabe eines Ts

## Inferenz-Verbesserungen bei generischen Typen

In manchen Fällen wusste der Java-Compiler bisher nicht, was er mit generischen Typen anfangen sollte. Dann musste ein &#8222;Typ-Zeuge&#8220; eingesetzt werden um zu verhindern, dass der Compiler auf _Object_ als generischen Typ zurückfällt:

<pre class="brush: java; title: ; notranslate" title="">// In Java 7:
foo(Utility&lt;Type&gt;.bar());
Utility.&lt;Type&gt;foo().bar();
</pre>

Durch Verbesserung der generischen Typen kann der Compiler in Java 8 nun viel häufiger aus dem Context auf den generischen Typ schließen:

<pre class="brush: java; title: ; notranslate" title="">// In Java 8:
foo(Utility.bar());
Utility.foo().bar();
</pre>

Dieses Java 8 Feature wird vielen Entwicklern den Umgang mit generischen Typen erleichtern.

## java.time

Auch java.time enthält in Java 8 deutliche Neuerungen. Es werden nun für Monate und Wochentag Enums statt Integer genutzt. Weiterhin sind große Teile der API unveränderbar, was verhindern soll, dass _Date_-Felder versehentlich außerhalb der Klasse geändert werden können.

## Weitere Java 8-Features und -Änderungen

  * Komplett neues java.util.stream-Paket
  * Collections API Erweiterungen
  * Concurrency API Erweiterungen
  * IO/NIO API Erweiterungen
  * Änderungen an Reflections und Annotation
  * Nashorn JavaScript Engine
  * Diverse Änderungen an java.lang, java.util, and java.sql

Quelle: Sehr umfangreiche Übersicht wirklich aller Java 8-Features und -Änderungen von <a href="http://www.techempower.com/blog/2013/03/26/everything-about-java-8/" target="_blank">TechEmpower</a>.