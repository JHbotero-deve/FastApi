import inventario


def main():
    productos = []
    inventario.agregar_producto(productos, 'Lapicero', 1.5)
    inventario.agregar_producto(productos, 'Cuaderno', 3.2)
    inventario.agregar_producto(productos, 'Borrador', 0.8)

    total = inventario.calcular_total(productos)
    print('Total inventario:', total)

    reporte = 'REPORTE DE INVENTARIO\n'
    for p in productos:
        reporte += f"- {p['nombre']}: {p['precio']}\n"
    reporte += f"TOTAL: {total}\n"

    try:
        with open('reporte.txt', 'w', encoding='utf-8') as f:
            f.write(reporte)
        print('Reporte guardado en reporte.txt')
    except Exception as e:
        print('Error al escribir el archivo de reporte:', e)


if __name__ == '__main__':
    main()
