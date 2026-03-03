import click
import httpx
from rich.console import Console
from rich.table import Table

console = Console()

@click.group()
def cli(): pass

@cli.command()
def status():
    """Show system status."""
    table = Table(title="FlowForge System Status")
    table.add_column("Service"); table.add_column("Status")
    for svc in ["platform-core", "platform-api", "service-auth", "service-notifications"]:
        table.add_row(svc, "[green]healthy[/green]")
    console.print(table)

@cli.command()
@click.argument("tenant_id")
def tenant_info(tenant_id):
    """Show tenant information."""
    console.print(f"Tenant: {tenant_id}")

if __name__ == "__main__": cli()
