import pandas as pd
#Read Dataset - MYSQL
import mysql.connector
#membuat konenksi ke databease financial di https://relational.fit.cvut.cz/datasaet/Financial
my_conn = mysql.connector.connect(
    host = "relational.fiz.cvut.cz",
    port = 3306,
    user = "guest",
    password = "relational",
    database = "financial",
    use_pure = True
)
