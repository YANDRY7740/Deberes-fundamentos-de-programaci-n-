def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicando el porcentaje al monto total de la compra.

    Parameters:
        monto_total (float): Monto total de la compra.
        porcentaje_descuento (float, optional): Porcentaje de descuento. Por defecto es 10%.

    Returns:
        float: Monto del descuento calculado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


def main():
    # Llamada a la función con solo el monto total de la compra
    monto_compra_1 = 300
    descuento_1 = calcular_descuento(monto_compra_1)
    monto_final_1 = monto_compra_1 - descuento_1
    print("Monto total de la compra:", monto_compra_1)
    print("Porcentaje de descuento:", 15)
    print("Monto del descuento:", descuento_1)
    print("Monto final a pagar después del descuento:", monto_final_1)
    print()

    # Llamada a la función con el monto total de la compra y un porcentaje de descuento personalizado
    monto_compra_2 = 200
    porcentaje_descuento_2 = 20
    descuento_2 = calcular_descuento(monto_compra_2, porcentaje_descuento_2)
    monto_final_2 = monto_compra_2 - descuento_2
    print("Monto total de la compra:", monto_compra_2)
    print("Porcentaje de descuento:", porcentaje_descuento_2)
    print("Monto del descuento:", descuento_2)
    print("Monto final a pagar después del descuento:", monto_final_2)


if __name__ == "__main__":
    main()
