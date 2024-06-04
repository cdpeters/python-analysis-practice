# converts user input km to mi.
km = float(input("How mmany kilometers did you cycle today?\n"))
mi = round(km/1.60934, 1)
print(f"Ok, you said {km}km, that is {mi}mi.")