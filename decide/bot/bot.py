# Importamos las librerías necesarias
from telegram.ext import MessageHandler, Filters, Updater, CommandHandler

# Método que imprimirá por pantalla la información que reciba
def listener(bot, update):
    id = update.message.chat_id
    mensaje = update.message.text

    print("ID: " + str(id) + " MENSAJE: " + mensaje)


# Método que utilizaremos para cuando se mande el comando de "start"
def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text='¡Bienvenido al bot de Alfonso sobre la plataforma de voto Decide!')


# Método que mandará el mensaje "¡Hola, usuario!"
def hola_mundo(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text='¡Hola, usuario de Decide!')

def vivo(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text='¡Estoy vivo padre ,VIVOOOOO!')
    bot.sendPhoto(chat_id=update.message.chat_id, photo=open('vivo.jpg', 'rb'))

def web(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text='La plataforma de despliege que he utilizado es Heroku')
    bot.sendPhoto(chat_id=update.message.chat_id, photo=open('heroku.png', 'rb'))
    bot.sendMessage(chat_id=update.message.chat_id, text='Buenas, aquí tiene la página:'+'\n'+' https://decidevisualizacion.herokuapp.com/doc/')

def votaciones(bot, update):
        bot.sendMessage(chat_id=update.message.chat_id, text='Las votaciones en las que aun puedes particicpar son las siguientes:')

def logo(bot, update):
    # Enviamos de vuelta una foto. Primero indicamos el ID del chat a donde
    # enviarla y después llamamos al método open() indicando la dónde se encuentra
    # el archivo y la forma en que queremos abrirlo (rb = read binary)
    bot.sendPhoto(chat_id=update.message.chat_id, photo=open('logo.png', 'rb'))

# Método que mandará el logo de la página
def logo(bot, update):
    # Enviamos de vuelta una foto. Primero indicamos el ID del chat a donde
    # enviarla y después llamamos al método open() indicando la dónde se encuentra
    # el archivo y la forma en que queremos abrirlo (rb = read binary)
    bot.sendPhoto(chat_id=update.message.chat_id, photo=open('logo.jpg', 'rb'))


def resultados(bot, update):
    # Enviamos de vuelta una foto. Primero indicamos el ID del chat a donde
    # enviarla y después llamamos al método open() indicando la dónde se encuentra
    # el archivo y la forma en que queremos abrirlo (rb = read binary)
    bot.sendPhoto(chat_id=update.message.chat_id, photo=open('Formato.jpg', 'rb'))

def correo(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text='La notificación por correo electrónico esta pendiente de implementación')
    bot.sendPhoto(chat_id=update.message.chat_id, photo=open('notyet.png', 'rb'))

def resultadosQueso(bot, update):
    # Enviamos de vuelta una foto. Primero indicamos el ID del chat a donde
    # enviarla y después llamamos al método open() indicando la dónde se encuentra
    # el archivo y la forma en que queremos abrirlo (rb = read binary)
    bot.sendPhoto(chat_id=update.message.chat_id, photo=open('Queso.jpg', 'rb'))


# Método que mandará el mensaje "¡Hola, usuario!"
def requeriments(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text='Necesitaras estos requisitos si quieres ejecutar el proyecto en local:')
    bot.send_photo(chat_id=update.message.chat_id, photo='https://i.kym-cdn.com/entries/icons/original/000/018/326/TXT_File.png')
    bot.send_document(chat_id=update.message.chat_id, document=open('requirementsTelegram.txt', 'rb'))

def comandos(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text='Buenas,los comandos  disponibles son los siquientes: \n'
                    '/start \n'
                    '/holamundo \n'
                    '/votaciones \n'
                    '/logo \n'
                    '/vivo \n'
                    '/web \n'
                    '/requeriments \n'
                    '/resultados \n'
                    '/resultadosQueso \n'
                    '/correo \n'

                    )


def main():
    # Creamos el Updater, objeto que se encargará de mandarnos las peticiones del bot
    # Por supuesto no os olvidéis de cambiar donde pone "TOKEN" por el token que os ha dado BotFather
    updater = Updater("753679513:AAHwHg8zTSP6DnXdyQ9GEmLWabY71Y-zW2Y")

    # Cogemos el Dispatcher, en el cual registraremos los comandos del bot y su funcionalidad
    dispatcher = updater.dispatcher

    # Registramos el método que hemos definido antes como listener para que muestre la información de cada mensaje
    listener_handler = MessageHandler(Filters.text, listener)
    dispatcher.add_handler(listener_handler)

    # Ahora registramos cada método a los comandos necesarios
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("holamundo", hola_mundo))
    dispatcher.add_handler(CommandHandler("logo", logo))
    dispatcher.add_handler(CommandHandler("vivo", vivo))
    dispatcher.add_handler(CommandHandler("votaciones", votaciones))
    dispatcher.add_handler(CommandHandler("web", web))
    dispatcher.add_handler(CommandHandler("comandos", comandos))
    dispatcher.add_handler(CommandHandler("requeriments", requeriments))
    dispatcher.add_handler(CommandHandler("resultados", resultados))
    dispatcher.add_handler(CommandHandler("resultadosQueso", resultadosQueso))
    dispatcher.add_handler(CommandHandler("correo", correo))








    # Y comenzamos la ejecución del bot a las peticiones
    updater.start_polling()
    updater.idle()


# Llamamos al método main para ejecutar lo anterior
if __name__ == '__main__':
    main()