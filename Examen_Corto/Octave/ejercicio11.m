
entrada = input("Ingrese una palabra: ", "s");
vocales = "AEIOUaeiou";

contador_a = 0;
contador_e = 0;
contador_i = 0;
contador_o = 0;
contador_u = 0;

for i = 1:length(entrada)
    letra = entrada(i);
    if any(letra == vocales)
        switch letra
            case {'A', 'a'}
                contador_a += 1;
            case {'E', 'e'}
                contador_e += 1;
            case {'I', 'i'}
                contador_i += 1;
            case {'O', 'o'}
                contador_o += 1;
            case {'U', 'u'}
                contador_u += 1;
        endswitch
    end
end

salida = sprintf("A=%d, E=%d, I=%d, O=%d, U=%d", contador_a, contador_e, contador_i, contador_o, contador_u);

disp("Resultado:");
disp(salida);



fid = fopen("ejercicio6.txt", "w");
fprintf(fid, "%s", salida);
fclose(fid);

% Conexión a la base de datos PostgreSQL
pkg load database %cargar el paquete

conn = pq_connect(setdbopts('dbname','Tarea','host','localhost',
'port','5432','user','postgres','password','gabrielgrdb'))


query = sprintf("insert into ejercicio1 values ('%s');", salida);
N = pq_exec_params(conn, query);
