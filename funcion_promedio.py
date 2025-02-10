

def calcular_precio_promedio(menu):
    precios = []

    for category in menu:
        if isinstance(category, dict):
            products = category.get("Products", [])
            for product in products:
                if isinstance(product, dict) and "Price" in product:
                    precios.append(product["Price"])
                elif isinstance(product, dict):
                    for subcategory in product.values():
                        if subcategory is not None:
                            for sub_product in subcategory:
                                if sub_product is not None and "Price" in sub_product:
                                    precios.append(sub_product["Price"])

    if precios:
        promedio_precio = sum(precios) / len(precios)
    else:
        promedio_precio = 0
        
    return promedio_precio


