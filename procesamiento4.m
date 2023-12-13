
n=-3:7;
x=0.55.^(n+3);
h=[1 1 1 1 1 1 1 1 1 1 1];
y=conv(x,h);
subplot(3,1,1)
stem(x)
title('Señal Original')
subplot(3,1,2)
stem(h)
title('Respuesta al Impulso / Segunda Señal')
subplot(3,1,3)
stem(y)
title('Convolucion Resultante')
