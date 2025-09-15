def modo_ahorro():
    print("\nActivando modo ahorro...")
    for nombre, datos in dispositivos.items():
        if not datos["esencial"]:
            dispositivos[nombre]["estado"] = 0
            print(f"→ {nombre} no esencial puesto en estado inactivo.")
