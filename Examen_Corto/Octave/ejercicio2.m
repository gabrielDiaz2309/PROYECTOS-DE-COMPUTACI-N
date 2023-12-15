




num_str = input("Ingrese un número: ", "s");
num = str2num(num_str);

divisores = [];
for i = 1:num
    if mod(num, i) == 0
        divisores = [divisores, i];
    end
end

% Mostrar los divisores
divisores_str = sprintf("Los divisores de %d son: %s", num, num2str(divisores));
disp(divisores_str);


fid = fopen("ejercicio2.txt", "w");
fprintf(fid, "%s", divisores_str);
fclose(fid);



% Conexión a la base de datos PostgreSQL
pkg load database %cargar el paquete

conn = pq_connect(setdbopts('dbname','ExamenCorto1','host','localhost',
'port','5432','user','postgres','password','gabrielgrdb'))

salida = divisores_str;

query = sprintf("insert into salida values ('%s');", salida);
N = pq_exec_params(conn, query);


