numero = input('Ingrese un número: ');

if mod(numero, 7) == 0
    % Calcular el factorial si el número es divisible por 7
    factorialResultado = factorial(numero);
    disp(['El factorial de ' num2str(numero) ' es: ' num2str(factorialResultado)]);

    % Almacenar el resultado en el archivo de texto
    nombreArchivo = 'ejercicio7.txt';
    fid = fopen(nombreArchivo, 'w');
    if fid ~= -1
        fprintf(fid, 'El factorial de %d es: %d\n', numero, factorialResultado);
        fclose(fid);
        disp(['El resultado se ha guardado en ' nombreArchivo]);

        % Almacenar el resultado en la variable 'salida'
        salida = num2str(factorialResultado);  % Convertir a texto

        % Conexión a la base de datos PostgreSQL
        pkg load database % Cargar el paquete

        conn = pq_connect(setdbopts('dbname','ExamenCorto1','host','localhost',
            'port','5432','user','postgres','password','gabrielgrdb'));

        query = sprintf("INSERT INTO salida VALUES ('%s');", salida);
        N = pq_exec_params(conn, query);

        if ~isempty(N)
            disp('El resultado se ha insertado en la base de datos.');
        else
            disp('Error al insertar en la base de datos.');
        end

        pq_close(conn);
    else
        disp('Error al abrir el archivo para escribir.');
    end
else
    disp('Error: El número no es divisible por 7.');
end

