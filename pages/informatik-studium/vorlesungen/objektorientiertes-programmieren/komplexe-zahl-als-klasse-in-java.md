---
id: 1471
title: Komplexe Zahl als Klasse in Java
date: 2013-02-07T19:10:47+00:00
author: Karl Lorey
layout: page
guid: http://www.karllorey.de/?page_id=1471
---
<pre class="brush: java; title: ; notranslate" title="">/**
 * Repräsentation einer komplexen Zahl.
 *
 * @author Karl Lorey
 * @version 1.0.0
 *
 */
public class ComplexNumber {
    /**
     * Realteil.
     */
    double re;

    /**
     * Imaginärteil
     */
    double im;

    /**
     * Erstellt 0.
     */
    public ComplexNumber() {
        this(0);
    }

    /**
     * Erstellt eine reele Zahl.
     *
     * @param real
     *            Reelle Zahl.
     */
    public ComplexNumber(double real) {
        this(real, 0);
    }

    /**
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

    /**
     * Erstellt eine komplexe Zahl mithilfe einer anderen komplexen Zahl.
     *
     * @param cn
     *            komplexe Zahl.
     */
    public ComplexNumber(ComplexNumber cn) {
        this.re = cn.re;
        this.im = cn.im;
    }

    /**
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

    /**
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

    public void setRealPart(double real) {
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

    public ComplexNumber clone() {
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