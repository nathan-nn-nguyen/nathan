# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    },
    "Debeb": {
        "RA": "20h 41m 25.9s",
        "Dec": "+45° 16′ 49″",
        "Magnitude": 1.25,
        "Spectral Type": "A2la"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
def name_star(targets):
    for target in targets:
        print(target) 

name_star(targets)
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
#print(targets["Betelgeuse"]["Spectral Type"])
def star_name_and_type(targets):
    for target in targets:
        print(target, ": ", targets[target]["Spectral Type"])

print(star_name_and_type(targets))
    

# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
def magnitude_checker(targets):
    for target in targets:
        if targets[target]["Magnitude"] >= 0.1:
            print(target, "has a magnitude greater than 0.1!")

magnitude_checker(targets)
# 4) Look up another target, add all the necessary information to the targets list. 
#I used Deneb

# 5) Write a function that finds the brightest star whose Declination is closest to 20°.

def brightest_star(targets):
    for target in targets:
        if targets[target]["Dec"] >= 10 and targets[target]["Dec"] <= 30:
            print(target, "is the brightest star!")

# 6) What is your favorite constellation?
    #It's the Cygnus Constellation
