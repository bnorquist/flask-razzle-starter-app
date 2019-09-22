from app import app

def initilize_db_tables():
    # this needs to be called sometime before you interact with the database
    with app.app_context():
        #db.create_all()
        pass