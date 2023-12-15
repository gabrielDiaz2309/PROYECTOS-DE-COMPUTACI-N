% Solicitar al usuario ingresar las tres notas
nota1 = input('Ingrese la primera nota: ');
nota2 = input('Ingrese la segunda nota: ');
nota3 = input('Ingrese la tercera nota: ');

% Calcular el promedio
promedio = (nota1 + nota2 + nota3) / 3;

% Verificar si el promedio es mayor o igual a 60
if promedio >= 60
    mensaje = 'Aprobado';
else
    mensaje = 'Reprobado';
end

% Crear la cadena de salida
salida = sprintf('Promedio: %.2f, Estado: %s', promedio, mensaje);

% Mostrar en la consola
disp(salida);

% Almacenar el resultado en un archivo de texto
archivo = fopen('ejercicio13.txt', 'w');

% Verificar si se pudo abrir el archivo correctamente
if archivo == -1
    error('No se pudo abrir el archivo para escribir.');
end

% Escribir la cadena en el archivo
fprintf(archivo, '%s', salida);

        % Conexión a la base de datos PostgreSQL
        pkg load database % Cargar el paquete

        conn = pq_connect(setdbopts('dbname','ExamenCorto1','host','localhost',
            'port','5432','user','postgres','password','gabrielgrdb'));

        query = sprintf("INSERT INTO salida VALUES ('%s');", salida);
        N = pq_exec_params(conn, query);

% Cerrar el archivo
fclose(archivo);

