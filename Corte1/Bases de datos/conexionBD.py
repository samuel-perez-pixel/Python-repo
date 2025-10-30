import psycopg2

conn = psycopg2.connect(
    host =  'localhost',
    database = 'postgres',
    user = 'postgres',
    password = 'post56',
    port = '5432'
)

cursor = conn.cursor()

cursor.execute('SELECT * FROM products')
rows = cursor.fetchall()

print()
for item in rows:
    print(item)
    print()