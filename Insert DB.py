import pymysql
from main import btc_data
# Configurar conexão com o banco de dados MySQL
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='*****',
    db='******'
)

# Converter o índice para uma coluna normal
btc_data.reset_index(inplace=True)
btc_data.dropna(subset=['Media Movel', 'Mayer Multiple'], inplace=True)
# Inserir os dados no banco de dados
try:
    with connection.cursor() as cursor:
        for index, row in btc_data.iterrows():
            sql = """
            INSERT INTO btc (date, close, mv_av, mayer)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (row['Date'], row['Close'], row['Media Movel'], row['Mayer Multiple']))
    connection.commit()
finally:
    connection.close()

