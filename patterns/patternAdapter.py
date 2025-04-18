import abc


class SQLite:
    def connect(self, host, port, username, password):
        pass

    def cursor(self, query):
        pass

    def commit(self):
        pass


class MySQLConnector:
    def conn(self, uri):
        pass

    def comm(self):
        pass

    def exec(self, query):
        pass


class BaseDBConnector(abc.ABC):
    db: object
    @abc.abstractmethod
    def connect(self, host, port, username, password):
        pass

    @abc.abstractmethod
    def cursor(self):
        pass

    @abc.abstractmethod
    def commit(self):
        pass


class SQLiteDBConnectorAdapter(BaseDBConnector):
    db:SQLite
    def connect(self, host, port, username, password):
        self.db.connect(host,port,username,password)

    def cursor(self,query):
        self.db.cursor(query)


    def commit(self):
        self.db.commit()



class MySQLDBConnectorAdapter(BaseDBConnector):
    db:MySQLConnector
    def connect(self, host, port, username, password):
        self.db.conn(host,port,username,password)

    def cursor(self,query):
        self.db.exec(query)


    def commit(self):
        self.db.comm()





...




db = MySQLDBConnectorAdapter()
db.commit('SELECT * from MY_TABLE')

...
