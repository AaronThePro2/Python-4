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

def nieuwe_lijst():
  leeg_scherm()
  print_header()
  print_regel("U wilt een lijst toevoegen")
  print_footer()
  filenaam = input("Wat is de naam van de file?")
  a = open("Lijsten.data", "a")
  a.write(filenaam + "\n")
  a.close()

  f = open(filenaam + ".wrd", "a")
  f.close()
  main()

def voegwoordtoe():
  leeg_scherm()
  print_header()
  print_regel("U wilt een woord toevoegen")
  print_regel("Schrijf het woord aan elkaar zonder spaties: car=auto")
  print_footer()
  nieuwwoordinput = input("Wat is het woord?")
  content_list.append(nieuwwoordinput)
  f = open(geselecteerdelijst, "a")
  f.write(nieuwwoordinput + "\n")
  f.close()
  main()

def bekijkeenwoordenlijst():
  leeg_scherm()
  print_header()
  print_regel("Je wilt een lijst bekijken, je bekijkt nu de geselecteerde lijst")
  print_footer()
  print("")
  f = open(geselecteerdelijst)

  for line in f:
    woord1, woord2 = line.strip('\n').split('=')
    print(woord1 + " = " + woord2)

  f.close()
  wait = input("Duw op ENTER als je terug wilt")
  main() 

def verwijdereenwoord():
  leeg_scherm()
  print_header()
  print_regel("U wilt een woord verwijderen:")
  print_regel()
  print_regel("Welk woord wilt u verwijderen?")
  print_footer()
  woordkeuze = input("Om welk woord gaat het?")
  content_list.remove(woordkeuze)
  MyFile=open(geselecteerdelijst,'w')

  for element in content_list:
     MyFile.write(element)
     MyFile.write('\n')
  MyFile.close()
  main()

def exitprogram():
  leeg_scherm()
  print_header()
  print_regel("Leuk dat je mijn programma hebt gebruikt!")
  print_footer()
  wait = input("Duw op ENTER als je het programma wilt afsluiten")

def selecteeranderelijst():
    print_header()
    print_regel("Vul de naam van de lijst in om te switchen van lijst")
    print_footer()
    print("De beschikbare lijsten zijn:")
    a = open("Lijsten.data")
    lijsten = a.read().split("\n")
    print(lijsten)
    global geselecteerdelijst
    geselecteerdelijst = input("Welke lijst wil je selecteren? ")
    geselecteerdelijst = geselecteerdelijst + ".wrd"
    global content_list
    content_list = []
    
    
    f = open(geselecteerdelijst)

    for line in f:
      woord1 = line.strip("\n")
      content_list.append(woord1)
      

    f.close()
    
    main()

def overhoor():
    leeg_scherm()
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
            break
        choice = random.choice(content_list)
        woord1, woord2 = choice.split("=")
     


def main():
  leeg_scherm()
  print_header()
  print_regel("Welkom bij het menu van het overhoorprogramma")
  print_regel("Wat wil je doen?")
  print_regel("S -  Een andere lijst selecteren")
  print_regel("O -  Overhoor de geselcteerde lijst")
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
    voegwoordtoe()
  elif answer == "k":
    bekijkeenwoordenlijst()
  elif answer == "q":
    exitprogram()
  elif answer == "v":
    verwijdereenwoord()
  elif answer == "s":
      selecteeranderelijst()
  elif answer == "o":
      overhoor()
  else:
    main()

main()
