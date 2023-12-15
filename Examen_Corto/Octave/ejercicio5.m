% Generar números impares del 1 al 100
impares = 1:2:100;

% Contar la cantidad de números impares
cantidad_impares = numel(impares);

% Mostrar los números impares
disp("Números impares:");
disp(impares);

% Mostrar la cantidad de números impares
disp(["Cantidad de números impares: " num2str(cantidad_impares)]);

% Almacenar en un archivo de texto
fid = fopen('ejercicio5.txt', 'w');
fprintf(fid, 'Numeros impares= %s', num2str(impares));
fclose(fid);


% Conexión a la base de datos PostgreSQL
pkg load database %cargar el paquete

conn = pq_connect(setdbopts('dbname','ExamenCorto1','host','localhost',
'port','5432','user','postgres','password','gabrielgrdb'))


query = sprintf("insert into salida values ('%s');", num2str(impares));
N = pq_exec_params(conn, query);
