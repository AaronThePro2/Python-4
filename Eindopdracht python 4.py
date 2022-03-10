from asyncore import write
import os
import random

schermbreedte = 80



def leeg_scherm():
    os.system('cls')

def print_regel(inhoud=''):
  print("| {:<76} |".format(inhoud))
  
def print_header():
  print("="*schermbreedte)
  print("|" + " "*(schermbreedte - 2) + "|")

def print_footer():
  print("|" + " "*(schermbreedte - 2) + "|")
  print("="*schermbreedte)

def geef_bestandnaam(lijst):
  return lijst + ".wrd"

def nieuwe_lijst():
  leeg_scherm()
  print_header()
  print_regel("U wilt een lijst toevoegen")
  print_footer()
  lijst = input("Wat is de naam van de lijst?")
  a = open("Lijsten.data", "a")
  a.write(lijst + "\n")
  a.close()

  schrijflijst(lijst, [])

def selecteeranderelijst():
    print_header()
    print_regel("Vul de naam van de lijst in om te switchen van lijst")
    print_footer()
    print("De beschikbare lijsten zijn:")
    a = open("Lijsten.data")
    lijsten = a.read().split("\n")
    print(lijsten)
    geselecteerdelijst = input("Welke lijst wil je selecteren? ")
    return geselecteerdelijst
    

def voegwoordtoe(lijst):
  leeg_scherm()
  print_header()
  print_regel("U wilt een woord toevoegen")
  print_regel("Schrijf het woord aan elkaar zonder spaties: car=auto")
  print_footer()
  nieuwwoordinput = input("Wat is het woord?")
  bestand = geef_bestandnaam(lijst)
  content_list = laadlijst(lijst)
  content_list.append(nieuwwoordinput)

  schrijflijst(lijst, content_list)
  
def laadlijst(lijst):
  content_list = []
  bestand = lijst + ".wrd"

  f = open(bestand)

  for line in f:
    woord1 = line.strip("\n")
    content_list.append(woord1)

  f.close()
  return content_list

def schrijflijst(lijst, content_list):
  bestand = geef_bestandnaam(lijst)
  f = open(bestand,'w')

  for element in content_list:
     f.write(element)
     f.write('\n')
  f.close()

def bekijkeenwoordenlijst(lijst):
  leeg_scherm()
  print_header()
  print_regel("Je wilt een lijst bekijken, je bekijkt nu de geselecteerde lijst")
  print_footer()
  print("")
  content_list = laadlijst(lijst)

  for line in content_list:
    woord1, woord2 = line.split('=')
    print(woord1 + " = " + woord2)
    
  wait = input("Duw op ENTER als je terug wilt")

def verwijdereenwoord(lijst):
  leeg_scherm()
  print_header()
  print_regel("U wilt een woord verwijderen:")
  print_regel()
  print_regel("Welk woord wilt u verwijderen?")
  print_footer()
  woordkeuze = input("Om welk woord gaat het?")
  content_list = laadlijst(lijst)
  content_list.remove(woordkeuze)
  schrijflijst(lijst, content_list)


def exitprogram():
  leeg_scherm()
  print_header()
  print_regel("Leuk dat je mijn programma hebt gebruikt!")
  print_footer()
  wait = input("Duw op ENTER als je het programma wilt afsluiten")


def overhoor(lijst):
    leeg_scherm()
    content_list = laadlijst(lijst)
    choice = random.choice(content_list)
    woord1, woord2 = choice.split("=")
    print_header()
    print_regel("Welkom bij het woordjes overhoring systeem")
    print_footer()
    while True:
        answer = input("Wat is het woord: " + woord1 + " ")
        if answer == woord2:
            print("Jouw antwoord was goed!")
        else:
            print("Jouw antwoord was fout! Het antwoord was: " + woord2)
        continuemetoverhoren = input("Wil je nog een woord doen? Y/N").lower()
        if continuemetoverhoren == "n":
            main()
        choice = random.choice(content_list)
        woord1, woord2 = choice.split("=")

def menu():
  geselecteerdelijst = ""
  while True:
      leeg_scherm()
      print(geselecteerdelijst)
      print_header()
      print_regel("Welkom bij het menu van het overhoorprogramma")
      print_regel("Wat wil je doen?")
      print_regel("S -  Een andere lijst selecteren")
      print_regel("O -  Overhoor de geselecteerde lijst")
      print_regel("N -  Een nieuwe lijst toevoegen")
      print_regel("K -  Bekijk de geselecteerde woordenlijst")
      print_regel("V -  Verwijder een woord")
      print_regel("T -  Voeg woorden toe aan de geselecteerde woordenlijst")
      print_regel("Q -  Stop het programma")
      print_footer()
      answer = input("Wat wilt u doen?").lower()
      if answer == "n":
        nieuwe_lijst()
      elif answer == "t":
        voegwoordtoe(geselecteerdelijst)
      elif answer == "k":
        bekijkeenwoordenlijst(geselecteerdelijst)
      elif answer == "q":
        exitprogram()
        break
      elif answer == "v":
        verwijdereenwoord(geselecteerdelijst)
      elif answer == "s":
          geselecteerdelijst = selecteeranderelijst()
      elif answer == "o":
          overhoor(geselecteerdelijst)

def main():
    menu()

main()
