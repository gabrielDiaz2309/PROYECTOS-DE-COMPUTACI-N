






palabra_ingresada = input('Ingrese una palabra: ', 's');

numero_vocales = contar_vocales(palabra_ingresada);

resultado = ['La palabra ' palabra_ingresada ' tiene ' num2str(numero_vocales) ' vocales.'];
disp(resultado);

fid = fopen('ejercicio3.txt', 'w');
fprintf(fid, '%s', resultado);
fclose(fid);

% Almacenar el resultado en la variable 'salida'
salida = resultado;




fid = fopen("ejercicio3.txt", "w");
fprintf(fid, "%s", salida);
fclose(fid);

% Conexión a la base de datos PostgreSQL
pkg load database %cargar el paquete

conn = pq_connect(setdbopts('dbname','ExamenCorto1','host','localhost',
'port','5432','user','postgres','password','gabrielgrdb'))


query = sprintf("insert into salida values ('%s');", salida);
N = pq_exec_params(conn, query);


