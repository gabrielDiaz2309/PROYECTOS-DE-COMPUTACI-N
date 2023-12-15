







printf("Ingrese el número de inicio: ");
inicio = input("");

printf("Ingrese el número de fin: ");
fin = input("");

% Asegurarse de que el número de inicio sea par
if mod(inicio, 2) != 0
    inicio += 1;
end

% Crear un vector para almacenar los números de 2 en 2
numeros_pares = inicio:2:fin;

% Convertir el vector de números en una cadena
resultado = sprintf("%s", num2str(numeros_pares));

% Mostrar el resultado
disp(["Resultado: " resultado]);


fid = fopen("ejercicio4.txt", "w");
fprintf(fid, "%s", resultado);
fclose(fid);

% Conexión a la base de datos PostgreSQL
pkg load database %cargar el paquete

conn = pq_connect(setdbopts('dbname','ExamenCorto1','host','localhost',
'port','5432','user','postgres','password','gabrielgrdb'))


query = sprintf("insert into salida values ('%s');", resultado);
N = pq_exec_params(conn, query);

