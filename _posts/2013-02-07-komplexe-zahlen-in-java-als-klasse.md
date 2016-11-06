---
id: 1380
title: Komplexe Zahlen in Java als Klasse
date: 2013-02-07T13:23:13+00:00
author: Karl Lorey
layout: post
guid: http://www.karllorey.de/?p=1380
permalink: /2013/02/07/komplexe-zahlen-in-java-als-klasse/
categories:
  - Informatik-Studium
tags:
  - Informatik
  - Java
  - komplexe Zahlen
  - Musterlösung
  - Objektorientiertes Programmieren
  - Studium
  - Übungsblatt
  - Uni Würzburg
  - Vorlesung
  - Wintersemester 2012/2013
---
Eine Aufgabe in der Vorlesung &#8222;Objektorientiertes Programmieren&#8220; war es, eine Klasse _ComplexNumber_ zur Repräsentation einer komplexen Zahl in Java zu erstellen. Meine kommentierte Musterlösung hilft hoffentlich auch einigen anderen Studenten. Hierzu sollten auch _clone_, _equals_, _hashCode_ und _toString_ sinnvoll überschrieben werden.<!--more-->

Die zusammenhängende, unkommentierte Klasse ist übrigens unter &#8222;Informatik-Studium &#8211; Vorlesungen &#8211; Objektorientiertes Programmieren &#8211; [Komplexe Zahl als Klasse in Java](http://www.karllorey.de/informatik-studium/vorlesungen/objektorientiertes-programmieren/komplexe-zahl-als-klasse-in-java/ "Komplexe Zahl als Klasse in Java")&#8220; zu finden.

<pre class="brush: java; title: ; notranslate" title="">/**
 * Repräsentation einer komplexen Zahl.
 *
 * @author Karl Lorey
 * @version 1.0.0
 *
 */
public class ComplexNumber {
</pre>

## Attribute

Zunächst müssen die Eigenschaften einer komplexen Zahl als Attribute dargestellt werden. Dies sind der Real- und der Imaginär-Teil der jeweiligen Zahl.

<pre class="brush: java; title: ; notranslate" title="">/**
	 * Realteil.
	 */
	double re;

	/**
	 * Imaginärteil
	 */
	double im;
</pre>

## Konstruktoren

Weiterhin sind für die komplexe Zahl Konstruktoren zur Erstellung einer komplexen Zahl zu definieren. Zunächst ein Konstruktor zum Erstellen der Zahl 0.

<pre class="brush: java; title: ; notranslate" title="">/**
	 * Erstellt 0.
	 */
	public ComplexNumber() {
		this(0);
	}
</pre>

Weiterhin ein konstruktor, zum Erstellen einer reellen Zahl. Eine reelle Zahl ist eine komplexe Zahl mit 0 als Imaginärteil. Es wird der Konstruktor zum Erstellen einer komplexen Zahl aufgerufen und 0 als imaginärteil übergeben.

<pre class="brush: java; title: ; notranslate" title="">/**
	 * Erstellt eine reelle Zahl.
	 *
	 * @param real
	 *            Reelle Zahl.
	 */
	public ComplexNumber(double real) {
		this(real, 0);
	}
</pre>

Der Konstruktor zum Erstellen einer &#8222;normalen&#8220; komplexen Zahl.

<pre class="brush: java; title: ; notranslate" title="">/**
	 * Erstellt eine komplexe Zahl.
	 *
	 * @param real
	 *            Realteil.
	 * @param img
	 *            Imaginärteil.
	 */
	public ComplexNumber(double real, double img) {
		this.re = real;
		this.im = img;
	}
</pre>

Um mit einer komplexen Zahl schnell eine weitere komplexe Zahl zu instanziieren zu können, existiert ein Konstruktor, der eine andere komplexe Zahl dupliziert.

<pre class="brush: java; title: ; notranslate" title="">/**
	 * Erstellt eine komplexe Zahl mithilfe einer anderen komplexen Zahl.
	 *
	 * @param cn
	 *            komplexe Zahl.
	 */
	public ComplexNumber(ComplexNumber cn) {
		this.re = cn.re;
		this.im = cn.im;
	}
</pre>

## Rechenoperationen für komplexe Zahlen

<pre class="brush: java; title: ; notranslate" title="">/**
	 * Addiere eine komplexe Zahl zu dieser Zahl.
	 *
	 * @param cn
	 *            komplexe Zahl die addiert werden soll.
	 * @return Das Ergebnis der Addition.
	 */
	public ComplexNumber add(ComplexNumber cn) {
		return new ComplexNumber(this.re + cn.re, this.im + cn.im);
	}

	/**
	 * Subtrahiere eine komplexe Zahl von dieser Zahl.
	 *
	 * @param cn
	 *            komplexe Zahl die subtrahiert werden soll.
	 * @return Das Ergebnis der Subtraktion.
	 */
	public ComplexNumber subtract(ComplexNumber cn) {
		return new ComplexNumber(this.re - cn.re, this.im - cn.im);
	}

	/**
	 * Multiplizieren eine komplexe Zahl zu dieser Zahl.
	 *
	 * @param cn
	 *            komplexe Zahl die multipliziert werden soll.
	 * @return Das Ergebnis der Multiplikation.
	 */
	public ComplexNumber multiply(ComplexNumber cn) {
		double re = this.re * cn.re - this.im * cn.im;
		double im = this.im * cn.re + this.re * cn.im;
		return new ComplexNumber(re, im);
	}

	/**
	 * Dividiere eine komplexe Zahl durch diese Zahl.
	 *
	 * @param cn
	 *            komplexe Zahl die dividiert werden soll.
	 * @return Das Ergebnis der Division.
	 */
	public ComplexNumber divide(ComplexNumber cn) {
		// a+bi / c+di
		double cAndDSquared = (cn.re * cn.re + cn.im * cn.im);
		double re = (this.re * cn.re + this.im * cn.im) / cAndDSquared;
		double im = (this.im * cn.re - this.re * cn.im) / cAndDSquared;
		return new ComplexNumber(re, im);
	}
</pre>

## Rechenoperationen für reelle Zahlen

<pre class="brush: java; title: ; notranslate" title="">/**
	 * Addiere eine reelle Zahl zu dieser Zahl.
	 *
	 * @param number
	 *            reelle Zahl die addiert werden soll.
	 * @return Das Ergebnis der Addition.
	 */
	public ComplexNumber add(double number) {
		return this.add(new ComplexNumber(number));
	}

	/**
	 * Subtrahiere eine reelle Zahl von dieser Zahl.
	 *
	 * @param number
	 *            reelle Zahl die subtrahiert werden soll.
	 * @return Das Ergebnis der Subtraktion.
	 */
	public ComplexNumber subtract(double number) {
		return this.subtract(new ComplexNumber(number));
	}

	/**
	 * Multiplizieren eine reelle Zahl zu dieser Zahl.
	 *
	 * @param number
	 *            reelle Zahl die multipliziert werden soll.
	 * @return Das Ergebnis der Multiplikation.
	 */

	public ComplexNumber multiply(double number) {
		return this.multiply(new ComplexNumber(number));
	}

	/**
	 * Dividiere eine reelle Zahl durch diese Zahl.
	 *
	 * @param number
	 *            reelle Zahl die dividiert werden soll.
	 * @return Das Ergebnis der Division.
	 */
	public ComplexNumber divide(double number) {
		return this.divide(new ComplexNumber(number));
	}
</pre>

## Getter- und Setter-Methoden

<pre class="brush: java; title: ; notranslate" title="">public void setRealPart(double real) {
		this.re = real;
	}

	public double getRealPart() {
		return this.re;
	}

	public void setImaginaryPart(double imaginary) {
		this.im = imaginary;
	}

	public double getImaginaryPart() {
		return this.im;
	}
</pre>

## clone, equals, hashCode und toString

Die clone-Methode dupliziert die komplexe Zahl. Die equals-Methode prüft auf Gleichheit und die hashCode-Methode erstellt einen hashCode mithilfe der Double-Objekte der beiden Attribute.

<pre class="brush: java; title: ; notranslate" title="">public ComplexNumber clone() {
		return new ComplexNumber(this.re, this.im);
	}

	public boolean equals(Object o) {
		if (o instanceof ComplexNumber) {
			ComplexNumber cn = (ComplexNumber) o;
			if (cn.re == this.re && cn.im == this.im) {
				return true;
			}
		}
		return false;
	}

	public int hashCode() {
		Double re = this.re;
		Double im = this.im;

		// XOR erhält eine Gleichverteilung
		return re.hashCode() ^ im.hashCode();
	}

	public String toString() {
		return this.re + "+" + this.im + "i";
	}
}
</pre>