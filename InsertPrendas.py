import sqlite3

con = sqlite3.connect("elMojon.db")
cur = con.cursor()
def consulta():
    for n in range(len(cur.execute("SELECT * FROM Talles").fetchall())):
        datos = ("Chomba",n+1)
        consulta = "INSERT INTO Prendas (Prenda,Talle) VALUES (?,?)"
        cur.execute(consulta,datos)
        con.commit()

def idsTalles():
    registros = cur.execute("SELECT id FROM Talles ORDER BY id").fetchall()
    ids = []
    for r in registros:
        ids.append(r[0])
    return ids
def insertPrendas(prenda): 
    for idtalle in idsTalles():
        datos = (prenda,idtalle)
        consulta = "INSERT INTO Prendas (Prenda,Talle) VALUES (?,?)"
        cur.execute(consulta,datos)
        con.commit()

def ver():
    valores = cur.execute("SELECT Prendas.Prenda,Talles.Talle FROM Prendas INNER JOIN Talles ON Prendas.Talle = Talles.id").fetchall()
    print(valores)

def insertBordados(bordado):
    d = (bordado,)
    cons = "INSERT INTO Bordados (Bordado) VALUES (?)"
    cur.execute(cons,d)
    con.commit()
def insertb():
    while True:
        i = input("Bordado?: ")
        if i != "s":
            insertBordados(i)
        else:
            break

def idPrenda(t):
    idTalle = cur.execute("SELECT id FROM Talles WHERE Talle = ?",(t,)).fetchone()[0]
    d = ('Pantalon',idTalle)
    idPrenda = cur.execute("SELECT id FROM Prendas WHERE Prenda = ? AND Talle = ? ",d).fetchone()[0]
    return idPrenda
def insertPrendaDe(nombre,talle,obs):
    idP = idPrenda(talle)
    cur.execute("INSERT INTO Egresados (Bordado,Prenda,Obs) VALUES (?,?,?)",(nombre,idP,obs))
    con.commit()

def nombres():
    registros = cur.execute("SELECT Bordado FROM Bordados ORDER BY id").fetchall()
    nombres = []
    for registro in registros:
        nombres.append(registro[0])
    return nombres
def prendas():
    for nombre in nombres():
        talle = input("talle para {} : ".format(nombre))
        obs = input("Observaciones? :")
        if obs == "":
            obs = "no"
        if talle != "s":
            insertPrendaDe(nombre,talle,obs)
        else:
            break
    



"""
consultas:

ver todos los datos de Egresados 
SELECT Egresados.Bordado,Prendas.Prenda,Talles.Talle,Egresados.Obs FROM Egresados,Prendas,Talles WHERE Egresados.Prenda=Prendas.id AND Prendas.Talle=Talles.id ORDER BY Talles.id;

ver todos los que tengan chombas
SELECT Egresados.Bordado,Prendas.Prenda,Talles.Talle,Egresados.Obs FROM Egresados,Prendas,Talles WHERE Egresados.Prenda=Prendas.id AND Prendas.Talle=Talles.id AND Prendas.Prenda='Chomba' ORDER BY Talles.id;

ver camperas
SELECT Egresados.Bordado,Prendas.Prenda,Talles.Talle,Egresados.Obs FROM Egresados,Prendas,Talles WHERE Egresados.Prenda=Prendas.id AND Prendas.Talle=Talles.id AND Prendas.Prenda='Campera' ORDER BY Talles.id;

ver las prendas de una persona :
SELECT Egresados.Bordado,Prendas.Prenda,Talles.Talle,Egresados.Obs FROM Egresados,Prendas,Talles WHERE Egresados.Prenda=Prendas.id AND Prendas.Talle=Talles.id AND Egresados.Bordado='ALE';

ver cantidad de talles de cada prenda:
SELECT Prendas.Prenda,Talles.Talle,COUNT(Egresados.Prenda) AS Cantidad FROM Egresados,Prendas,Talles WHERE Egresados.Prenda=Prendas.id AND Prendas.Talle=Talles.id GROUP BY Egresados.Prenda;

ver cantidad de talles de una prenda especificada:
SELECT Prendas.Prenda,Talles.Talle,COUNT(Egresados.Prenda) AS Cantidad FROM Egresados,Prendas,Talles WHERE Egresados.Prenda=Prendas.id AND Prendas.Talle=Talles.id AND Prendas.Prenda='Chomba'  GROUP BY Egresados.Prenda;

ver los bordados de una de una prenda especifica
SELECT Egresados.Bordado,Prendas.Prenda,Talles.Talle FROM Egresados,Prendas,Talles WHERE Egresados.Prenda=(SELECT id FROM Prendas WHERE Prenda='Campera' AND Talle=(SELECT id FROM Talles WHERE Talle='L')) AND Egresados.Prenda=Prendas.id AND Prendas.Talle=Talles.id;
ver solo bordados
SELECT Bordado FROM Egresados WHERE Egresados.Prenda=(SELECT id FROM Prendas WHERE Prenda='Campera' AND Talle=(SELECT id FROM Talles WHERE Talle='L')) ORDER BY id;
ver cantidad de una prenda especifica:
SELECT Prendas.Prenda,COUNT(Prendas.Prenda) FROM Egresados,Prendas WHERE Egresados.Prenda=Prendas.id AND Prendas.Prenda='Campera' AND Prendas.Talle!=(SELECT id FROM Talles WHERE Talle='No');

ver cantidad de prenda especifica de un talle especificado
SELECT COUNT(Egresados.Prenda) AS CANTIDAD FROM Egresados WHERE Egresados.Prenda=(SELECT id FROM Prendas WHERE Prenda='Campera' AND Talle=(SELECT id FROM Talles WHERE Talle='S'));






"""
