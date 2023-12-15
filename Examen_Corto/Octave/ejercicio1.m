

disp("Ingrese el primer número");
Num1 = input("");

disp("Ingrese el segundo número");
Num2 = input("");

disp("Ingrese el tercer número");
Num3 = input("");

if Num1 == Num2 && Num2 == Num3
    Res = sprintf("Todos son iguales: %.2f", Num1);
elseif Num1 == Num2
    Res = sprintf("El número diferente es: %.2f", Num3);
elseif Num1 == Num3
    Res = sprintf("El número diferente es: %.2f", Num2);
elseif Num2 == Num3
    Res = sprintf("El número diferente es: %.2f", Num1);
elseif Num1 > Num2 && Num1 > Num3
    Res = sprintf("La suma de los números es: %.2f", Num1 + Num2 + Num3);
elseif Num2 > Num1 && Num2 > Num3
    Res = sprintf("La multiplicación de los números es: %.2f", Num1 * Num2 * Num3);
else
    Res = sprintf("La concatenación es: %s", strcat(num2str(Num1), num2str(Num2), num2str(Num3)));
end

disp(Res);



fid = fopen("ejercicio1.txt", "w");
fprintf(fid, "%s", Res);
fclose(fid);

% Conexión a la base de datos PostgreSQL
pkg load database %cargar el paquete

conn = pq_connect(setdbopts('dbname','ExamenCorto1','host','localhost',
'port','5432','user','postgres','password','gabrielgrdb'))

salida = Res;

query = sprintf("insert into salida values ('%s');", salida);
N = pq_exec_params(conn, query);


