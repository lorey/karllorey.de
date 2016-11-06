---
id: 730
title: Darstellung der Code-Effizienz und der maximalen Anzahl der Nutzbits in MATLAB
date: 2012-01-05T19:30:05+00:00
author: Karl Lorey
layout: page
guid: http://www.karllorey.de/?page_id=730
---
<pre class="brush: plain; title: ; notranslate" title="">%% Code-Effizienz
figure(1);
m = linspace(1, 100, 1000);
f = inline('m./(m+k) * 100', 'm', 'k');
semilogx(m, f(m, 1), m, f(m, 2), m, f(m, 3), m, f(m, 4), ...
    m, f(m, 5), m, f(m, 6), m, f(m, 7), m, f(m, 8), ...
    m, f(m, 9), m, f(m, 10), m, f(m, 11), m, f(m, 12));
legend('k = 1', 'k = 2', 'k = 3', 'k = 4', ...
    'k = 5', 'k = 6', 'k = 7', 'k = 8', ...
    'k = 9', 'k = 10', 'k = 11', 'k = 12', ...
    'Location', 'southeast');
title('Code-Effizienz');
xlabel('m: Anzahl der Nutzbits');
ylabel('Code-Effizienz in Prozent');
%set(gca,'YGrid', 'on');

%% Maximale Anzahl der Nutzbits
figure(2);
k = linspace(2, 16, 1000);
g = inline('2.^k - 1 - k', 'k');
semilogy(k, g(k));
legend('max. Anzahl von Nutzbits (m)', 'Location', 'southeast');
title('Maximale Anzahl der Nutzbits bei h=3');
xlabel('k: Anzahl der Prüfbits');
ylabel('m: Anzahl der maximal möglichen Nutzbits');
%set(gca,'XGrid', 'on');
</pre>