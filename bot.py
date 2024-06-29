from main import btc_data
from insert_DB import conn
import asyncio
from telegram import Bot

# Configurar o bot do Telegram
TELEGRAM_TOKEN = '%%%%%%%%%%%%%%%%%%%%%%%%%'
CHAT_ID = '%%%%%%%%%%%%%%%%%%%'
bot = Bot(token=TELEGRAM_TOKEN)

# Função para formatar os dados em uma mensagem
def format_message(row):
    message = (
        f"Data: {row['Date'].date()}\n"
        f"Preço de Fechamento: ${row['Close']:.2f}\n"
        f"Média Móvel 200 Dias: ${row['Media Movel']:.2f}\n"
        f"Indicador de Mayer: {row['Mayer Multiple']:.2f}"
    )
    return message

# Função assíncrona para enviar a mensagem
async def send_telegram_message(message):
    await bot.send_message(chat_id=CHAT_ID, text=message)


def main():
    # Enviar os dados recentes para o grupo do Telegram
    try:
        with conn.cursor() as cursor:
            for index, row in btc_data.iterrows():
                sql = """
                INSERT INTO btc (date, close, mv_av, mayer)
                VALUES (%s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                    close = VALUES(close),
                    mv_av = VALUES(mv_av),
                    mayer = VALUES(mayer)
                """
                cursor.execute(sql, (row['Date'], row['Close'], row['Media Movel'], row['Mayer Multiple']))
        conn.commit()


        # Enviar mensagem com os dados mais recentes
        last_row = btc_data.iloc[-1]
        message = format_message(last_row)
        asyncio.run(send_telegram_message(message))
    finally:
        conn.close()

if __name__ == "__main__":
    main()