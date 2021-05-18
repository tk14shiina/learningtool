import mysql.connector as connector


class DBHelper:
    def __init__(self):
        self.con = connector.connect(host='localhost',
                                     port='3306',
                                     user='root',
                                     password='',
                                     database='test')
        query = 'create table if not exists studySets(studySetId int primary key auto_increment, studySetName varchar(200))'        
        cur = self.con.cursor()
        cur.execute(query)                     
        query2 = 'create table if not exists wordlist(wordId int primary key auto_increment, studySetId int, word varchar(200), definition varchar(200), foreign key (studySetId) references studySets(studySetId) on delete cascade on update cascade)'
        cur2 = self.con.cursor()
        cur2.execute(query2)
        print("Created")

    #Insert
    def insert_word(self, studySetId, word, definition):
        query = "insert into wordlist(studySetId, word, definition) values('{}', '{}','{}')".format(
            studySetId, word, definition)
        #print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user saved to db")

    #Fech All
    def fetch_all_word(self):
        query = "select * from wordlist".format()
        cur = self.con.cursor()
        cur.execute(query)
        
        resWord = []
        for row in cur:
            print("Word Id : ", row[0])
            resWord.append([row[0], row[1], row[2], row[3]])
            print("StudySet Id : ", row[1])
            print("Word :", row[2])
            print("Definition : ", row[3])
            print()
        return resWord

    #Fech All
    def fetch_one_word(self, studySetId):
        query = "select * from wordlist where studySetId = {} order by rand() limit 1".format(
            studySetId)
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("word : ", row[2])
            return [row[2], row[3]]

    #delete user
    def delete_word(self, studySetId, wordId):
        query = "delete from wordlist where studySetId = {} and wordId= {}".format(
            studySetId, wordId)
        print(query)
        c = self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("deleted")

    #update
    def update_word(self, studySetId, wordId, newWord, newDefinition):
        query = "update wordlist set word ='{}', definition = '{}'  where studySetId = {} and wordId={}".format(
            newWord, newDefinition, studySetId, wordId)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated")

    def update_studySet(self, studySetId, newstudySetName):
        query = "update studySets set studySetName ='{}' where studySetId={}".format(
            newstudySetName, studySetId)
        print("HEllo")
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated")

    def insert_studySet(self, studySetName):
        query = "insert into studySets(studySetName) values('{}')".format(
            studySetName)
        #print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user saved to db")

    #Fech All
    def fetch_all_studySet(self):
        query = "select * from studySets"
        cur = self.con.cursor()
        cur.execute(query)
        res = []
        for row in cur:
            res.append([row[0], row[1]])
            print("studySet Id : ", row[0])
            print("studySetName :", row[1])
            print()
        return res

    def fetch_one_studySet(self, studySetId):
        query = "select * from studySets where studySetId = {}".format(studySetId)
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("studySet : ", row[1])

    #delete user
    def delete_studySet(self, studySetId):
        query = "delete from studySets where studySetId= {}".format(studySetId)
        print(query)
        c = self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("deleted")

    #update

    def update_studySet(self, studySetId, newstudySetName):
        query = "update studySets set studySetName ='{}' where studySetId={}".format(
            newstudySetName, studySetId)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated")
