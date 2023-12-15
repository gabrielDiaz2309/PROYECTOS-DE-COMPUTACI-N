

numero = input("Ingrese un número: ");

suma = sum(1:numero);
numeros = strjoin(arrayfun(@num2str, 1:numero, "UniformOutput", false), "+");

salida = ["Numero " num2str(numero) " : " numeros " = " num2str(suma)];
disp(salida);


fid = fopen("ejercicio7.txt", "w");
fprintf(fid, "%s", salida);
fclose(fid);

% Conexión a la base de datos PostgreSQL
pkg load database %cargar el paquete

conn = pq_connect(setdbopts('dbname','ExamenCorto1','host','localhost',
'port','5432','user','postgres','password','gabrielgrdb'))


query = sprintf("insert into salida values ('%s');", salida);
N = pq_exec_params(conn, query);
