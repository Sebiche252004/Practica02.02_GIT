#fecha de nacimiento

fecha= input("Introduzca su fecha de nacimiento en formato dd/mm/aaaa")

division= fecha.split("/")

dia= division[0]
mes=division[1]
año=division[2]

print("Tu fecha de nacimiento es el dia", dia, "del mes",mes,"del año",año)