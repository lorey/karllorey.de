---
id: 726
title: Plot der Restfehlerwahrscheinlichkeit bei automatischer Fehlerkorrektur und Wiederholungsaufforderung in MATLAB
date: 2012-01-05T19:29:01+00:00
author: Karl Lorey
layout: page
guid: http://www.karllorey.de/?page_id=726
---
Gegeben: Die Funktionen f1 und f2, welche die Restfehlerwahrscheinlichkeit im Verhältnis zur Bitfehlerwahrscheinlichkeit angeben.

<pre class="brush: plain; title: ; notranslate" title="">figure(1);
f1 = inline('1-(((1-x).^3) + 3*x.*((1-x).^3))','x');
f2 = inline('x.^3','x');

% Erstellung eines logarithmischen Wertebereichs
% für pb von 10^-8 (pb von satellit) bis 10^0 (maximales pb = 1)
x = logspace(-8, 0, 100); % spart berechnungen im Vgl. zu linspace

loglog(x,f1(x), 'red'); % Zeichnen von f1 in rot
hold on; % Figure nicht resetten
grid on; %raster einblenden
loglog(x,f2(x), 'green'); % Zeichnen von f2 in grün

% Titel
title('Vergleich von Restfehlerwahrscheinlichkeit in Abhängigkeit von p_b');

% Achsenbeschriftungen
xlabel('Bitfehlerwahrscheinlichkeit: p_b');
ylabel('Restfehlerwahrscheinlichkeit: p_{RK} und p_{RN}');

% Legende
legend('p_{RK} (autom. Fehlerkorrektur)', 'p_{RN} (Wiederholungsaufforderung)');
legend('Location', 'southeast');
</pre>