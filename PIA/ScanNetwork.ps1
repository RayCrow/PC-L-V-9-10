# PIA PC 
#
# 
# Escaneo de puertos dada una ip
# 
#
#

 Param( 
    [Parameter(Mandatory)][String] $ip,
    [Parameter(Mandatory)][String] $pin,
    [Parameter(Mandatory)][String] $pfi
    )

$subred = (Get-NetRoute -DestinationPrefix 0.0.0.0/0).NextHop
Write-Host "Tu gateway es: "$subred

$rango = $subred.Substring(0,$subred.IndexOf('.') + 1 + $subred.Substring($subred.IndexOf('.') + 1).IndexOf('.') + 3)

$punto = $rango.EndsWith('.')
if ( $punto -like "False") {
    $rango = $rango + '.'
}

$porttoscan = $pin..$pfi
$waittime = 100

foreach ( $p in $porttoscan) {

    $TCPObject = new-object System.Net.Sockets.Tcpclient
        try{
            $resultado = $TCPObject.ConnectAsync($ip,$p).Wait($waittime)
        }catch{}
        if ( $resultado -eq "True") {
            Write-Host "Puerto Abierto: " -NoNewline; Write-Host $p -ForegroundColor Green
            }
        else {
            Write-Host "Puerto Cerrado: " -NoNewline; Write-Host $p -ForegroundColor Red
        }
        }

     
        