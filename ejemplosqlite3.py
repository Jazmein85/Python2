from os import curdir
import sqlite3
import click
from click.termui import prompt

def crear_tabla(con, cursor):
    try:
        cursor.execute('CREATE TABLE employees(id integer PRIMARY KEY, nombre TEXT, apellido TEXT, salario REAL)')
        con.commit()
    except:
        print('La tabla fue creada')
@click.command()
@click.option('--id', prompt="Inserte ID del empleado")
@click.option('--nombre', prompt="Inserte nombre del empleado")
@click.option('--apellido', prompt="Inserte apellido del empleado")
@click.option('--salario', prompt="Inserte salario $$ del empleado", type=float)

def insertar_empleado(id, nombre, apellido, salario):
    try:
        cursor.execute('INSERT INTO employees(id, nombre, apellido, salario) VALUES (?, ?, ?, ?)', [id, nombre, apellido, salario])
        con.commit()
        print(f'Empleado{nombre} agregado')
    except Exception as e:
        print('No se pudo insertar el usuario. Razón {e}')
    
if __name__=='__main__':
    con = sqlite3.connect('Base_de_datos.db')
    cursor = con.cursor()

    crear_tabla(con, cursor)
    insertar_empleado()

    con.close()
