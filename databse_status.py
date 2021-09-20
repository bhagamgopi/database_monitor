import MySQLdb as mysql

from rich.prompt import Prompt
from rich import style
from rich.console import Console

import time
import json

from rich import style

console = Console()
db = mysql.connect(host='localhost', user='root',
                   password='12345', db="INFORMATION_SCHEMA")
cur = db.cursor()
cur.execute('SHOW STATUS')
res = cur.fetchall()
res2= dict(res)

def db_info():
    console.print(f"Uptime => {res2['Uptime']}", style='bold  italic green')
    console.print(f"Threads_created => {res2['Threads_created']}", style='bold  italic red')
    console.print(f"Threads_connected => {res2['Threads_connected']}", style='bold  italic green')
    console.print(f"Threads_running => {res2['Threads_running']}", style='bold  italic blue')
    console.print(f"Queries => {res2['Queries']}", style='bold  italic red')
    console.print(f"Max_used_connections => {res2['Max_used_connections']}", style='bold  italic green')

def process_list():
	cur.execute("select ID,DB from PROCESSLIST") 
	res = cur.fetchall()
	console.print(f'{res}',style='bold italic green')



def main_menu():
        console.print(f'--------database monitor------',style='bold italic red')
        console.print(f'1.database info',style='bold italic green')
        console.print(f'2.process list',style='bold blue')
        console.print(f'3.Exit',style='bold red')

while True:
	main_menu()
	ch=int(input('Enter your optin:- '))
	if ch == 1:
		db_info()
	elif ch == 2:
		process_list()
	elif ch == 3:
		console.print(f'-------------Exit----------',style='bold italic green')
		break
	else:
		console.print(f'----wrong option------',style='bold italic red')


cur.close()
