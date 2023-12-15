
function salida = calcular_y_guardar_areas()

    % Menú de selección
    fprintf('Seleccione la figura geométrica:\n');
    fprintf('1. Círculo\n');
    fprintf('2. Triángulo\n');
    fprintf('3. Cuadrado\n');
    fprintf('4. Rectángulo\n');

    opcion = input('Ingrese el número de la opción deseada: ');

    switch opcion
        case 1
            % Área de un círculo
            radio = input('Ingrese el radio del círculo: ');
            area = pi * radio^2;
            figura = 'Círculo';

        case 2
            % Área de un triángulo
            base = input('Ingrese la base del triángulo: ');
            altura = input('Ingrese la altura del triángulo: ');
            area = 0.5 * base * altura;
            figura = 'Triángulo';

        case 3
            % Área de un cuadrado
            lado = input('Ingrese el lado del cuadrado: ');
            area = lado^2;
            figura = 'Cuadrado';

        case 4
            % Área de un rectángulo
            base = input('Ingrese la base del rectángulo: ');
            altura = input('Ingrese la altura del rectángulo: ');
            area = base * altura;
            figura = 'Rectángulo';

        otherwise
            fprintf('Opción no válida.\n');
            salida = [];
            return;
    end

    % Mostrar el resultado
    fprintf('El área del %s es: %.4f\n', figura, area);

    % Crear la cadena de texto
    cadena_resultado = sprintf('Figura: %s, Área: %.4f', figura, area);

    % Guardar la cadena en la variable salida
    salida = struct('cadena_resultado', cadena_resultado);

    % Guardar el resultado en un archivo de texto
    guardar_en_archivo(cadena_resultado);

end

function guardar_en_archivo(cadena_resultado)
    % Abrir el archivo en modo de escritura
    archivo = fopen('ejercicio12.txt', 'a');

    % Verificar si se pudo abrir el archivo
    if archivo == -1
        fprintf('Error al abrir el archivo.\n');
        return;
    end

    % Escribir el resultado en el archivo
    fprintf(archivo, '%s\n', cadena_resultado);


    % Cerrar el archivo
    fclose(archivo);

        % Conexión a la base de datos PostgreSQL
        pkg load database % Cargar el paquete

        conn = pq_connect(setdbopts('dbname','ExamenCorto1','host','localhost',
            'port','5432','user','postgres','password','gabrielgrdb'));

        query = sprintf("INSERT INTO salida VALUES ('%s');", cadena_resultado);
        N = pq_exec_params(conn, query);


    fprintf('Resultado guardado en "ejercicio12.txt".\n');
end



