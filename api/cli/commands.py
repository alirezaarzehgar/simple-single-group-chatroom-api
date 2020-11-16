from ..common import db, app


@app.cli.command('db_init')
def db_init():
    db.create_all()

@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
