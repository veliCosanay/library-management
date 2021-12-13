import psycopg2


class DataBase:

    def connect(self):

        self.conn = psycopg2.connect(user="postgres",
                              password="postgres",
                              host="localhost",
                              port="5432",
                              database="postgres")
        self.cur = self.conn.cursor()   

    def TabloUye(self):

        try:
            self.connect()
            komut_CREATE = """ CREATE TABLE users(
                    id SERIAL PRIMARY KEY,
                    userName TEXT NOT NULL,
                    password TEXT NOT NULL
                    );
                    """
            self.cur.execute(komut_CREATE)
            self.conn.commit()
            
        except psycopg2.DatabaseError:
            print("Verı tababnına baglantı saglanamadı")
        else:
            
            pass
        finally:
            self.conn.close()          

        # users(id, username, password, name, surname)
    
    def UyeEkle(self, userName, password):
        
        try:
            self.connect()
            komut_ekle = f"INSERT INTO users(userName,password) VALUES('{userName}', '{password}')"

            self.cur.execute(komut_ekle)
            self.conn.commit()
        except Exception:
            return "Hata oluştu"
        finally:
            self.conn.close()
    
    def UyeKontrol(self,userName, password):

        try:
            self.connect()
            komut_select = f"SELECT * FROM users WHERE userName='{userName}' AND password='{password}'"
            self.cur.execute(komut_select)
            
            data = self.cur.fetchone()
            if data is not None:
                return True
            return False 
        except Exception:
            pass
        finally:
            self.conn.close()
            
    def TabloKitap(self):
        # books(id, name, author, number_of_pages, publisher)
        try:
            self.connect()
            komut_CREATE = """ CREATE TABLE books(
                    id SERIAL PRIMARY KEY,
                    name TEXT NOT NULL,
                    author TEXT NOT NULL,
                    number_of_pages INTEGER,
                    publisher TEXT NOT NULL
                    );
                    """
            self.cur.execute(komut_CREATE)
            self.conn.commit() 
        except Exception:
            print("tablo oluşurken hata var")
        finally:
            self.conn.close() 

    def KitapListele(self):

        try:
            self.connect()
            komut_SELECT = "SELECT * FROM books ORDER BY id ASC;"
            self.cur.execute(komut_SELECT)

            liste = self.cur.fetchall()
        except Exception:
            pass
        else:
            return liste
        finally:
            self.conn.close()        

    
    def KitapEkle(self,name,author,number_of_pages,publisher):

        try:
            self.connect()
            komut_ekle = f"INSERT INTO books(name, author, number_of_pages, publisher) VALUES('{name}', '{author}', '{number_of_pages}', '{publisher}');"
            self.cur.execute(komut_ekle)
            self.conn.commit()
        except:
            pass
        finally:
            self.conn.close()

    def KitapDüzenle(self,id,name,author,number_of_pages,publisher):
        
        try:
            self.connect()
            komut_UPDATE = f"UPDATE books SET name='{name}', author='{author}',\
                 number_of_pages={int(number_of_pages)}, publisher='{publisher}'\
                      WHERE id={id};"
            self.cur.execute(komut_UPDATE)
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.conn.close()
    
    def duzen(self, id):
        try:
            self.connect()
            komut_SELECT = f"SELECT * FROM books WHERE id={int(id)};"
            self.cur.execute(komut_SELECT)

            data = self.cur.fetchone()
        except Exception:
            pass
        finally:
            self.conn.close()    
        return data