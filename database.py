import aiosqlite

class DataBase:
    def __init__(self, db_name="base.db") -> None:
        self.db_name = db_name

    async def init(self):
        async with aiosqlite.connect(self.db_name) as db:
            await db.execute("""CREATE TABLE IF NOT EXISTS test (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url TEXT NOT NULL,
                status_code INTEGER,
                time REAL,
                ok BOOLEAN
            )""")
            await db.commit()

    async def save(self, url, status_code, time, ok):
        async with aiosqlite.connect(self.db_name) as db:
            await db.execute("INSERT INTO test (url, status_code, time, ok) VALUES (?, ?, ?, ?)", (url, status_code, time, ok))
            await db.commit()

    async def fetch(self):
        async with aiosqlite.connect(self.db_name) as db:
            return await db.execute_fetchall("SELECT * FROM test")
