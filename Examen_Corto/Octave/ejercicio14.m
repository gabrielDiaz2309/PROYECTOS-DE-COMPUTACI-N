% Solicitar al usuario ingresar el año de nacimiento
anno_nacimiento = input("Ingrese el año de nacimiento: ");

% Verificar si el año es bisiesto
if (mod(anno_nacimiento, 4) == 0 && mod(anno_nacimiento, 100) ~= 0) || mod(anno_nacimiento, 400) == 0
    resultado = sprintf("El año %d es bisiesto.", anno_nacimiento);
else
    resultado = sprintf("El año %d no es bisiesto.", anno_nacimiento);
end

% Almacenar el resultado en una variable llamada salida
salida = resultado;

% Guardar el resultado en un archivo de texto
nombre_archivo = "ejercicio14.txt";
fid = fopen(nombre_archivo, 'w'); % Corregir aquí
fprintf(fid, '%s', salida);
fclose(fid);

printf("Resultado: %s\n", salida);
printf("El resultado ha sido guardado en el archivo %s\n", nombre_archivo);
        % Conexión a la base de datos PostgreSQL
        pkg load database % Cargar el paquete

        conn = pq_connect(setdbopts('dbname','ExamenCorto1','host','localhost',
            'port','5432','user','postgres','password','gabrielgrdb'));

        query = sprintf("INSERT INTO salida VALUES ('%s');", salida);
        N = pq_exec_params(conn, query);
