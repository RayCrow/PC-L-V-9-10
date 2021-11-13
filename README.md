## PIA PROGRAMACION PARA CIBERSEGURIDAD 9-10 AM

1. Instalar requirements.txt

### Correr PCPIA.py

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

### Modulo Nmap (ScanActive/ScanNetwork)

1. Determinar la ip a evaluar
2. Si no tienes una ip, puedes usar la herramienta SCANACTIVE (-opt SCANACTIVE) para verificar las ip que responden
3. Establecer un rango de puertos
4. Inicializar python PCPIA.py -opt ___SCANNETWORK___ -ip ___IpDelEquipo___ -pin ___PuertoInicial___ -pfi ___PuertoFinal___
