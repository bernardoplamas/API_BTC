import pymysql
from main import btc_data
# Configurar conexão com o banco de dados MySQL
conn = pymysql.connect(
    host='localhost',
    user='%%%%%%%%%%%%%%%%%%%%%%',
    password='%%%%%%%%%%%%%',
    db='new_schema'
)

# Converter o índice para uma coluna normal
btc_data.reset_index(inplace=True)

btc_data=btc_data.dropna(subset=['Media Movel', 'Mayer Multiple'], inplace=True)

