import os
import re
import sys
import time
import numpy
import poetry
import replit
import random
import urllib3
import requests
import urllib.request

from art import flag
from art import space
from art import combadge
from art import hologram
from art import starship1
from art import starship2
from art import starship3
from art import starship4
from art import starship5
from art import starship6
from art import starship7
from art import starship8
from art import title_spaceships

from lxml import html
from termcolor import *
from PIL import ImageChops
from bs4 import BeautifulSoup
from pyscreenshot import grab
from Complex_Number_Encryptor.ComplexNumber import Encoder

global starship_type
global attack_power
global defense_power
global rate_of_fire_power
global speed_of_ship_power
global weapon_accuracy_power
global secondary_weapon
global emergency_ship_weapon
global shipName
global shipPassword

starship_type = None

attack_power = 0
defense_power = 0
rate_of_fire_power = 0
speed_of_ship_power = 0
weapon_accuracy_power = 0

secondary_weapon = None
emergency_ship_weapon = "Scrapper's Docking Hook"

shipName = ''
shipPassword = ''

Encryption_factors = [(1+1j), (2+2j), (3+3j)]

turn = 1
turn_taker = ''
turn_option = ['You', 'Enemy Ship']
ship_types = ['Assualt Starship', 'Close Range Transport', 'Far Range Recon Craft', 'SpeedCraft Ace StarFighter', 'Double Cannoned StarFighter', 'Scout Craft', 'Bomber Craft', 'Scrapper Ship', 'Commando Personal Starfighter', 'DreadNaught', 'Long Range Warp Cannon Transport']
weapon_accuracy = ['hit', 'miss', 'miss', 'miss']
random_shot_list = ['hit', 'miss', 'miss', 'miss', 'miss', 'miss', 'miss', 'miss', 'miss']

enemy_health = 100
dailyVictories = 0
totalVictories = 0
blanket_subvictories = ''

faction_name = ''

list_of_ships = []
ship_name_fight = ''

dog_fight_ship_health = 100
dog_fight_ship_enemy_health = 100

def title_screen():
  os.system('clear')
  cprint('[+Star Crap == Star Ship+]                         ', 'white', 'on_blue')
  print(title_spaceships)
  cprint('{[SELECT] An Option...                            }', 'red', 'on_grey')
  cprint('[1: Create Starship                               ]', 'white', 'on_grey')
  cprint('[2: Pilot(Sign In) to Starship                    ]', 'white', 'on_grey')
  cprint('Type Option Number Here: ', 'white', 'on_red', end='')

  c = input('')

  if c == '1':
    create_starship()
  elif c == '2':
    sign_in()
  else:
    os.system('clear')
    title_screen()

def create_starship():
  global starship_type
  global attack_power
  global defense_power
  global rate_of_fire_power
  global speed_of_ship_power
  global weapon_accuracy_power
  global secondary_weapon
  global emergency_ship_weapon
  global shipName
  global shipPassword

  os.system('clear')
  cprint('[Create A StarShip                                ]', 'white', 'on_blue')
  print(starship2)
  cprint('{[SELECT] An Option...                            }', 'red', 'on_grey')
  cprint('[1: Build Assault Starship                        ]', 'white', 'on_grey')
  cprint('[2: Build Close Range Transport                   ]', 'white', 'on_grey')
  cprint('[3: Build Far Range Recon Craft                   ]', 'white', 'on_grey')
  cprint('[4: Build SpeedCraft Ace StarFighter              ]', 'white', 'on_grey')
  cprint('[5: Build Double Cannoned StarFighter             ]', 'white', 'on_grey')
  cprint('[6: Build Scout Craft                             ]', 'white', 'on_grey')
  cprint('[7: Build Bomber Craft                            ]', 'white', 'on_grey')
  cprint('[8: Build Scrapper Ship                           ]', 'white', 'on_grey')
  cprint('[9: Build Commando Personal Starfighter           ]', 'white', 'on_grey')
  cprint('[10: Build DreadNaught                            ]', 'white', 'on_grey')
  cprint('[11: Build Long Range Warp Cannon Transport       ]', 'white', 'on_grey')
  cprint('{12: [EXIT]}', 'red', 'on_grey')
  cprint('Type Option Number: ', 'blue', 'on_white', end='')
  
  c = input('')

  if c == '1':
    starship_type = 'Assault Starship'
    attack_power = 30
    defense_power = 100
    rate_of_fire_power = 30
    speed_of_ship_power = 60
    
    secondary_weapon = 'Disruptor'
    emergency_ship_weapon = "Scrapper's Docking Hook"

    os.system('clear')
    cprint('[Building Starship....                          ]', 'white', 'on_blue')
    print(starship3)
    cprint('Starship Stats....', 'red', 'on_grey')
    cprint('Starship Type: '+str(starship_type), 'white', 'on_grey')
    cprint('Attack Power: '+str(attack_power), 'white', 'on_grey')
    cprint('Defense Power: '+str(defense_power), 'white', 'on_grey')
    cprint('Rate Of Fire Power'+str(rate_of_fire_power), 'white', 'on_grey')
    cprint('Speed of Ship: '+str(speed_of_ship_power), 'white', 'on_grey')
    print()
    cprint('Secondary Weapon: '+str(secondary_weapon), 'white', 'on_grey')
    cprint('Emergency Ship Weapon: '+str(emergency_ship_weapon), 'white', 'on_grey')
    verifyStarship()

  elif c == '2':
    starship_type = 'Close Range Transport'
    attack_power = 80
    defense_power = 100
    rate_of_fire_power = 2
    speed_of_ship_power = 80

    secondary_weapon = 'Disruptor'
    emergency_ship_weapon = "Scrapper's Docking Hook"

    os.system('clear')
    cprint('[Building Starship....                          ]', 'white', 'on_blue')
    print(starship3)
    cprint('Starship Stats....', 'red', 'on_grey')
    cprint('Starship Type: '+str(starship_type), 'white', 'on_grey')
    cprint('Attack Power: '+str(attack_power), 'white', 'on_grey')
    cprint('Defense Power: '+str(defense_power), 'white', 'on_grey')
    cprint('Rate Of Fire Power'+str(rate_of_fire_power), 'white', 'on_grey')
    cprint('Speed of Ship: '+str(speed_of_ship_power), 'white', 'on_grey')
    print()
    cprint('Secondary Weapon: '+str(secondary_weapon), 'white', 'on_grey')
    cprint('Emergency Ship Weapon: '+str(emergency_ship_weapon), 'white', 'on_grey')
    verifyStarship()

  elif c == '3':
    starship_type = 'Far Range Recon Craft'
    attack_power = 80
    defense_power = 60
    rate_of_fire_power = 3
    speed_of_ship_power = 40

    secondary_weapon = 'Disruptor'
    emergency_ship_weapon = "Scrapper's Docking Hook"

    os.system('clear')
    cprint('[Building Starship....                          ]', 'white', 'on_blue')
    print(starship3)
    cprint('Starship Stats....', 'red', 'on_grey')
    cprint('Starship Type: '+str(starship_type), 'white', 'on_grey')
    cprint('Attack Power: '+str(attack_power), 'white', 'on_grey')
    cprint('Defense Power: '+str(defense_power), 'white', 'on_grey')
    cprint('Rate Of Fire Power'+str(rate_of_fire_power), 'white', 'on_grey')
    cprint('Speed of Ship: '+str(speed_of_ship_power), 'white', 'on_grey')
    print()
    cprint('Secondary Weapon: '+str(secondary_weapon), 'white', 'on_grey')
    cprint('Emergency Ship Weapon: '+str(emergency_ship_weapon), 'white', 'on_grey')
    verifyStarship()

  elif c == '4':
    starship_type = 'SpeedCraft Ace StarFighter'
    attack_power = 10
    defense_power = 100
    rate_of_fire_power = 25
    speed_of_ship_power = 80

    secondary_weapon = None
    emergency_ship_weapon = "Scrapper's Docking Hook"

    os.system('clear')
    cprint('[Building Starship....                          ]', 'white', 'on_blue')
    print(starship3)
    cprint('Starship Stats....', 'red', 'on_grey')
    cprint('Starship Type: '+str(starship_type), 'white', 'on_grey')
    cprint('Attack Power: '+str(attack_power), 'white', 'on_grey')
    cprint('Defense Power: '+str(defense_power), 'white', 'on_grey')
    cprint('Rate Of Fire Power'+str(rate_of_fire_power), 'white', 'on_grey')
    cprint('Speed of Ship: '+str(speed_of_ship_power), 'white', 'on_grey')
    print()
    cprint('Secondary Weapon: '+str(secondary_weapon), 'white', 'on_grey')
    cprint('Emergency Ship Weapon: '+str(emergency_ship_weapon), 'white', 'on_grey')
    verifyStarship()

  elif c == '5':
    starship_type = 'Double Cannoned StarFighter'
    attack_power = 10
    defense_power = 100
    rate_of_fire_power = 18
    speed_of_ship_power = 80

    secondary_weapon = 'Disruptor'
    emergency_ship_weapon = "Scrapper's Docking Hook"

    os.system('clear')
    cprint('[Building Starship....                          ]', 'white', 'on_blue')
    print(starship3)
    cprint('Starship Stats....', 'red', 'on_grey')
    cprint('Starship Type: '+str(starship_type), 'white', 'on_grey')
    cprint('Attack Power: '+str(attack_power), 'white', 'on_grey')
    cprint('Defense Power: '+str(defense_power), 'white', 'on_grey')
    cprint('Rate Of Fire Power'+str(rate_of_fire_power), 'white', 'on_grey')
    cprint('Speed of Ship: '+str(speed_of_ship_power), 'white', 'on_grey')
    print()
    cprint('Secondary Weapon: '+str(secondary_weapon), 'white', 'on_grey')
    cprint('Emergency Ship Weapon: '+str(emergency_ship_weapon), 'white', 'on_grey')
    verifyStarship()

  elif c == '6':
    starship_type = 'Scout Craft'
    attack_power = 60
    defense_power = 100
    rate_of_fire_power = 6
    speed_of_ship_power = 80

    secondary_weapon = None
    emergency_ship_weapon = "Scrapper's Docking Hook"

    os.system('clear')
    cprint('[Building Starship....                          ]', 'white', 'on_blue')
    print(starship3)
    cprint('Starship Stats....', 'red', 'on_grey')
    cprint('Starship Type: '+str(starship_type), 'white', 'on_grey')
    cprint('Attack Power: '+str(attack_power), 'white', 'on_grey')
    cprint('Defense Power: '+str(defense_power), 'white', 'on_grey')
    cprint('Rate Of Fire Power'+str(rate_of_fire_power), 'white', 'on_grey')
    cprint('Speed of Ship: '+str(speed_of_ship_power), 'white', 'on_grey')
    print()
    cprint('Secondary Weapon: '+str(secondary_weapon), 'white', 'on_grey')
    cprint('Emergency Ship Weapon: '+str(emergency_ship_weapon), 'white', 'on_grey')
    verifyStarship()

  elif c == '7':
    starship_type = 'Bomber Craft'
    attack_power = 100
    defense_power = 130
    rate_of_fire_power = 2
    speed_of_ship_power = 40

    secondary_weapon = 'Disruptor'
    emergency_ship_weapon = "Scrapper's Docking Hook"

    os.system('clear')
    cprint('[Building Starship....                          ]', 'white', 'on_blue')
    print(starship3)
    cprint('Starship Stats....', 'red', 'on_grey')
    cprint('Starship Type: '+str(starship_type), 'white', 'on_grey')
    cprint('Attack Power: '+str(attack_power), 'white', 'on_grey')
    cprint('Defense Power: '+str(defense_power), 'white', 'on_grey')
    cprint('Rate Of Fire Power'+str(rate_of_fire_power), 'white', 'on_grey')
    cprint('Speed of Ship: '+str(speed_of_ship_power), 'white', 'on_grey')
    print()
    cprint('Secondary Weapon: '+str(secondary_weapon), 'white', 'on_grey')
    cprint('Emergency Ship Weapon: '+str(emergency_ship_weapon), 'white', 'on_grey')
    verifyStarship()

  elif c == '8':
    starship_type = 'Scrapper Ship'
    attack_power = 80
    defense_power = 100
    rate_of_fire_power = 100000
    speed_of_ship_power = 80

    secondary_weapon = 'Disruptor'
    emergency_ship_weapon = "Scrapper's Docking Hook"

    os.system('clear')
    cprint('[Building Starship....                          ]', 'white', 'on_blue')
    print(starship3)
    cprint('Starship Stats....', 'red', 'on_grey')
    cprint('Starship Type: '+str(starship_type), 'white', 'on_grey')
    cprint('Attack Power: '+str(attack_power), 'white', 'on_grey')
    cprint('Defense Power: '+str(defense_power), 'white', 'on_grey')
    cprint('Rate Of Fire Power'+str(rate_of_fire_power), 'white', 'on_grey')
    cprint('Speed of Ship: '+str(speed_of_ship_power), 'white', 'on_grey')
    print()
    cprint('Secondary Weapon: '+str(secondary_weapon), 'white', 'on_grey')
    cprint('Emergency Ship Weapon: '+str(emergency_ship_weapon), 'white', 'on_grey')
    verifyStarship()

  elif c == '9':
    starship_type = 'Commando Personal Starfighter'
    attack_power = 40
    defense_power = 100
    rate_of_fire_power = 24
    speed_of_ship_power = 60
    
    secondary_weapon = 'Disruptor'
    emergency_ship_weapon = "Scrapper's Docking Hook"

    os.system('clear')
    cprint('[Building Starship....                          ]', 'white', 'on_blue')
    print(starship3)
    cprint('Starship Stats....', 'red', 'on_grey')
    cprint('Starship Type: '+str(starship_type), 'white', 'on_grey')
    cprint('Attack Power: '+str(attack_power), 'white', 'on_grey')
    cprint('Defense Power: '+str(defense_power), 'white', 'on_grey')
    cprint('Rate Of Fire Power'+str(rate_of_fire_power), 'white', 'on_grey')
    cprint('Speed of Ship: '+str(speed_of_ship_power), 'white', 'on_grey')
    print()
    cprint('Secondary Weapon: '+str(secondary_weapon), 'white', 'on_grey')
    cprint('Emergency Ship Weapon: '+str(emergency_ship_weapon), 'white', 'on_grey')
    verifyStarship()

  elif c == '10':
    starship_type = 'DreadNaught'
    attack_power = 20
    defense_power = 100
    rate_of_fire_power = 60
    speed_of_ship_power = 40

    secondary_weapon = 'Disruptor'
    emergency_ship_weapon = "Scrapper's Docking Hook"

    os.system('clear')
    cprint('[Building Starship....                          ]', 'white', 'on_blue')
    print(starship3)
    cprint('Starship Stats....', 'red', 'on_grey')
    cprint('Starship Type: '+str(starship_type), 'white', 'on_grey')
    cprint('Attack Power: '+str(attack_power), 'white', 'on_grey')
    cprint('Defense Power: '+str(defense_power), 'white', 'on_grey')
    cprint('Rate Of Fire Power'+str(rate_of_fire_power), 'white', 'on_grey')
    cprint('Speed of Ship: '+str(speed_of_ship_power), 'white', 'on_grey')
    print()
    cprint('Secondary Weapon: '+str(secondary_weapon), 'white', 'on_grey')
    cprint('Emergency Ship Weapon: '+str(emergency_ship_weapon), 'white', 'on_grey')
    verifyStarship()

  elif c == '11':
    starship_type = 'Long Range Warp Cannon Transport'
    attack_power = 100
    defense_power = 100
    rate_of_fire_power = 1
    speed_of_ship_power = 40

    secondary_weapon = 'Disruptor'
    emergency_ship_weapon = "Scrapper's Docking Hook"

    os.system('clear')
    cprint('[Building Starship....                          ]', 'white', 'on_blue')
    print(starship3)
    cprint('Starship Stats....', 'red', 'on_grey')
    cprint('Starship Type: '+str(starship_type), 'white', 'on_grey')
    cprint('Attack Power: '+str(attack_power), 'white', 'on_grey')
    cprint('Defense Power: '+str(defense_power), 'white', 'on_grey')
    cprint('Rate Of Fire Power'+str(rate_of_fire_power), 'white', 'on_grey')
    cprint('Speed of Ship: '+str(speed_of_ship_power), 'white', 'on_grey')
    print()
    cprint('Secondary Weapon: '+str(secondary_weapon), 'white', 'on_grey')
    cprint('Emergency Ship Weapon: '+str(emergency_ship_weapon), 'white', 'on_grey')
    verifyStarship()
  elif c == '12':
    os.system('clear')
    title_screen()
  else:
    create_starship()

def submit_starship():
  os.system('clear')
  cprint('[Building Starship....                          ]', 'white', 'on_blue')
  print(starship3)
  cprint('Starship Stats....', 'red', 'on_grey')
  cprint('Starship Type: '+str(starship_type), 'white', 'on_grey')
  cprint('Attack Power: '+str(attack_power), 'white', 'on_grey')
  cprint('Defense Power: '+str(defense_power), 'white', 'on_grey')
  cprint('Rate Of Fire Power'+str(rate_of_fire_power), 'white', 'on_grey')
  cprint('Speed of Ship: '+str(speed_of_ship_power), 'white', 'on_grey')
  print()
  cprint('Secondary Weapon: '+str(secondary_weapon), 'white', 'on_grey')
  cprint('Emergency Ship Weapon: '+str(emergency_ship_weapon), 'white', 'on_grey')
  verifyStarship()

def verifyStarship():
  global shipName
  global shipPassword
  global starship_type

  cprint('Are you ready to make these changes?(Y/N): ', 'white', 'on_red', end='')
  c = input('')

  if c == 'Y' or c == 'y':
   cprint('Name your ship: ', 'white', 'on_red', end='')
   name = input('')

   shipName = name

   cprint('Ship Password: ', 'white', 'on_red', end='')
   ship_password = input('')

   shipPassword = ship_password

   Encoded_Name = Encoder(shipName, Encryption_factors, d=1).enc()
   Encoded_Password = Encoder(shipPassword, Encryption_factors, d=1).enc()

   request = requests.get('https://starshipdatabase--codesalvageon.repl.co/accounts/'+str(shipName)+'/verified.html')
   if request.status_code == 200:
     cprint('Starship already exists! Choose a new name.', 'red', 'on_white')
     cprint('Press ENTER to continue.', 'red', 'on_white', end='')
     c = input('')
     create_starship()
   else:
     cprint('Creating Starship...', 'blue', 'on_white')
     os.system('curl --data "name='+str(shipName)+'&password='+str(int.from_bytes(str(Encoded_Password).encode('utf-8'), byteorder='big'))+'&type='+starship_type+'" https://starshipdatabase.codesalvageon.repl.co/create_ship.php')
     logged_in()

  else:
    create_starship()

def sign_in():
  global shipName
  global shipPassword
  global starship_type
  global attack_power
  global defense_power
  global rate_of_fire_power
  global speed_of_ship_power
  global weapon_accuracy_power
  global secondary_weapon
  global emergency_ship_weapon
  global blanket_subvictories

  os.system('clear')
  cprint('Pilot Star Ship                                   ', 'white', 'on_blue')
  print(starship5)
  cprint('Login                                             ', 'white', 'on_red')
  cprint('Starship Name:', 'blue', 'on_grey', end='')
  name = input('')

  shipName = name

  cprint('Password:', 'blue', 'on_grey', end='')
  password = input('')
  shipPassword = password

  Encoded_Name = Encoder(shipName, Encryption_factors, d=1).enc()
  Encoded_Password = Encoder(shipPassword, Encryption_factors, d=1).enc()

  request = requests.get('https://starshipdatabase--codesalvageon.repl.co/accounts/'+str(shipName)+'/verified.html')
  if request.status_code == 200:
     page = requests.get('https://starshipdatabase--codesalvageon.repl.co/accounts/'+str(shipName)+'/verified.html')
     tree = html.fromstring(page.content)
     pwd = tree.xpath('//div[@class="pwd"]/text()')
     blanket_pwd = "['"+str(int.from_bytes(str(Encoded_Password).encode('utf-8'), byteorder='big'))+"']"

     if str(blanket_pwd) == str(pwd):
       cprint('Login Succesful!', 'blue', 'on_white')
       os.system('clear')
       account = requests.get('https://starshipdatabase--codesalvageon.repl.co/accounts/'+str(shipName)+'/verified.html')
       account_tree = html.fromstring(account.content)
       blanket_subtype = tree.xpath('//div[@class="type"]/text()')
       blanket_subvictories = tree.xpath('//div[@class="victories"]/text()')
       if str(blanket_subtype) == "['Assault Starship']":
         starship_type = 'Assault Starship'
         attack_power = 30
         defense_power = 100
         rate_of_fire_power = 30
         speed_of_ship_power = 60
    
         secondary_weapon = 'Disruptor'
         emergency_ship_weapon = "Scrapper's Docking Hook"
       elif str(blanket_subtype) == "['Close Range Transport']":
         starship_type = 'Close Range Transport'
         attack_power = 80
         defense_power = 100
         rate_of_fire_power = 2
         speed_of_ship_power = 80

         secondary_weapon = 'Disruptor'
         emergency_ship_weapon = "Scrapper's Docking Hook"
       elif str(blanket_subtype) == "['Far Range Recon Craft']":
         starship_type = 'Far Range Recon Craft'
         attack_power = 80
         defense_power = 60
         rate_of_fire_power = 3
         speed_of_ship_power = 40

         secondary_weapon = 'Disruptor'
         emergency_ship_weapon = "Scrapper's Docking Hook"
       elif str(blanket_subtype) == "['SpeedCraft Ace StarFighter']":
         starship_type = 'SpeedCraft Ace StarFighter'
         attack_power = 10
         defense_power = 100
         rate_of_fire_power = 25
         speed_of_ship_power = 80

         secondary_weapon = None
         emergency_ship_weapon = "Scrapper's Docking Hook"
       elif str(blanket_subtype) == "['Double Cannoned StarFighter']":
         starship_type = 'Double Cannoned StarFighter'
         attack_power = 10
         defense_power = 100
         rate_of_fire_power = 18
         speed_of_ship_power = 80

         secondary_weapon = 'Disruptor'
         emergency_ship_weapon = "Scrapper's Docking Hook"
       elif str(blanket_subtype) == "['Scout Craft']":
         starship_type = 'Scout Craft'
         attack_power = 60
         defense_power = 100
         rate_of_fire_power = 6
         speed_of_ship_power = 80

         secondary_weapon = None
         emergency_ship_weapon = "Scrapper's Docking Hook"
       elif str(blanket_subtype) == "['Bomber Craft']":
         starship_type = 'Bomber Craft'
         attack_power = 100
         defense_power = 130
         rate_of_fire_power = 2
         speed_of_ship_power = 40

         secondary_weapon = 'Disruptor'
         emergency_ship_weapon = "Scrapper's Docking Hook"
       elif str(blanket_subtype) == "['Scrapper Ship']":
         starship_type = 'Scrapper Ship'
         attack_power = 80
         defense_power = 100
         rate_of_fire_power = 100000
         speed_of_ship_power = 80

         secondary_weapon = 'Disruptor'
         emergency_ship_weapon = "Scrapper's Docking Hook"
       elif str(blanket_subtype) == "['Commando Personal Starfighter']":
         starship_type = "Commando Personal Starfighter"
         attack_power = 40
         defense_power = 100
         rate_of_fire_power = 24
         speed_of_ship_power = 60
    
         secondary_weapon = 'Disruptor'
         emergency_ship_weapon = "Scrapper's Docking Hook"
       elif str(blanket_subtype) == "['DreadNaught']":
         starship_type = 'DreadNaught'
         attack_power = 20
         defense_power = 100
         rate_of_fire_power = 60
         speed_of_ship_power = 40

         secondary_weapon = 'Disruptor'
         emergency_ship_weapon = "Scrapper's Docking Hook"
       elif str(blanket_subtype) == "['Long Range Warp Cannon Transport']":
         starship_type = 'Long Range Warp Cannon Transport'
         attack_power = 100
         defense_power = 100
         rate_of_fire_power = 1
         speed_of_ship_power = 40

         secondary_weapon = 'Disruptor'
         emergency_ship_weapon = "Scrapper's Docking Hook"
       else:
         cprint('Error')
         pass
         exit()
       logged_in()
     else:
       cprint('Login Failed. Check starship name and password.', 'red', 'on_white')
       cprint('Press ENTER to continue. ', 'red', 'on_white', end='')
       c = input('')
       os.system('clear')
       sign_in()

  else:
     cprint('Starship Does not Exist!', 'red', 'on_white')
     cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
     c = input('')
     os.system('clear')
     create_starship()

def logged_in():
  os.system('clear')
  cprint('Commanding the USS '+str(shipName)+'.', 'white', 'on_blue')
  print(space)
  cprint('Commanding Officer Options:', 'blue', 'on_white')
  cprint('1: View combat operations', 'red', 'on_grey')
  cprint('2: View Faction Operations', 'red', 'on_grey')
  cprint('3: View communications', 'red', 'on_grey')
  cprint('Type Option Number: ', 'red', 'on_white', end='')
  c = input('')
  if c == '1':
    os.system('clear')
    combat_ops()
  elif c == '2':
    os.system('clear')
    faction_ops()
  elif c == '3':
    os.system('clear')
    com_ops()
  elif c == '4':
    os.system('clear')
    logged_in()
  else:
    os.system('clear')
    logged_in()

def combat_ops():
  global enemy_health
  global defense_power

  enemy_health = 100
  defense_power = 100
  os.system('clear')
  cprint('Viewing Combat Operations                       ', 'white', 'on_blue')
  print(starship6)
  cprint('Combat Options: ', 'red', 'on_white')
  cprint("1: Practice against the holodeck's computer", 'red', 'on_grey')
  cprint("2: Fight random ship                       ", 'red', 'on_grey')
  cprint('3: Exit', 'red', 'on_white')
  cprint('Type option number: ', 'red', 'on_white', end='')
  c = input('')

  if c == '1':
    os.system('clear')
    holodeck_computer()
  elif c == '2':
    os.system('clear')
    fight_random()
  elif c == '3':
    os.system('clear')
    logged_in()
  else:
    os.system('clear')
    combat_ops()

def holodeck_computer():
  global turn
  global turn_taker
  global ship_types
  global turn_option
  global weapon_accuracy
  global enemy_health
  global attack_power

  ship_tack = attack_power
  computer_health = enemy_health

  os.system('clear')

  if turn == 1:
    is_you = random.choice(turn_option)
    holodeck_ship_type = random.choice(ship_types)

    if is_you == 'You':
      turn_taker = 'ship'
      os.system('clear')
      holodeck_computer_turn()
    else:
      computer_turn()
  else:
    print('error')
    exit()

def holodeck_computer_turn():
  global turn
  global turn_taker
  global ship_types
  global turn_option
  global enemy_health
  global attack_power
  global dailyVictories

  os.system('clear')
  cprint('Turn goes to the USS '+str(shipName)+'!', 'red', 'on_grey')
  print(starship7)
  if starship_type == 'Assault Starship':
    cprint('1: Rapid Phaser (30 dmg per hit)', 'red', 'on_grey')
    cprint('2: Disruptor (10 dmg per hit)', 'red', 'on_grey')
    cprint("3: Scrapper's Docking Hook   ", 'red', 'on_grey')
    cprint('Type weapon option number: ', 'red', 'on_white', end='')
    c = input('')

    if c == '1':
      cprint('Firing Phasers!', 'red', 'on_blue')
      lol = random.choice(weapon_accuracy)
      
      if lol == 'hit':
        enemy_health = enemy_health - attack_power
        if enemy_health < 1:
          cprint('Enemy Ship Defeated!', 'blue', 'on_white')
          cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
          c = input('')
          dailyVictories = dailyVictories + 1
          os.system('clear')
          combat_ops()
        else:
          cprint('Enemy ship damaged!', 'blue', 'on_white')
          cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
          c = input('')
          os.system('clear')
          computer_turn()
      else:
          cprint('Miss!', 'red', 'on_white')
          cprint('Press ENTER to continue. ', 'red', 'on_white', end='')
          c = input('')
          os.system('clear')
          computer_turn()
    elif c == '2':
      cprint('Firing Disruptors!', 'red', 'on_blue')
      lol = random.choice(weapon_accuracy)

      if lol == 'hit':
        enemy_health = enemy_health - 10

        if enemy_health < 1:
          cprint('Enemy ship defeated!', 'blue', 'on_white')
          cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
          c = input('')
          dailyVictories = dailyVictories + 1
          os.system('clear')
          combat_ops()
        else:
          cprint('Enemy ship damaged', 'blue', 'on_white')
          cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
          c = input('')
          os.system('clear')
          computer_turn()
      else:
        cprint('Miss!', 'red', 'on_white')
        cprint('Press ENTER to continue. ', 'red', 'on_white', end='')
        c = input('')
        os.system('clear')
        computer_turn()
    else:
      cprint('Taking random shot...', 'white', 'on_red')
      lol = random.randint(0, 80)
      enemy_health = enemy_health - lol
      if enemy_health < 1:
        cprint('Enemy Ship defeated!', 'blue', 'on_white')
        cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
        c = input('')
        dailyVictories = dailyVictories + 1
        os.system('clear')
        combat_ops()
      else:
        cprint('Enemy ship intact!', 'red', 'on_white')
        cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
        c = input('')
        os.system('clear')
        computer_turn()

  elif starship_type == 'Close Range Transport':
    cprint('1: Close Range Plasma Bursts (80 dmg per hit)', 'red', 'on_grey')
    cprint('2: Disruptor (10 dmg per hit)', 'red', 'on_grey')
    cprint("3: Scrapper's Docking Hook   ", 'red', 'on_grey')
    cprint('Type weapon option number: ', 'red', 'on_white', end='')
    c = input('')

    if c == '1':
      cprint('Firing Phasers!', 'red', 'on_blue')
      lol = random.choice(weapon_accuracy)
      
      if lol == 'hit':
        enemy_health = enemy_health - attack_power
        if enemy_health < 1:
          cprint('Enemy Ship Defeated!', 'blue', 'on_white')
          cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
          c = input('')
          dailyVictories = dailyVictories + 1
          os.system('clear')
          combat_ops()
        else:
          cprint('Enemy ship damaged!', 'blue', 'on_white')
          cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
          c = input('')
          os.system('clear')
          computer_turn()
      else:
          cprint('Miss!', 'red', 'on_white')
          cprint('Press ENTER to continue. ', 'red', 'on_white', end='')
          c = input('')
          os.system('clear')
          computer_turn()
    elif c == '2':
      cprint('Firing Disruptors!', 'red', 'on_blue')
      lol = random.choice(weapon_accuracy)

      if lol == 'hit':
        enemy_health = enemy_health - 10

        if enemy_health < 1:
          cprint('Enemy ship defeated!', 'blue', 'on_white')
          cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
          c = input('')
          dailyVictories = dailyVictories + 1
          os.system('clear')
          combat_ops()
        else:
          cprint('Enemy ship damaged', 'blue', 'on_white')
          cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
          c = input('')
          os.system('clear')
          computer_turn()
      else:
        cprint('Miss!', 'red', 'on_white')
        cprint('Press ENTER to continue. ', 'red', 'on_white', end='')
        c = input('')
        os.system('clear')
        computer_turn()
    else:
      cprint('Taking random shot...', 'white', 'on_red')
      lol = random.randint(0, 80)
      enemy_health = enemy_health - lol
      if enemy_health < 1:
        cprint('Enemy Ship defeated!', 'blue', 'on_white')
        cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
        c = input('')
        dailyVictories = dailyVictories + 1
        os.system('clear')
        combat_ops()
      else:
        cprint('Enemy ship intact!', 'red', 'on_white')
        cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
        c = input('')
        os.system('clear')
        computer_turn()

  elif starship_type == 'Far Range Recon Craft':
    cprint('1: Shield Piercing Phaser (80 dmg per hit)', 'red', 'on_grey')
    cprint('2: Disruptor (10 dmg per hit)', 'red', 'on_grey')
    cprint("3: Scrapper's Docking Hook   ", 'red', 'on_grey')
    cprint('Type weapon option number: ', 'red', 'on_white', end='')
    c = input('')

    if c == '1':
      cprint('Firing Phasers!', 'red', 'on_blue')
      lol = random.choice(weapon_accuracy)
      
      if lol == 'hit':
        enemy_health = enemy_health - attack_power
        if enemy_health < 1:
          cprint('Enemy Ship Defeated!', 'blue', 'on_white')
          cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
          c = input('')
          dailyVictories = dailyVictories + 1
          os.system('clear')
          combat_ops()
        else:
          cprint('Enemy ship damaged!', 'blue', 'on_white')
          cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
          c = input('')
          os.system('clear')
          computer_turn()
      else:
          cprint('Miss!', 'red', 'on_white')
          cprint('Press ENTER to continue. ', 'red', 'on_white', end='')
          c = input('')
          os.system('clear')
          computer_turn()
    elif c == '2':
      cprint('Firing Disruptors!', 'red', 'on_blue')
      lol = random.choice(weapon_accuracy)

      if lol == 'hit':
        enemy_health = enemy_health - 10

        if enemy_health < 1:
          cprint('Enemy ship defeated!', 'blue', 'on_white')
          cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
          c = input('')
          dailyVictories = dailyVictories + 1
          os.system('clear')
          combat_ops()
        else:
          cprint('Enemy ship damaged', 'blue', 'on_white')
          cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
          c = input('')
          os.system('clear')
          computer_turn()
      else:
        cprint('Miss!', 'red', 'on_white')
        cprint('Press ENTER to continue. ', 'red', 'on_white', end='')
        c = input('')
        os.system('clear')
        computer_turn()
    else:
      cprint('Taking random shot...', 'white', 'on_red')
      lol = random.randint(0, 80)
      enemy_health = enemy_health - lol
      if enemy_health < 1:
        cprint('Enemy Ship defeated!', 'blue', 'on_white')
        cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
        c = input('')
        dailyVictories = dailyVictories + 1
        os.system('clear')
        combat_ops()
      else:
        cprint('Enemy ship intact!', 'red', 'on_white')
        cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
        c = input('')
        os.system('clear')
        computer_turn()
  elif starship_type == 'SpeedCraft Ace StarFighter':
    cprint('1: Pulsed Disruptor (10 dmg per hit)', 'red', 'on_grey')
    cprint('2: Disruptor (10 dmg per hit)       ', 'red', 'on_grey')
    cprint("3: Scrapper's Docking Hook          ", 'red', 'on_grey')
    cprint('Type weapon option number: ', 'red', 'on_white', end='')
    c = input('')

    if c == '1':
      cprint('Firing Phasers!', 'red', 'on_blue')
      lol = random.choice(weapon_accuracy)
      
      if lol == 'hit':
        enemy_health = enemy_health - attack_power
        if enemy_health < 1:
          cprint('Enemy Ship Defeated!', 'blue', 'on_white')
          cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
          c = input('')
          dailyVictories = dailyVictories + 1
          os.system('clear')
          combat_ops()
        else:
          cprint('Enemy ship damaged!', 'blue', 'on_white')
          cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
          c = input('')
          os.system('clear')
          computer_turn()
      else:
          cprint('Miss!', 'red', 'on_white')
          cprint('Press ENTER to continue. ', 'red', 'on_white', end='')
          c = input('')
          os.system('clear')
          computer_turn()
    elif c == '2':
      cprint('Firing Disruptors!', 'red', 'on_blue')
      lol = random.choice(weapon_accuracy)

      if lol == 'hit':
        enemy_health = enemy_health - 10

        if enemy_health < 1:
          cprint('Enemy ship defeated!', 'blue', 'on_white')
          cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
          c = input('')
          dailyVictories = dailyVictories + 1
          os.system('clear')
          combat_ops()
        else:
          cprint('Enemy ship damaged', 'blue', 'on_white')
          cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
          c = input('')
          os.system('clear')
          computer_turn()
      else:
        cprint('Miss!', 'red', 'on_white')
        cprint('Press ENTER to continue. ', 'red', 'on_white', end='')
        c = input('')
        os.system('clear')
        computer_turn()
    else:
      cprint('Taking random shot...', 'white', 'on_red')
      lol = random.randint(0, 80)
      enemy_health = enemy_health - lol
      if enemy_health < 1:
        cprint('Enemy Ship defeated!', 'blue', 'on_white')
        cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
        c = input('')
        dailyVictories = dailyVictories + 1
        os.system('clear')
        combat_ops()
      else:
        cprint('Enemy ship intact!', 'red', 'on_white')
        cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
        c = input('')
        os.system('clear')
        computer_turn()
  elif starship_type == 'Double Cannoned StarFighter':
    cprint('1: Small Pulsed Disruptor (10 dmg per hit)', 'red', 'on_grey')
    cprint('2: Disruptor (10 dmg per hit)             ', 'red', 'on_grey')
    cprint("3: Scrapper's Docking Hook                ", 'red', 'on_grey')
    cprint('Type weapon option number: ', 'red', 'on_white', end='')
    c = input('')

    if c == '1':
      cprint('Firing Phasers!', 'red', 'on_blue')
      lol = random.choice(weapon_accuracy)
      
      if lol == 'hit':
        enemy_health = enemy_health - attack_power
        if enemy_health < 1:
          cprint('Enemy Ship Defeated!', 'blue', 'on_white')
          cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
          c = input('')
          dailyVictories = dailyVictories + 1
          os.system('clear')
          combat_ops()
        else:
          cprint('Enemy ship damaged!', 'blue', 'on_white')
          cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
          c = input('')
          os.system('clear')
          computer_turn()
      else:
          cprint('Miss!', 'red', 'on_white')
          cprint('Press ENTER to continue. ', 'red', 'on_white', end='')
          c = input('')
          os.system('clear')
          computer_turn()
    elif c == '2':
      cprint('Firing Disruptors!', 'red', 'on_blue')
      lol = random.choice(weapon_accuracy)

      if lol == 'hit':
        enemy_health = enemy_health - 10

        if enemy_health < 1:
          cprint('Enemy ship defeated!', 'blue', 'on_white')
          cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
          c = input('')
          dailyVictories = dailyVictories + 1
          os.system('clear')
          combat_ops()
        else:
          cprint('Enemy ship damaged', 'blue', 'on_white')
          cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
          c = input('')
          os.system('clear')
          computer_turn()
      else:
        cprint('Miss!', 'red', 'on_white')
        cprint('Press ENTER to continue. ', 'red', 'on_white', end='')
        c = input('')
        os.system('clear')
        computer_turn()
    else:
      cprint('Taking random shot...', 'white', 'on_red')
      lol = random.randint(0, 80)
      enemy_health = enemy_health - lol
      if enemy_health < 1:
        cprint('Enemy Ship defeated!', 'blue', 'on_white')
        cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
        c = input('')
        dailyVictories = dailyVictories + 1
        os.system('clear')
        combat_ops()
      else:
        cprint('Enemy ship intact!', 'red', 'on_white')
        cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
        c = input('')
        os.system('clear')
        computer_turn()
  elif starship_type == 'Scout Craft':
    cprint('1: Union Issued Phaser (60 dmg per hit)', 'red', 'on_grey')
    cprint('2: Disruptor (10 dmg per hit)          ', 'red', 'on_grey')
    cprint("3: Scrapper's Docking Hook             ", 'red', 'on_grey')
    cprint('Type weapon option number: ', 'red', 'on_white', end='')
    c = input('')

    if c == '1':
      cprint('Firing Phasers!', 'red', 'on_blue')
      lol = random.choice(weapon_accuracy)
      
      if lol == 'hit':
        enemy_health = enemy_health - attack_power
        if enemy_health < 1:
          cprint('Enemy Ship Defeated!', 'blue', 'on_white')
          cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
          c = input('')
          dailyVictories = dailyVictories + 1
          os.system('clear')
          combat_ops()
        else:
          cprint('Enemy ship damaged!', 'blue', 'on_white')
          cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
          c = input('')
          os.system('clear')
          computer_turn()
      else:
          cprint('Miss!', 'red', 'on_white')
          cprint('Press ENTER to continue. ', 'red', 'on_white', end='')
          c = input('')
          os.system('clear')
          computer_turn()
    elif c == '2':
      cprint('Firing Disruptors!', 'red', 'on_blue')
      lol = random.choice(weapon_accuracy)

      if lol == 'hit':
        enemy_health = enemy_health - 10

        if enemy_health < 1:
          cprint('Enemy ship defeated!', 'blue', 'on_white')
          cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
          c = input('')
          dailyVictories = dailyVictories + 1
          os.system('clear')
          combat_ops()
        else:
          cprint('Enemy ship damaged', 'blue', 'on_white')
          cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
          c = input('')
          os.system('clear')
          computer_turn()
      else:
        cprint('Miss!', 'red', 'on_white')
        cprint('Press ENTER to continue. ', 'red', 'on_white', end='')
        c = input('')
        os.system('clear')
        computer_turn()
    else:
      cprint('Taking random shot...', 'white', 'on_red')
      lol = random.randint(0, 80)
      enemy_health = enemy_health - lol
      if enemy_health < 1:
        cprint('Enemy Ship defeated!', 'blue', 'on_white')
        cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
        c = input('')
        dailyVictories = dailyVictories + 1
        os.system('clear')
        combat_ops()
      else:
        cprint('Enemy ship intact!', 'red', 'on_white')
        cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
        c = input('')
        os.system('clear')
        computer_turn()
  elif starship_type == 'Bomber Craft':
    cprint('1: Photon Torpedo Launcher (100 dmg per hit)', 'red', 'on_grey')
    cprint('2: Disruptor (10 dmg per hit)               ', 'red', 'on_grey')
    cprint("3: Scrapper's Docking Hook                  ", 'red', 'on_grey')
    cprint('Type weapon option number: ', 'red', 'on_white', end='')
    c = input('')

    if c == '1':
      cprint('Firing Phasers!', 'red', 'on_blue')
      lol = random.choice(weapon_accuracy)
      
      if lol == 'hit':
        enemy_health = enemy_health - attack_power
        if enemy_health < 1:
          cprint('Enemy Ship Defeated!', 'blue', 'on_white')
          cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
          c = input('')
          dailyVictories = dailyVictories + 1
          os.system('clear')
          combat_ops()
        else:
          cprint('Enemy ship damaged!', 'blue', 'on_white')
          cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
          c = input('')
          os.system('clear')
          computer_turn()
      else:
          cprint('Miss!', 'red', 'on_white')
          cprint('Press ENTER to continue. ', 'red', 'on_white', end='')
          c = input('')
          os.system('clear')
          computer_turn()
    elif c == '2':
      cprint('Firing Disruptors!', 'red', 'on_blue')
      lol = random.choice(weapon_accuracy)

      if lol == 'hit':
        enemy_health = enemy_health - 10

        if enemy_health < 1:
          cprint('Enemy ship defeated!', 'blue', 'on_white')
          cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
          c = input('')
          dailyVictories = dailyVictories + 1
          os.system('clear')
          combat_ops()
        else:
          cprint('Enemy ship damaged', 'blue', 'on_white')
          cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
          c = input('')
          os.system('clear')
          computer_turn()
      else:
        cprint('Miss!', 'red', 'on_white')
        cprint('Press ENTER to continue. ', 'red', 'on_white', end='')
        c = input('')
        os.system('clear')
        computer_turn()
    else:
      cprint('Taking random shot...', 'white', 'on_red')
      lol = random.randint(0, 80)
      enemy_health = enemy_health - lol
      if enemy_health < 1:
        cprint('Enemy Ship defeated!', 'blue', 'on_white')
        cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
        c = input('')
        dailyVictories = dailyVictories + 1
        os.system('clear')
        combat_ops()
      else:
        cprint('Enemy ship intact!', 'red', 'on_white')
        cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
        c = input('')
        os.system('clear')
        computer_turn()
  elif starship_type == 'Scrapper Ship':
    cprint('1: Docking Hook    ', 'red', 'on_grey')
    cprint('2: Disruptor (10 dmg per hit)', 'red', 'on_grey')
    c = input('')

    if c == '1':
      cprint('Firing Phasers!', 'red', 'on_blue')
      lol = random.choice(weapon_accuracy)
      
      if lol == 'hit':
        enemy_health = enemy_health - attack_power
        if enemy_health < 1:
          cprint('Enemy Ship Defeated!', 'blue', 'on_white')
          cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
          c = input('')
          dailyVictories = dailyVictories + 1
          os.system('clear')
          combat_ops()
        else:
          cprint('Enemy ship damaged!', 'blue', 'on_white')
          cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
          c = input('')
          os.system('clear')
          computer_turn()
      else:
          cprint('Miss!', 'red', 'on_white')
          cprint('Press ENTER to continue. ', 'red', 'on_white', end='')
          c = input('')
          os.system('clear')
          computer_turn()
    elif c == '2':
      cprint('Firing Disruptors!', 'red', 'on_blue')
      lol = random.choice(weapon_accuracy)

      if lol == 'hit':
        enemy_health = enemy_health - 10

        if enemy_health < 1:
          cprint('Enemy ship defeated!', 'blue', 'on_white')
          cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
          c = input('')
          dailyVictories = dailyVictories + 1
          os.system('clear')
          combat_ops()
        else:
          cprint('Enemy ship damaged', 'blue', 'on_white')
          cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
          c = input('')
          os.system('clear')
          computer_turn()
      else:
        cprint('Miss!', 'red', 'on_white')
        cprint('Press ENTER to continue. ', 'red', 'on_white', end='')
        c = input('')
        os.system('clear')
        computer_turn()
    else:
      cprint('Taking random shot...', 'white', 'on_red')
      lol = random.randint(0, 80)
      enemy_health = enemy_health - lol
      if enemy_health < 1:
        cprint('Enemy Ship defeated!', 'blue', 'on_white')
        cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
        c = input('')
        dailyVictories = dailyVictories + 1
        os.system('clear')
        combat_ops()
      else:
        cprint('Enemy ship intact!', 'red', 'on_white')
        cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
        c = input('')
        os.system('clear')
        computer_turn()
  elif starship_type == 'Commando Personal Starfighter':
    cprint('1: Burst Fire Pulse Cannon (40 dmg per hit)', 'red', 'on_grey')
    cprint('2: Disruptor (10 dmg per hit)              ', 'red', 'on_grey')
    cprint("3: Scrapper's Docking Hook                 ", 'red', 'on_grey')
    cprint('Type weapon option number: ', 'red', 'on_white', end='')
    c = input('')

    if c == '1':
      cprint('Firing Phasers!', 'red', 'on_blue')
      lol = random.choice(weapon_accuracy)
      
      if lol == 'hit':
        enemy_health = enemy_health - attack_power
        if enemy_health < 1:
          cprint('Enemy Ship Defeated!', 'blue', 'on_white')
          cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
          c = input('')
          dailyVictories = dailyVictories + 1
          os.system('clear')
          combat_ops()
        else:
          cprint('Enemy ship damaged!', 'blue', 'on_white')
          cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
          c = input('')
          os.system('clear')
          computer_turn()
      else:
          cprint('Miss!', 'red', 'on_white')
          cprint('Press ENTER to continue. ', 'red', 'on_white', end='')
          c = input('')
          os.system('clear')
          computer_turn()
    elif c == '2':
      cprint('Firing Disruptors!', 'red', 'on_blue')
      lol = random.choice(weapon_accuracy)

      if lol == 'hit':
        enemy_health = enemy_health - 10

        if enemy_health < 1:
          cprint('Enemy ship defeated!', 'blue', 'on_white')
          cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
          c = input('')
          dailyVictories = dailyVictories + 1
          os.system('clear')
          combat_ops()
        else:
          cprint('Enemy ship damaged', 'blue', 'on_white')
          cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
          c = input('')
          os.system('clear')
          computer_turn()
      else:
        cprint('Miss!', 'red', 'on_white')
        cprint('Press ENTER to continue. ', 'red', 'on_white', end='')
        c = input('')
        os.system('clear')
        computer_turn()
    else:
      cprint('Taking random shot...', 'white', 'on_red')
      lol = random.randint(0, 80)
      enemy_health = enemy_health - lol
      if enemy_health < 1:
        cprint('Enemy Ship defeated!', 'blue', 'on_white')
        cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
        c = input('')
        dailyVictories = dailyVictories + 1
        os.system('clear')
        combat_ops()
      else:
        cprint('Enemy ship intact!', 'red', 'on_white')
        cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
        c = input('')
        os.system('clear')
        computer_turn()
  elif starship_type == 'DreadNaught':
    cprint('1: Rapid Fire Plasma Cannon (20 dmg per hit)', 'red', 'on_grey')
    cprint('2: Disruptor (10 dmg per hit)               ', 'red', 'on_grey')
    cprint("Scrapper's Docking Hook                     ", 'red', 'on_grey')
    cprint('Type weapon option number: ', 'red', 'on_white', end='')
    c = input('')

    if c == '1':
      cprint('Firing Phasers!', 'red', 'on_blue')
      lol = random.choice(weapon_accuracy)
      
      if lol == 'hit':
        enemy_health = enemy_health - attack_power
        if enemy_health < 1:
          cprint('Enemy Ship Defeated!', 'blue', 'on_white')
          cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
          c = input('')
          dailyVictories = dailyVictories + 1
          os.system('clear')
          combat_ops()
        else:
          cprint('Enemy ship damaged!', 'blue', 'on_white')
          cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
          c = input('')
          os.system('clear')
          computer_turn()
      else:
          cprint('Miss!', 'red', 'on_white')
          cprint('Press ENTER to continue. ', 'red', 'on_white', end='')
          c = input('')
          os.system('clear')
          computer_turn()
    elif c == '2':
      cprint('Firing Disruptors!', 'red', 'on_blue')
      lol = random.choice(weapon_accuracy)

      if lol == 'hit':
        enemy_health = enemy_health - 10

        if enemy_health < 1:
          cprint('Enemy ship defeated!', 'blue', 'on_white')
          cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
          c = input('')
          dailyVictories = dailyVictories + 1
          os.system('clear')
          combat_ops()
        else:
          cprint('Enemy ship damaged', 'blue', 'on_white')
          cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
          c = input('')
          os.system('clear')
          computer_turn()
      else:
        cprint('Miss!', 'red', 'on_white')
        cprint('Press ENTER to continue. ', 'red', 'on_white', end='')
        c = input('')
        os.system('clear')
        computer_turn()
    else:
      cprint('Taking random shot...', 'white', 'on_red')
      lol = random.randint(0, 80)
      enemy_health = enemy_health - lol
      if enemy_health < 1:
        cprint('Enemy Ship defeated!', 'blue', 'on_white')
        cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
        c = input('')
        dailyVictories = dailyVictories + 1
        os.system('clear')
        combat_ops()
      else:
        cprint('Enemy ship intact!', 'red', 'on_white')
        cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
        c = input('')
        os.system('clear')
        computer_turn()
  elif starship_type == 'Long Range Warp Cannon Transport':
    cprint('1: Warp Cannon (100 dmg per hit)', 'red', 'on_grey')
    cprint('2: Disruptor (10 dmg per hit)   ', 'red', 'on_grey')
    cprint("3: Scrapper's Docking Hook      ", 'red', 'on_grey')
    cprint('Type weapon option number: ', 'red', 'on_white', end='')
    c = input('')

    if c == '1':
      cprint('Firing Phasers!', 'red', 'on_blue')
      lol = random.choice(weapon_accuracy)
      
      if lol == 'hit':
        enemy_health = enemy_health - attack_power
        if enemy_health < 1:
          cprint('Enemy Ship Defeated!', 'blue', 'on_white')
          cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
          c = input('')
          dailyVictories = dailyVictories + 1
          os.system('clear')
          combat_ops()
        else:
          cprint('Enemy ship damaged!', 'blue', 'on_white')
          cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
          c = input('')
          os.system('clear')
          computer_turn()
      else:
          cprint('Miss!', 'red', 'on_white')
          cprint('Press ENTER to continue. ', 'red', 'on_white', end='')
          c = input('')
          os.system('clear')
          computer_turn()
    elif c == '2':
      cprint('Firing Disruptors!', 'red', 'on_blue')
      lol = random.choice(weapon_accuracy)

      if lol == 'hit':
        enemy_health = enemy_health - 10

        if enemy_health < 1:
          cprint('Enemy ship defeated!', 'blue', 'on_white')
          cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
          c = input('')
          dailyVictories = dailyVictories + 1
          os.system('clear')
          combat_ops()
        else:
          cprint('Enemy ship damaged', 'blue', 'on_white')
          cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
          c = input('')
          os.system('clear')
          computer_turn()
      else:
        cprint('Miss!', 'red', 'on_white')
        cprint('Press ENTER to continue. ', 'red', 'on_white', end='')
        c = input('')
        os.system('clear')
        computer_turn()
    else:
      cprint('Taking random shot...', 'white', 'on_red')
      lol = random.randint(0, 80)
      enemy_health = enemy_health - lol
      if enemy_health < 1:
        cprint('Enemy Ship defeated!', 'blue', 'on_white')
        cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
        c = input('')
        dailyVictories = dailyVictories + 1
        os.system('clear')
        combat_ops()
      else:
        cprint('Enemy ship intact!', 'red', 'on_white')
        cprint('Press ENTER to continue.', 'blue', 'on_white', end='')
        c = input('')
        os.system('clear')
        computer_turn()

def computer_turn():
  global defense_power
  cprint('Turn goes to the Holodeck Computer!', 'red', 'on_white')
  print(starship7)
  cprint('Press ENTER to continue.', 'red', 'on_white', end='')
  c = input('')
  k = random.randint(0, 5)
  defense_power = defense_power - k

  if defense_power < 1:
    cprint('Ship destroyed! Abandon ship!', 'red', 'on_grey')
    cprint('Press ENTER to continue.', 'red', 'on_grey', end='')
    c = input('')
    os.system('clear')
    defense_power = 100
    combat_ops()
  else:
    cprint('Shields down to:'+str(defense_power), 'red', 'on_grey')
    cprint('Press ENTER to continue.', 'red', 'on_grey', end='')
    c = input('')
    os.system('clear')
    holodeck_computer_turn()

def faction_ops():
  global faction_name

  cprint('Viewing Factions Options.....', 'white', 'on_blue')
  print(flag)
  cprint('1: Create a faction', 'red', 'on_grey')
  cprint('2: Join an existing faction', 'red', 'on_grey')
  cprint('3: Exit', 'red')
  cprint('Type option number:', 'red', 'on_grey', end='')
  c = input('')
  if c == '1':
    cprint('Faction name: ', 'red', 'on_white', end='')
    c = input('')
    faction_name = c
    req = requests.get('https://starshipdatabase.codesalvageon.repl.co/factions/'+str(faction_name)+'.html')
    if req.status_code == 200:
      cprint('Faction already exists!', 'red', 'on_white')
      cprint('Press ENTER to continue.', 'red', 'on_white', end='')
      c = input('')
      faction_ops()
    else:
      cprint('Creating faction!', 'blue', 'on_white')
      os.system('curl --data "faction-name='+str(faction_name)+'&faction=factiong" https://starshipserver.codesalvageon.repl.co/create_faction.php')
      cprint('Faction created! Press ENTER to continue.', 'blue', 'on_white', end='')
      c = input('')
      os.system('clear')
      logged_in()
  elif c == '2':
    cprint('Faction name: ', 'red', 'on_white', end='')
    c = input('')
    faction_name = c
    req = requests.get('https://starshipdatabase.codesalvageon.repl.co/factions/'+str(faction_name)+'.html')
    if req.status_code == 200:
      cprint('Joined faction!', 'red', 'on_white')
      cprint('Press ENTER to continue.', 'red', 'on_white', end='')
      c = input('')
      os.system('clear')
      logged_in()
    else:
      cprint('Faction does not exist.')
      time.sleep(3)
      os.system('clear')
      logged_in()
  elif c == '3':
    os.system('clear')
    logged_in()
    
  else:
    os.system('clear')
    faction_ops()

def turn_in_victories():
  global totalVictories
  global dailyVictories

  os.system('clear')
  cprint('Turning in daily victories...', 'blue', 'on_grey')
  s = requests.get('https://starshipdatabase.codesalvageon.repl.co/accounts/'+str(shipName)+'/verified.html')
  if s.status_code == 200:
    cprint('Sending data....', 'blue', 'on_grey')
    totalVictories = blanket_subvictories
    print(totalVictories)

  else:
    cprint('Error: Failed to find account', 'red')
    cprint('Press ENTER to continue.', 'red', end='')
    c = input('')
    os.system('clear')
    logged_in()

def fight_random():
  global ship_name_fight

  os.system('clear')
  d = requests.get('https://starshipdatabase.codesalvageon.repl.co/accounts.htm')
  f = d.text
  soup = BeautifulSoup(f, features="html5lib")
  cprint('Finding match...', 'blue', 'on_white')
  for link in soup.find_all('a'):
    system = link.get('href')
    list_of_ships.append(system)
  r = random.choice(list_of_ships)
  os.system('clear')
  ship_name_fight = r
  dog_fight_random()

def dog_fight_random():
  global dog_fight_ship_health
  global dog_fight_ship_enemy_health

  choice = ['turn', 'enemy']

  dog_fight_ship_health = 100
  dog_fight_ship_enemy_health = 100

  cprint('Fighting the USS '+str(ship_name_fight)+'.', 'red', 'on_grey')
  print(starship8)
  cprint('You are about to enter a dogfight! Prepare yourself!', 'red', 'on_white')
  cprint('Press ENTER to begin!', 'red', 'on_white', end='')
  c = input('')
  s = random.choice(choice)

  if s == 'turn':
    os.system('clear')
    dog_fight_you()
  elif s == 'enemy':
    os.system('clear')
    dog_fight_enemy()
  else:
    print('error')
    exit()

def dog_fight_you():
  os.system('clear')

  global dog_fight_ship_health
  global dog_fight_ship_enemy_health

  cprint('Preparing to attack the USS '+str(ship_name_fight), 'blue', 'on_white')
  print(starship8)
  cprint('Press ENTER to fire phasers at target!', 'red', end='')
  c = input('')
  kiki = random.randint(1, 10)
  dog_fight_ship_enemy_health = dog_fight_ship_enemy_health - kiki
  if dog_fight_ship_enemy_health < 1:
    cprint('Enemy ship destroyed!', 'red', 'on_blue')
    cprint('Press ENTER to continue.', 'blue', end='')
    c = input('')
    os.system('clear')
    combat_ops()
  else:
    cprint('Enemy ship damaged!', 'red', 'on_blue')
    cprint('Press ENTER to continue.', 'blue', end='')
    c = input('')
    os.system('clear')
    dog_fight_enemy()

def dog_fight_enemy():
  os.system('clear')

  global dog_fight_ship_health
  global dog_fight_ship_enemy_health

  cprint('The USS '+str(ship_name_fight)+' is attacking!', 'red', 'on_grey')
  print(starship8)
  cprint('Press ENTER to brace for an attack', 'red', end='')
  c = input('')
  didi = random.randint(1, 10)
  dog_fight_ship_health = dog_fight_ship_health - didi
  if dog_fight_ship_health < 1:
    cprint('Our ship has been destroyed! Get into the escape pods!', 'red', 'on_grey')
    cprint('Press ENTER to continue.', 'red', end='')
    c = input('')
    os.system('clear')
    combat_ops()
  else:
    cprint('Ship damaged!', 'red')
    cprint('Press ENTER to return fire!', 'red', end='')
    c = input('')
    os.system('clear')
    dog_fight_you()

def com_ops():
  os.system('clear')
  cprint('Viewing Communication Operations', 'white', 'on_blue')
  print(combadge)
  cprint('Com options:', 'blue', 'on_white')
  cprint('1: Send message on galaxy wide holo-forum', 'red', 'on_grey')
  cprint('2: Exit', 'red')
  cprint('Type in option number: ', 'red', 'on_white', end='')
  c = input('')
  
  if c == '1':
    os.system('clear')
    holo_forum()
  elif c == '2':
    os.system('clear')
    logged_in()
  else:
    os.system('clear')
    com_ops()

def holo_forum():
  os.system('clear')
  page = requests.get('https://starshipdatabase.codesalvageon.repl.co/forum.txt')
  e = page.text
  cprint('Welcome to the Galaxy Wide Holo-Forum', 'blue', 'on_grey')
  print(hologram)
  cprint('Press ENTER to show whats on the forum today.', 'blue', 'on_white', end='')
  c = input('')
  print(e)
  cprint('Options', 'blue', 'on_grey')
  cprint('1: Send message', 'blue', 'on_white')
  cprint('2: Reload messages', 'blue', 'on_white')
  cprint('3: Exit', 'red', 'on_white')
  cprint('Type option number:', 'red', 'on_grey', end='')
  c = input('')

  if c == '1':
    cprint('Message:', 'blue', end='')
    c = input('')
    os.system('curl -d name="'+shipName+'" -d message="'+c+'" https://starshipdatabase.codesalvageon.repl.co/forum_thing.php')
    cprint('Message sent!', 'blue')
    cprint('Press ENTER to continue.', 'blue', end='')
    c = input('')
    os.system('clear')
    holo_forum()
  elif c == '2':
    page = requests.get('https://starshipdatabase.codesalvageon.repl.co/forum.txt')
    e = page.text
    print(e)
    cprint('Press ENTER to continue.', 'blue', end='')
    c = input('')
    os.system('clear')
    holo_forum()
  elif c == '3':
    os.system('clear')
    logged_in()
  else:
    os.system('clear')
    holo_forum()

title_screen()