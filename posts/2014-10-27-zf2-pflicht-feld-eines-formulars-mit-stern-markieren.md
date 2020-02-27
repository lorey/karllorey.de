---
id: 1769
title: 'ZF2: Pflicht-Feld eines Formulars mit Stern markieren'
date: 2014-10-27T13:15:09+00:00
author: Karl Lorey
layout: post
guid: http://www.karllorey.de/?p=1769
permalink: /2014/10/27/zf2-pflicht-feld-eines-formulars-mit-stern-markieren/
image: /wp-content/uploads/2014/08/astronomy-constellation-dark-2154.jpg
categories:
  - Allgemein
tags:
  - Anleitung
  - Clean Code
  - Formular
  - PHP
  - Zend Framework 2
  - Zend\Form
---
Zend Framework 2.3 bietet bisher leider keine Funktionalität an, um Pflicht-Felder eines Formulars (Zend\Form und Zend\Form\Element) automatisch mit einem Stern zu markieren. Dieser Artikel zeigt Möglichkeiten auf, wie benötigte Formular-Felder bzw. Form-Elemente mit einem beliebigen Zeichen (z.B. einem Stern) gekennzeichnet werden können. Prinzipiell ist hierbei beides Mal ein ViewHelper zu erstellen, der den gewünschten Effekt erzielt, indem er das Label um einen Stern ergänzt.

Beispielsweise sei folgendes Formular-Element gegeben, welches mit `required' => true` als Pflicht-Feld deklariert wurde und anschließend automatisch als benötigtes Feld gekennzeichnet werden soll.

<pre class="brush: php; title: ; notranslate" title="">
// Irgendwo in einem Controller
$form = new Zend\Form();

// ... konfiguration, etc.

// beliebiges benötigtes element
// muss ausgefüllt werden (required =&gt; true)
$form-&gt;add(array(
    'type' =&gt; 'Zend\Form\Element\Email',
    'required' =&gt; true,
    'name' =&gt; 'email',
    'options' =&gt; array(
        'label' =&gt; 'Email'
    ),
));
</pre>

## Einfach: Zend\Form\View\Helper\FormLabel erweitern

Die einfachste Möglichkeit ein benötigtes Formular-Element in Zend Framework mit einem Stern zu markieren besteht darin `Zend\Form\View\Helper\FormLabel` zu erweitern.

<pre class="brush: php; title: ; notranslate" title="">&lt;?php

namespace Application\Form\View\Helper;

use Zend\Form\View\Helper\FormLabel as OriginalFormLabel;
use Zend\Form\ElementInterface;

class MarkRequiredWithStar extends OriginalFormLabel
{
    public function __invoke(ElementInterface $element = null,
            $labelContent = null, $position = null)
    {
        // TODO: Alle Zeilen aus __invoke in der Klasse
        // Zend\Form\View\Helper\FormLabel implementieren

        // Setze $required per Standard auf true, falls required nicht existiert
        $isRequiredElement = ($element-&gt;hasAttribute('required') ?
            $element-&gt;getAttribute('required') : true);      

        if ($isRequiredElement) {
        $labelContent = sprintf(
            // hier wird der Stern oder ein anderes Symbol eingefügt
            '&lt;span class="required-label"&gt;(*)&lt;/span&gt; %s',
            $labelContent
        );
        }

        return $openTag . $labelContent . $this-&gt;closeTag();
    }
}
</pre>

Dieser ViewHelper ist dann wie gewohnt in der Module.php unter `getViewHelperConfig` zu verlinken, so dass man ihn in jedem View aufrufen kann. Wie das funktioniert ist am Ende des Artikels beschrieben.

Diese Implementierung ist zwar einfach, hat jedoch den Nachteil, dass bei künftigen Versionen des Zend Framework Änderungen am FormLabel-Helper vorgenommen werden könnten, die dann manuell in die selbst erstellte Klasse kopiert werden müssen. Dies ist umständlich und kann zu einem späteren Zeitpunkt zu Fehlern führen. Die nachfolgende Methode umgeht dieses Problem.

## Elegant und sauber: Zend\Form\View\Helper\FormLabel wiederverwenden

Statt den Inhalt der Methode zu kopieren und damit duplizierten und schwer zu wartenden Code zu erzeugen, wird bei dieser Möglichkeit der Implementierung das Problem beseitigt, indem der FormLabel-Helper nicht kopiert sondern einfach wiederverwendet wird. So funktioniert der ViewHelper auch noch, wenn sich die Funktionalität des Zend Framework in kommenden Versionen ändert.

<pre class="brush: php; title: ; notranslate" title="">namespace Application\Form\View\Helper;

use Zend\Form\View\Helper\FormLabel as OriginalFormLabel;
use Zend\Form\ElementInterface;

/**
 * Add mark (*) for all required elements inside a form.
 */
class MarkRequiredWithStar extends OriginalFormLabel
{
     /**
     * Invokable
     *
     * @return str
     */
    public function __invoke(ElementInterface $element = null,
           $labelContent = null, $position = null)
    {
        // parent::__invoke() ruft die invoke-Methode aus FormLabel auf
        $originalformLabel = parent::__invoke($element, $labelContent, $position);

        // Setze $required per Standard auf true, falls required nicht existiert
        $isRequiredElement = $element-&gt;hasAttribute('required') ?
            $element-&gt;getAttribute('required') : true;

        if ($isRequiredElement) {
            // mit Stern markieren
            return '&lt;span class="required-label"&gt;(*)&lt;/span&gt;' . $originalformLabel;
        } else {
            // normales Label zurückgeben
            return  $originalformLabel;
        }
    }
}
</pre>

## ViewHelper in der Config des Moduls verlinken

Beide Methoden erstellen einen neuen ViewHelper, der anschließend natürlich in der Module.php des jeweiligen Moduls verlinkt werden muss, da er nur so direkt im View aufgerufen werden kann.

<pre class="brush: php; title: ; notranslate" title="">// ...
public function getViewHelperConfig()
{
    return array(
        'invokables' =&gt; array(
            // ...
            'formlabel' =&gt; 'Application\Form\View\Helper\MarkRequiredWithStar',
            // ...
        ),
    );
}
// ...
</pre>

Benutzt man den Namen des originalen Zend Framework ViewHelper (also `formLabel`), so wird dieser auch von allen anderen ZF2-ViewHelpern verwendet, die Formulare mit Label anzeigen. So nutzt dann der form-ViewHelper automatisch den neu erstellten Helper zum darstellen von Feldern. Es werden also alle Pflicht-Felder in allen Fomularen mit einem Stern markiert. Bei einem anderen Namen passiert dies natürlich nicht. Der ViewHelper kann natürlich jederzeit auch explizit im View über `$this->formLabel($element)` oder mit dem entsprechenden Namen aufgerufen werden.

Weitere Informationen:

  * <a href="http://framework.zend.com/manual/2.3/en/modules/zend.form.view.helpers.html#formlabel" target="_blank">formLabel-Helper in der Zend Framework 2 Dokumentation</a>
  * <a href="http://stackoverflow.com/questions/15936804/how-to-use-a-custom-form-view-helper-in-zend-framework-2/15940309#15940309" target="_blank">Überschreiben der ZF2-Standard-ViewHelper</a>
  * <a href="http://stackoverflow.com/questions/16260836/add-required-suffix-to-zf2-form-element-label" target="_blank">Label anpassen</a>
