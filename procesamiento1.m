

t= -0.04:0.001:0.04;

%Guardamos la funcion en x
x=20*exp(j*(80*pi*t-0.4*pi));
figure;
%posicionamos la imagen
subplot (1,2,1);
plot3(t, real(x), imag(x)); grid
title('20*e^{j*(80\pit-0.4\pi)}')
xlabel('Tiempo, s'); ylabel('Real'); zlabel('Imag')
%posicionamos la imagen
subplot (1,2,2);
plot(t, real(x), 'b'); hold on
plot(t, imag(x), 'r'); grid
title('Rojo - Componente Imaginario, Azul - Componente Real de la Exponencial')
xlabel('Tiempo');ylabel('Amplitud')

