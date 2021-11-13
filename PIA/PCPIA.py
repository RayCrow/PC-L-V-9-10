def Main():
    info = 'PIA CIBERSEGURIDAD 2021'
    parser = argparse.ArgumentParser(info)

    parser.add_argument('-opt', '--option', required = True, help = 'Opcion para elegir script a utilizar.', dest = 'opt')

    #Escaneo de Puertos
    parser.add_argument('-ip', '--ip', help = 'Ingrese la ip a escanear')

    parser.add_argument('-pin', '--pin', help = 'Primer puerto a analizar.')
    parser.add_argument('-pfi', '--pfi', help = 'Ultimo puerto a analizar.')
    
    #ENCRIPTAR
    parser.add_argument('-enc', '--enc', help = 'Ruta del directorio a encriptar.')
    #DESENCRIPTAR
    parser.add_argument('-dec', '--dec', help = 'Ruta del directorio a desencriptar.')
    
    #Hunter
    parser.add_argument('-a', '--api', help = 'Agrega tu API key.')
    parser.add_argument('-c', '--company', help = 'Nombre de la compañía.')
    parser.add_argument('-n', '--numero', help = 'Numero de correos (Maximo 10 si tienes plan gratuito).')

    #Web Scraping y Metadata
    parser.add_argument('-link', '--link', help = 'Ingrese la url del sitio web donde estan las imagenes a descargar') 

    args = parser.parse_args()
    
    if args.opt.upper() == 'SCANNETWORK':
        ip = args.ip
        pin = args.pin
        pfi = args.pfi
        PowerS.getScanNetwork(ip, pin, pfi)

    if args.opt.upper() == 'SCANACTIVE':
        PowerS.getScanActive()

    if args.opt.upper() == 'HUNTER':
        api = args.api
        company = args.company
        numero = args.numero
        huntermail.hunterio(api,company,numero)
    
    if args.opt.upper() == 'METADATA':
        url = args.link
        scrapmeta.scrapingImages(url)
        scrapmeta.printMeta()
        
    if args.opt.upper()== 'ENCRIPTAR':
         path_to_encrypt = args.enc
         encrypt.main(path_to_encrypt)

    if args.opt.upper()== 'DESENCRIPTAR':
         path_to_encrypt = args.dec
         decrypt.main(path_to_encrypt)


                      
if __name__ == '__main__':
    import argparse
    import PowerS
    import huntermail
    import scrapmeta
    import encrypt
    import decrypt
    
    Main()
    
    
    
