import pymysql
# מספר 1 
schema_name = "freedb_sql.freedb.tech2"

# Establishing a connection to DB
conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_freedb_test123456', passwd='UWk2nu8b8#2%82G', db=schema_name)
conn.autocommit(True)

# Getting a cursor from Database
# מחזיק את כל המידע של הטבלה  - פוינטר בדאטה בייס
# יכולת לקרוא ולכתוב דברים 
cursor = conn.cursor()

# Inserting data into table
statementToExecute = "CREATE TABLE `"+schema_name+"`.`users2`(`id` INT NOT NULL,`name` VARCHAR(50) NOT NULL,`created` DATETIME , PRIMARY KEY (`id`));"
cursor.execute(statementToExecute)

cursor.close()
conn.close()