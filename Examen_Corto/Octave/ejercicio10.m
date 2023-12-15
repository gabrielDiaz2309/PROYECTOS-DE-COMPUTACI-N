
disp("Ingrese el primer número:");
num1 = input("");

disp("Ingrese el segundo número:");
num2 = input("");

% Encontrar el mayor y el menor número
mayor = max(num1, num2);
menor = min(num1, num2);

% Crear la matriz de números desde el mayor hasta el menor
numeros_matriz = [mayor:-1:menor];

% Crear la cadena de texto con el resultado
salida = ["Resultado: " num2str(numeros_matriz)];

disp(salida);

fid = fopen("ejercicio5.txt", "w");
fprintf(fid, "%s", salida);
fclose(fid);

% Conexión a la base de datos PostgreSQL
pkg load database %cargar el paquete

conn = pq_connect(setdbopts('dbname','Tarea','host','localhost',
'port','5432','user','postgres','password','gabrielgrdb'))


query = sprintf("insert into ejercicio1 values ('%s');", salida);
N = pq_exec_params(conn, query);
