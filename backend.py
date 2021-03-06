import sqlite3

# https://www.sqlite.org/datatype3.html


main_f=''
import pandas as pd



def connect():
    conn=sqlite3.connect(f'{main_f}gen_tree.db')
    cur=conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS family (
                                    id INTEGER PRIMARY KEY, 
                                    name TEXT, 
                                    surname TEXT, 
                                    
                                    date_birth TEXT,
                                    date_death TEXT,
                                    
                                    mother_id INTEGER,
                                    father_id INTEGER,
                                    spouse_id INTEGER,
                                    
                                    generation INTEGER,
                                    cluster INTEGER,
                                    
                                    gender INTEGER,
                                    

                                    place_birth	TEXT,
                                    country_birth	 TEXT,
                                    country           TEXT,
                                    comments	TEXT                                  	
                                    
                                    
                                    )'''
                                    
 
    )
    conn.commit()
    conn.close()

def insert(id,   
          name, 
                                                            surname,                                   
                                                            date_birth,
                                                            date_death,
                                                            mother_id,
                                                            father_id,
                                                            spouse_id,                                   
                                                            generation,
                                                            cluster, 
                                                            gender,
                                                            place_birth,
                                                            country_birth,
                                                            country,
                                                            comments):
    conn=sqlite3.connect(f'{main_f}gen_tree.db')
    cur=conn.cursor()

    cur.execute("INSERT INTO family VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(  
                                                            id,   
          name, 
                                                            surname,                                   
                                                            date_birth,
                                                            date_death,
                                                            mother_id,
                                                            father_id,
                                                            spouse_id,                                   
                                                            generation,
                                                            cluster, 
                                                            gender,
                                                            place_birth,
                                                            country_birth,
                                                            country,
                                                            comments))
    conn.commit()
    conn.close()



def view():
    conn=sqlite3.connect(f'{main_f}gen_tree.db')
    cur=conn.cursor()
    cur.execute("SELECT * FROM family")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(name="",surname="",date_birth="",generation=""):
    import numpy as np
    conn=sqlite3.connect(f'{main_f}gen_tree.db')
    cur=conn.cursor()
    
    lst=[name,surname,date_birth,generation]
    lst_n=['name','surname','date_birth','generation']
    
    strk=''
    nones=['nan', np.nan, None, "NaN", '']
    
    for i in range(0,len(lst)):
        if not (pd.isnull(lst[i]) or lst[i] in nones):
            if len(strk)==0:
                if lst_n[i] in ['name','surname','date_birth']:
                    strk=f"{lst_n[i]}='{lst[i]}'"
                else:
                    strk=f"{lst_n[i]}={lst[i]}" 
            else:
                if lst_n[i] in ['name','surname','date_birth']:
                    strk=f"{strk} AND {lst_n[i]}='{lst[i]}'"
                else:
                    strk=f"{strk} AND {lst_n[i]}={lst[i]}" 
    
    # cur.execute("SELECT * FROM family WHERE name=? OR surname=? OR date_birth=? OR generation=?", (name,surname,date_birth,generation))
    if len(strk)>0:
        sql_s=f"SELECT * FROM family WHERE {strk}"
    else:
        sql_s=f"SELECT * FROM family "

    cur.execute(sql_s)
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect(f'{main_f}gen_tree.db')
    cur=conn.cursor()
    cur.execute("DELETE FROM family WHERE id=?",(id,))
    conn.commit()
    conn.close()
    view()

def update(id,   
          name, 
                                                            surname,                                   
                                                            date_birth,
                                                            date_death,
                                                            mother_id,
                                                            father_id,
                                                            spouse_id,                                   
                                                            generation,
                                                            cluster, 
                                                            gender,
                                                            place_birth,
                                                            country_birth,
                                                            country,
                                                            comments):
    conn=sqlite3.connect(f'{main_f}gen_tree.db')
    cur=conn.cursor()
    date_birth=str(date_birth)
    # date_birth='1982/06/05'
    date_birth=date_birth.replace('/','.')
    # "UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
   
    sql_q=f"""UPDATE family SET  name='{name}', 
                                surname='{surname}',                                   
                                date_birth='{date_birth}',
                                date_death='{date_death}',
                                mother_id=cast({mother_id} as INTEGER),
                                father_id=cast({father_id} as INTEGER),
                                spouse_id=cast({spouse_id} as INTEGER),                                   
                                generation=cast({generation} as INTEGER),
                                cluster=cast({cluster} as INTEGER), 
                                gender=cast({gender} as INTEGER),
                                place_birth='{place_birth}',
                                country_birth='{country_birth}',
                                country='{country}',
                                comments='{comments}'                                
                                WHERE id={id} """
    sql_q=sql_q.replace('=,','=NULL,')
    sql_q=sql_q.replace('=None,','=NULL,')
    sql_q=sql_q.replace('=nan,','=NULL,')
    sql_q=sql_q.replace("='nan',",'=NULL,')
    sql_q=sql_q.replace("='',",'=NULL,')
    sql_q=sql_q.replace("=cast(nan as INTEGER)",'=NULL')
    sql_q=sql_q.replace("=cast( as INTEGER)",'=NULL')
    # print(sql_q )
    cur.execute(sql_q)
    conn.commit()
    conn.close()

def select(id):
    conn=sqlite3.connect(f'{main_f}gen_tree.db')
    cur=conn.cursor()
    cur.execute("Select * FROM family WHERE id=?",(id,))
    rows=cur.fetchall()
    conn.close()
    return rows

