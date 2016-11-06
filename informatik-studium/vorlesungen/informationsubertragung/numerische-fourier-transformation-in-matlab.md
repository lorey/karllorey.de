---
id: 761
title: Numerische Fourier-Transformation in MATLAB
date: 2012-01-06T14:01:09+00:00
author: Karl Lorey
layout: page
guid: http://www.karllorey.de/?page_id=761
---
<pre class="brush: plain; title: ; notranslate" title="">%% Teil 1 Plot
fs = 1/200;
X = 0:fs:5;
Y = 2*sin(2*pi*60*X) + cos(2*pi*100*X);

subplot(3, 2, [1 2]);
stem(X, Y);

%% Teil 2 Fourier
values = fft(Y);
subplot(3, 2, [3 4]);
plot(values, 'ro');
title('Fourier Koeffizienten in der komplexen Ebene');
xlabel('Re(Z)');
ylabel('Im(Z)');

%% Teil 3 Amplitudenspektrum
subplot(3, 2, 5);
n = length(Y);
c = fft(Y)/n;
amp = 2*abs(c);
amp(1) = amp(1)/2;
m = floor(n/2);
plot(linspace(0, (m-1)*fs/n, m), amp(1:m))
title('Amplitudenspektrum');
xlabel('Frequenz');
ylabel('Amplitude');

%% Teil 4 Phasenspektrum
subplot(3, 2, 6)
phase = unwrap(angle(c));
phase(1) = phase(1)/2;
m = floor(n/2);
plot(linspace(0, (m-1)*fs/n, m), phase(1:m))
title('Phasenspektrum');
xlabel('Frequenz');
ylabel('Phase');
</pre>

Folgende Fehler sind zu beachten:

  * Achsen teilweise falsch skaliert
  * Phase und Amplitude nur tweilweise angezeigt
  * Werte sind kontinuierlich zu plotten