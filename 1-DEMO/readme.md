### sync.py

1. *hacemos un `with` stament*
2. traemos *la funcion `sync_playwright()` y la llamamos `p` → la `p` va a estar utilizando los comandos de la libreria playwright*
3. variable `browser` → le asignamos el valor de `p.chromium.launch()`
    1. Para mostrar la ejecución del browser, le pasamos a `launch()` el parámetro de `headless=False`
4. `page` → apunta a `browser` y usamos el método `.new_page()`
5. utilizamos el `page` para ir a un web site con el método `.goto(<url>)`
6. tomar screenshot → `.screenshot(path="demo.png")`
7. `browser.close()` → cierra la instancia del browser

### async.py

**`asyncio`** →  Es una librería de python que permite manejar de forma **asincrona** la ejecución de playwright

1. Creamos una función asincrona, para q posteriormente instanciarla o llamarla con **`asyncio`**
2. `print(await page.title())` → Imprime el texto del titulo (de `head`) en consola 
3. llamamos al a funcion `main()` utilizando `asyncio`