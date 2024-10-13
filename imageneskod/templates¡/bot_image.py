import discord

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@bot.command()
async def mem(ctx):
    with open('imageskod/imagen2.jpg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

client.run("MTI5MjQ5NzA5Nzk3NDYxNjE5Ng.G3xkbf.HQLP9EXdmtqOlbUvECKQIH7qmJoa_sZR-zVS8g")