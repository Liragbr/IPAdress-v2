import asyncio
from rich.console import Console
from src.services.ipinfo_service import IpInfoService
from src.utils.input_validator import is_valid_ip

console = Console()

async def main():
    banner = r"""


 ██▓ ██▓███      ▄▄▄      ▓█████▄ ▓█████▄  ██▀███  ▓█████   ██████   ██████ 
▓██▒▓██░  ██▒   ▒████▄    ▒██▀ ██▌▒██▀ ██▌▓██ ▒ ██▒▓█   ▀ ▒██    ▒ ▒██    ▒ 
▒██▒▓██░ ██▓▒   ▒██  ▀█▄  ░██   █▌░██   █▌▓██ ░▄█ ▒▒███   ░ ▓██▄   ░ ▓██▄   
░██░▒██▄█▓▒ ▒   ░██▄▄▄▄██ ░▓█▄   ▌░▓█▄   ▌▒██▀▀█▄  ▒▓█  ▄   ▒   ██▒  ▒   ██▒
░██░▒██▒ ░  ░    ▓█   ▓██▒░▒████▓ ░▒████▓ ░██▓ ▒██▒░▒████▒▒██████▒▒▒██████▒▒
░▓  ▒▓▒░ ░  ░    ▒▒   ▓▒█░ ▒▒▓  ▒  ▒▒▓  ▒ ░ ▒▓ ░▒▓░░░ ▒░ ░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░
 ▒ ░░▒ ░          ▒   ▒▒ ░ ░ ▒  ▒  ░ ▒  ▒   ░▒ ░ ▒░ ░ ░  ░░ ░▒  ░ ░░ ░▒  ░ ░
 ▒ ░░░            ░   ▒    ░ ░  ░  ░ ░  ░   ░░   ░    ░   ░  ░  ░  ░  ░  ░  
 ░                    ░  ░   ░       ░       ░        ░  ░      ░        ░      
                           ░       ░                                        
                           ░       ░                               
    """

    console.print(f"[bold blue]{banner}[/bold blue]")
    console.rule("[bold blue]IP Geolocation - by Lira[/bold blue]")

    ip = console.input("[bold yellow]Enter IP address:[/bold yellow] ").strip()

    if not is_valid_ip(ip):
        console.print("[red]Endereço IP inválido.[/red]")
        return

    service = IpInfoService()
    ip_data = await service.get_ip_info(ip)

    if not ip_data:
        console.print("[red]Falha ao obter informações do IP.[/red]")
        return

    console.clear()
    console.print("[bold green]=== IP INFORMATION ===[/bold green]")
    console.print(f"[cyan]Country:[/cyan] {ip_data.country}")
    console.print(f"[cyan]Region:[/cyan] {ip_data.region}")
    console.print(f"[cyan]City:[/cyan] {ip_data.city}")
    console.print(f"[cyan]Organization:[/cyan] {ip_data.org}")
    console.print(f"[cyan]Postal Code:[/cyan] {ip_data.postal}")

    coords = ip_data.get_coordinates()
    if coords:
        lat, lon = coords
        console.print(f"[cyan]Coordinates:[/cyan] {lat}, {lon}")
        console.print(f"[cyan]Google Maps:[/cyan] https://www.google.com/maps/?q={lat},{lon}")
    else:
        console.print("[yellow]Coordenadas indisponíveis.[/yellow]")

if __name__ == "__main__":
    asyncio.run(main())
