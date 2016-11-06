---
id: 1451
title: 'Entwurfsmuster: Builder in Java (Erbauer)'
date: 2013-02-05T21:33:23+00:00
author: Karl Lorey
layout: page
guid: http://www.karllorey.de/?page_id=1451
---
Zum Verständnis:

  * Joshua Block: Effective Java
  * <a href="http://stackoverflow.com/questions/328496/when-would-you-use-the-builder-pattern/1953567#1953567" target="_blank">StackOverflow: When would you use the Builder Pattern</a>

## Erbauermuster in Java zur Erzeugung von Objekten mit optionalen Parametern

### Product mit integriertem ConcreteBuilder

<pre class="brush: java; title: ; notranslate" title="">/**
 * Product.
 *
 * @author Karl Lorey
 *
 */
public class Car {
    public static enum FuelType {
        GASOLINE, DIESEL
    }

    // Muss
    private int speed;
    private int power;
    private FuelType fuelType;

    // Kann
    private boolean withCdAudio;
    private boolean withSunroof;
    private boolean withAirConditioning;

    /**
     * ConcreteBuilder nach Effective Java. In diesem Fall ohne abstrakten
     * Builder, da durch den Builder nur die Standardparameter gesetzt werden
     * sollen.
     *
     * @author Karl Lorey
     *
     */
    public static class Builder {
        // Muss
        private int speed;
        private int power;
        private FuelType fuelType;

        // Kann mit Standardwerten
        private boolean withCdAudio = true;
        private boolean withSunroof = false;
        private boolean withAirConditioning = true;

        /**
         * Benötigt die Parameter, die gesetzt werden müssen.
         *
         * @param speed
         *            Höchstgeschwindigkeit.
         * @param power
         *            Leistung.
         * @param ft
         *            Kraftstoff-Art.
         */
        public Builder(int speed, int power, FuelType ft) {
            this.speed = speed;
            this.power = power;
            this.fuelType = ft;
        }

        public Builder withCdAudio(boolean integrated) {
            this.withCdAudio = integrated;
            return this;
        }

        public Builder withSunroof(boolean integrated) {
            this.withSunroof = integrated;
            return this;
        }

        public Builder withAirConditioning(boolean integrated) {
            this.withAirConditioning = integrated;
            return this;
        }

        /**
         * Erstellt das eigentliche Auto.
         *
         * @return Das erstellte Auto.
         */
        public Car build() {
            return new Car(this);
        }
    }

    public Car(Builder builder) {
        this.speed = builder.speed;
        this.power = builder.power;
        this.fuelType = builder.fuelType;
        this.withCdAudio = builder.withCdAudio;
        this.withSunroof = builder.withSunroof;
        this.withAirConditioning = builder.withAirConditioning;
    }
}
</pre>

### Director

<pre class="brush: java; title: ; notranslate" title="">/**
 * Director. Nutzt den Builder zur Erstellung eines Autos mit und ohne
 * Standardparameter.
 *
 * @author Karl Lorey
 *
 */
public class Director {
    /**
     * Erstellung eines Autos mit Standardparametern.
     *
     * @return Standardauto
     */
    public Car createUsualCar() {
        return new Car.Builder(176, 95, Car.FuelType.DIESEL).build();
    }

    /**
     * Erstellung eines Autos mit geänderten Parametern.
     *
     * @return BMW M3
     */
    public Car createBmwM3() {
        return new Car.Builder(249, 420, Car.FuelType.GASOLINE)
                .withAirConditioning(true).withCdAudio(true).withSunroof(true)
                .build();
    }
}
</pre>