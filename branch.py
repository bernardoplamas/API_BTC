import asyncio
from telegram import Bot
import yfinance as yf
import datetime
import schedule
import time

# Configurar o bot do Telegram
TELEGRAM_TOKEN = ''
CHAT_ID = ''
bot = Bot(token=TELEGRAM_TOKEN)

async def fetch_and_send_data():
    start_date = datetime.datetime(2010, 1, 1)
    end_date = datetime.datetime.now().strftime('%Y-%m-%d')

    # Baixar dados do Bitcoin
    btc_data = yf.download('BTC-USD', start=start_date, end=end_date)

    # Calcular média móvel de 200 dias e indicador de Mayer
    btc_data['Media Movel'] = btc_data['Close'].rolling(window=200).mean()
    btc_data['Mayer Multiple'] = btc_data['Close'] / btc_data['Media Movel']

    # Remover linhas com valores nulos
    btc_data.dropna(subset=['Media Movel', 'Mayer Multiple'], inplace=True)

    # Enviar mensagem com os dados mais recentes
    last_row = btc_data.iloc[-1]
    message = (
        f"Data: {last_row.name.date()}\n"
        f"Preço de Fechamento: ${last_row['Close']:.2f}\n"
        f"Média Móvel 200 Dias: ${last_row['Media Movel']:.2f}\n"
        f"Indicador de Mayer: {last_row['Mayer Multiple']:.2f}"
    )
    await bot.send_message(chat_id=CHAT_ID, text=message)

async def main():
    # Agendar a tarefa para ser executada a cada 5 minutos
    schedule.every(5).minutes.do(lambda: asyncio.create_task(fetch_and_send_data()))

    # Loop principal para continuar agendando tarefas
    try:
        while True:
            schedule.run_pending()
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        print("\nInterrompido pelo usuário. Saindo...")

def run_bot():
    asyncio.run(main())

if __name__ == "__main__":
    run_bot()
