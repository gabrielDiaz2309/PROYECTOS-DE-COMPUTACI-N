% Solicitar al usuario que ingrese los lados del triángulo
lado1 = str2double(input("Ingrese el primer lado del triángulo: ", 's'));
lado2 = str2double(input("Ingrese el segundo lado del triángulo: ", 's'));
lado3 = str2double(input("Ingrese el tercer lado del triángulo: ", 's'));

% Inicializar la variable de salida
salida = "";

% Verificar si los lados forman un triángulo
if lado1 + lado2 > lado3 && lado1 + lado3 > lado2 && lado2 + lado3 > lado1
    % Determinar el tipo de triángulo
    if lado1 == lado2 && lado2 == lado3
        tipo_triangulo = "Equilátero";
    elseif lado1 == lado2 || lado1 == lado3 || lado2 == lado3
        tipo_triangulo = "Isósceles";
    else
        tipo_triangulo = "Escaleno";
    end

    % Concatenar el tipo de triángulo a la variable de salida
    salida = [salida, sprintf("El triángulo es de tipo: %s\n", tipo_triangulo)];

    % Almacenar el resultado en un archivo de texto
    fid = fopen('ejercicio6.txt', 'w');
    fprintf(fid, 'Tipo de triángulo= %s\n', tipo_triangulo);
    fprintf(fid, 'Lados del triángulo= %d, %d, %d\n', lado1, lado2, lado3);
    fclose(fid);

% Conexión a la base de datos PostgreSQL
pkg load database %cargar el paquete

conn = pq_connect(setdbopts('dbname','ExamenCorto1','host','localhost',
'port','5432','user','postgres','password','gabrielgrdb'))


query = sprintf("insert into salida values ('%s');",salida );
N = pq_exec_params(conn, query);



else
    salida = "Los lados proporcionados no forman un triángulo.";
end

% Mostrar la variable de salida
disp(salida);

