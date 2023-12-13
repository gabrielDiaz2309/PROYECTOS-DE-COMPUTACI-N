
pkg load database

% Función para conectarse a la base de datos PostgreSQL
function conn = connect_to_db()
    conn = pq_connect(setdbopts('dbname', 'Ejercicio', 'host', 'localhost', 'port', '5432', 'user', 'postgres', 'password', 'gabrielgrdb'));
end

% Función para agregar venta en la base de datos
function agregar_venta_en_db()
    conn = connect_to_db();

    try
        nombre_producto = input("Ingrese el nombre del producto: ", 's');
        precio = input("Ingrese el precio del producto en: Q ");
        descuento = input("Ingrese el porcentaje de descuento (0 si no hay oferta): ");

        precio_oferta = precio - (precio * (descuento / 100));
        iva = precio * 0.12;
        precio_sin_iva = precio - iva;
        fecha_actual = datestr(now, 'yyyy-mm-dd HH:MM:SS');

        Ins1 = 'INSERT INTO productos (nombre, precio, precio_oferta, fecha) VALUES (';
        Ins2 = ');';
        Instruccion = strcat(Ins1, "'", nombre_producto, "', ", num2str(precio), ', ', num2str(precio_oferta), ', ''', fecha_actual, '''', Ins2);
        Registro = pq_exec_params(conn, Instruccion);
        fprintf("Datos de venta agregados a la base de datos.\n");

        fprintf("El precio sin IVA es de Q%.2f, por lo que el IVA es de Q%.2f\n", precio_sin_iva, iva);
    catch e
        disp(['Error durante la conexión a la DB, consulte sobre el error: ' e.message]);
    end

    pq_close(conn);
end

% Función para mostrar historial de la base de datos
function mostrar_historial()
    conn = connect_to_db();

    try
        consulta = 'SELECT * FROM productos;';
        resultado = pq_exec_params(conn, consulta);
        fprintf('%-4s %-20s %-10s %-15s %-20s\n', 'ID', 'Nombre', 'Precio', 'Precio Oferta', 'Fecha');
        fprintf('------------------------------------------------------------\n');
        for i = 1:size(resultado.data, 1)
            fprintf('%-4d %-20s Q%-9.2f Q%-14.2f %-20s\n', resultado.data{i, 1}, resultado.data{i, 2}, resultado.data{i, 3}, resultado.data{i, 4}, resultado.data{i, 5});
        end
    catch e
        disp(['Error durante la conexión a la DB, consulte sobre el error: ' e.message]);
    end

    pq_close(conn);
end

% Menú interactivo
while true
    fprintf("Menú:\n");
    fprintf("1. Agregar datos de venta\n");
    fprintf("2. Mostrar historial\n");
    fprintf("3. Salir\n");

    opciones_validas = ["1", "2", "3"];
    opcion = input("Seleccione una opción: ", 's');

    if ismember(opcion, opciones_validas)
        if opcion == "1"
            try
                agregar_venta_en_db();
            catch e
                disp(['Error: ' e.message]);
            end
        elseif opcion == "2"
            mostrar_historial();
        elseif opcion == "3"
            fprintf("Saliendo del programa.\n");
            break;
        end
    else
        fprintf("Opción no válida. Por favor, seleccione una opción válida.\n");
    end
end

