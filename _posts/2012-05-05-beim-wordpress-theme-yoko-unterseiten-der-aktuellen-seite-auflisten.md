---
id: 1124
title: Beim WordPress-Theme Yoko Unterseiten der aktuellen Seite auflisten
date: 2012-05-05T19:27:51+00:00
author: Karl Lorey
layout: post
guid: http://www.karllorey.de/?p=1124
permalink: /2012/05/05/beim-wordpress-theme-yoko-unterseiten-der-aktuellen-seite-auflisten/
categories:
  - Allgemein
tags:
  - Anleitung
  - Code
  - PHP
  - Theme
  - WordPress
  - Yoko
---
Yoko ist ein sehr schönes Theme für WordPress. Es passt sich automatisch der Fensterbreite bzw. dem Endgerät an (&#8222;responsive layout&#8220;) und lässt sich somit nicht nur auf dem PC, sondern auch auf mobilen Endgeräten sehr gut betrachten.
  
Als Problem ergibt sich leider der Nachteil, dass bei einer mobilen Ansicht des WordPress-Theme Yoko das Menü nicht mehr aufgeklappt werden kann (Touch-Bedienung). Dies führt dazu, dass Unterseiten, die nicht direkt im Inhalt der Seite verlinkt sind, auf einem mobilen Endgerät nicht mehr zu finden sind.

## Yoko um eine Unterseiten-Übersicht erweitern<figure id="attachment_1147" style="width: 150px" class="wp-caption alignright">

[<img class="size-thumbnail wp-image-1147" title="Yoko mit einer Unterseiten-Übersicht" src="http://www.karllorey.de/wp-content/uploads/2012/05/yoko_unterseiten_ohne_inhalt-150x99.png" alt="Yoko mit einer Unterseiten-Übersicht" width="150" height="99" />](http://www.karllorey.de/wp-content/uploads/2012/05/yoko_unterseiten_ohne_inhalt.png)<figcaption class="wp-caption-text">Yoko mit einer Unterseiten-Übersicht</figcaption></figure> 

Eine einfache und elegante Möglichkeit dieses Problem mit Yoko zu umgehen, ist die Erstellung eines WordPress-Seiten-Template, welches **nach dem eigentlichen Seiten-Inhalt alle Unterseiten als Liste** in einer Übersicht anzeigt. Dies ermöglicht eine erleichterte Bedienung des Themes und damit auch das problemlose mobile Navigieren durch die Webseite. Zunächst muss dazu das Theme Yoko selbst und danach der WordPress-Inhalt angepasst werden. Die Anpassung sollte maximal 20 Minuten in Anspruch nehmen (je nach Anzahl der umzustellenden Seiten).<!--more-->

## Anpassung des Theme im Yoko-Theme-Ordner

Die beste Möglichkeit Yoko anzupassen, ist das Erstellen eines neuen Templates. Hierzu muss lediglich eine Datei namens &#8222;subpageindex.php&#8220; im Yoko-Ordner (_wp-content/themes/yoko_) mit folgendem Inhalt erstellt werden:

<pre class="brush: xml; title: ; notranslate" title="">&lt;?php
/*
Template Name: Subpage index
*/
get_header(); ?&gt;

&lt;div id="wrap"&gt;
&lt;div id="main"&gt;

	&lt;div id="content"&gt;

		&lt;?php the_post(); ?&gt;

		&lt;article id="post-&lt;?php the_ID(); ?&gt;" &lt;?php post_class(); ?&gt;&gt;

			&lt;header class="page-entry-header"&gt;
				&lt;h1 class="entry-title"&gt;&lt;?php the_title(); ?&gt;&lt;/h1&gt;
			&lt;/header&gt;&lt;!--end page-entry-hader--&gt;

			&lt;div class="single-entry-content"&gt;
				&lt;?php the_content(); ?&gt;
				&lt;div class="clear"&gt;&lt;/div&gt;
				&lt;?php wp_link_pages( array( 'before' =&gt; '&lt;div class="page-link"&gt;' . __( 'Pages:', 'yoko' ), 'after' =&gt; '&lt;/div&gt;' ) ); ?&gt;
				&lt;?php edit_post_link( __( 'Edit &rarr;', 'yoko' ), '&lt;span class="edit-link"&gt;', '&lt;/span&gt;' ); ?&gt;
			&lt;/div&gt;&lt;!--end entry-content--&gt;

			&lt;!-- Subpage index --&gt;
			&lt;h2&gt;Unterseiten&lt;/h2&gt;
			&lt;?php
			// Hier werden die direkten Unterseiten geladen
			$children = wp_list_pages('title_li=&depth=1&child_of='.$post-&gt;ID.'&echo=0');
			// Falls es Unterseiten gibt, werden diese ausgegeben
			if ($children) { ?&gt;
				&lt;ul&gt;
				&lt;?php echo $children; ?&gt;
				&lt;/ul&gt;
			&lt;?php } ?&gt;

		&lt;/article&gt;&lt;!-- end post-&lt;?php the_ID(); ?&gt; --&gt;

		&lt;?php comments_template( '', true ); ?&gt;

	&lt;/div&gt;&lt;!-- end content --&gt;

&lt;?php get_sidebar(); ?&gt;
&lt;?php get_footer(); ?&gt;
</pre>

Der Inhalt dieser Datei gleicht dem Standard-Template einer normalen Seite (vgl. _page.php_), erweitert diese jedoch um eine Liste der direkten Unterseiten. Um die Unterseiten innerhalb des article-Tag einzubinden, wurde der Inhalt der Datei _content-page.php_ mit eingebunden (Zeilen 14-37). Dieser würde sonst durch den Aufruf von

<pre class="brush: php; title: ; notranslate" title="">&lt;?php get_template_part( 'content', 'page' ); ?&gt;
</pre>

nachgeladen.

Wichtig: Diese Änderungen werden, wie das Original-Theme Yoko auch, unter der <a href="http://www.gnu.org/licenses/gpl.html" target="_blank">GNU General Public License</a> veröffentlicht.

## Anpassung des Inhalts

Das erstellte Yoko-Template &#8222;Subpage index&#8220; muss dann nur noch als Template der betroffenen Seiten eingestellt werden. Im WordPress-Adminpanel öffnet man die Seite, welche eine Übersicht der Unterseiten zeigen soll, zum Bearbeiten und wählt nun auf der rechten Seite unter &#8222;Template&#8220; die Option &#8222;Subpage index&#8220;.

## Ergebnis: Yoko mit einer Unterseiten-Übersicht

Auf einer Seite ohne eigentlichen Inhalt sieht das Ganze dann folgendermaßen aus:<figure id="attachment_1147" style="width: 300px" class="wp-caption aligncenter">

[<img class="size-medium wp-image-1147" title="Yoko mit einer Unterseiten-Übersicht" src="http://www.karllorey.de/wp-content/uploads/2012/05/yoko_unterseiten_ohne_inhalt-300x199.png" alt="Yoko mit einer Unterseiten-Übersicht" width="300" height="199" />](http://www.karllorey.de/wp-content/uploads/2012/05/yoko_unterseiten_ohne_inhalt.png)<figcaption class="wp-caption-text">Das WordPress-Theme Yoko mit einer Unterseiten-Übersicht</figcaption></figure> 

Wer sich bei der Anpassung Arbeit sparen möchte, der kann sich die aktuellste Version des <a href="https://github.com/lorey/yoko" target="_blank">WordPress Theme Yoko auf GitHub</a> forken.

Für Anregungen oder Tipps steht für euch wie immer die Kommentarfunktion bereit!