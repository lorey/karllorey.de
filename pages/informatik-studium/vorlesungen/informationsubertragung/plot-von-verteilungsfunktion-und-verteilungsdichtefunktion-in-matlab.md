---
id: 724
title: Plot von Verteilungsfunktion und Verteilungsdichtefunktion in MATLAB
date: 2012-01-05T19:28:24+00:00
author: Karl Lorey
layout: page
guid: http://www.karllorey.de/?page_id=724
---
**Gegeben:** Die kontinuierliche Zufallsvariable X durch ihre Verteilungsdichtefunktion x(t), wobei

> x(t) = {
  
> 0,5*e^t, für t<=0
  
> 0,25*(t-2), für 2<=t<=4
  
> 0, sonst
  
> }

**Aufgabe:** Plot der Verteilungsdichtefunktion x(t) und der Verteilungsfunktion X(t)

<pre class="brush: plain; title: ; notranslate" title="">% Einstellungen für Plot
intervall = 0.01;

% Beschriftungen in Schaubild 1
figure(1);
title('Verteilungsdichtefuntion');
xlabel('t');
ylabel('x(t) = P(X&lt;=t)');
hold on; % Verwerfen des vorherigen Plot verhindern

% Beschriftungen in Schaubild 2
figure(2);
title('Verteilungsfunktion');
xlabel('t');
ylabel('X(t) = d/dt x(t)');
hold on; % Verwerfen des vorherigen Plot verhindern

% Plotten des ersten Bereichs -unendl. &lt; t &lt;= 0
T = -10:intervall:0;

% Plot in Schaubild 1
figure(1);
plot(T, 0.5*exp(T));
integraleins = quad('0.5 * exp(T)', -10, 0);

% Plot in Schaubild 2
figure(2);
plot(T,cumtrapz(T, 0.5 * exp(T)));

% Plotten des zweiten Bereichs 0 &lt; t &lt; 2
T = 0:intervall:2;

% Plot in Schaubild 1
figure(1);
plot(T, 0);

% Plot in Schaubild 2
figure(2);
plot(T, integraleins);

% Plotten des dritten Bereichs 2 &lt;= t &lt; 4
T = 2:intervall:4;

% Plot in Schaubild 1
figure(1);
plot(T, 0.25 * (T - 2));
integralzwei = quad('0.25 * (T - 2)', 2, 4);

% Plot in Schaubild 2
figure(2);
plot(T,cumtrapz(T, 0.25 * (T - 2)) + integraleins);

% Plotten des dritten Bereichs 4 &lt;= t &lt; 10
T = 4:intervall:10;

% Plot in Schaubild 1
figure(1);
plot(T, 0);

% Plot in Schaubild 2
figure(2);
plot(T, integraleins + integralzwei);
</pre>