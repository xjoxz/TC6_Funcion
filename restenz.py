def enzima(secuencia, enzima):
    fragmentos = []
    sitio_empalme = secuencia.find(enzima)

    while sitio_empalme != -1:
        fragmento = secuencia[:sitio_empalme]
        fragmentos.append(fragmento)
        secuencia = secuencia[sitio_empalme + len(enzima):]
        sitio_empalme = secuencia.find(enzima)

    fragmentos.append(secuencia)
    return(fragmentos)