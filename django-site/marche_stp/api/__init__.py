def callDB(db, query):
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()
    
def getDB():
#    return .connect("db.sqlite3")
    return None 