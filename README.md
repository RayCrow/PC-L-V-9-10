## PIA PROGRAMACION PARA CIBERSEGURIDAD 9-10 AM

1. Instalar requirements.txt

### Correr PIA.py

1. Identificar que herramienta usar
2. Dependiendo de la herramienta, la opcion a utilizar: metadata, cipher, nmap, hunter
3. Correr python PCPIA.py -opt ___herramienta___

### Modulo Metadata/WebScrapping 

1. Identificar la página web de la cuál obtendremos las imágenes a escanear
2. Correr python PCPIA.py -opt metadata -link ___Url___

### Modulo Cipher

1. Saber si quieres encriptar o desencriptar
2. Encriptar usar -enc, desencriptar usar -dec
3. Correr python PCPIA.py -opt cipher -dec ___frase___ o python PCPIA.py -opt cipher -enc ___frase___

### Modulo Hunter

1. Tener tu api de hunter.io
2. Correr python PCPIA.py -opt hunter -a ___apikey___ -c ___compañia___ -n ___numero de correos___

### Modulo Nmap

1. Saber tu ip (puedes visitar ifconfig.me para identificarla)
2. Dar un inicio y un fin para escanear un rango de puertos
3. Correr python PCPIA.py -opt SCANNETWORK -ip ___IpDelEquipo___ -pin ___PuertoInicial___ -pfi ___PuertoFinal___ o python PCPIA.py -opt SCANACTIVE
