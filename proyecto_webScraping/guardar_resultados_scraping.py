def guardar_resultados_scraping(pagina, nombre, precio, categoria, imagen_url,url, archivo):
    with open(archivo, 'a',encoding='utf-8') as f:
        f.write(f"La página es: {pagina}\n")
        f.write(f"Nombre del Producto: {nombre}\n")
        f.write(f"Precio del Producto: {precio}\n")
        f.write(f"Categoría del Producto: {categoria}\n")
        f.write(f"URL de la Imagen: {imagen_url}\n")  # Guardar la URL de la imagen
        f.write(f"URL del produco: {url}\n")
        f.write("-" * 20 + "\n")
    
    print(f"Los resultados del scraping se han guardado en {archivo}")
