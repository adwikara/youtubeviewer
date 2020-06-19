from selenium import webdriver
import time
from random import randrange
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#ref = https://cppsecrets.com/users/632106104971151041179810497109101103104495664103109971051084699111109/Python-Increase-youtube-view-count.php


# this is a list of my videos that I want to loop and view to increase my channel's view hours
url_list = [
    ["https://youtu.be/vaPRvXElTTg",61, "Pudge 300 IQ Plays Dota 2"],
    ["https://youtu.be/Zg5J44gsLWw",736, "Double Doom | Custom Hero Chaos"],
    ["https://youtu.be/r8YPcY7TTUE",884, "Throwing With Stampede"],
    ["https://youtu.be/YvQBxZHqJxY",843, "Calculated Double Sentry Ward Dota 2"],
    ["https://youtu.be/QnqPfHMRLfk",306, "Dota 2 Mirana Arrow Compilation Highlights"],
    ["https://youtu.be/1bOG0Vsivs8",780, "The Mirana Strat | Custom Hero Chaos"],
    ["https://youtu.be/0OajKBu1Yhc",815, "Snapfire Meets Toxic Queen"],
    ["https://youtu.be/zcUox8RWceo",825, "Finding Immortal Player In Normal Game"],
    ["https://youtu.be/ofl-wyuOOs4",814, "Trying Out Pangolier Mid Dota 2"],
    ["https://youtu.be/QCqRtYAQfk4",48, "Underlord The Fake Taxi Dota 2"],
    ["https://youtu.be/KZTvoI8e6vc",786, "Snapfire Meets Storm Smurf and PL Spammer"],
    ["https://youtu.be/CQZMzz1oMP8",860, "Mirana 74 Minute Comeback Dota 2"],
    ["https://youtu.be/-BbdLgspGW4",505, "Bristleback + Finger + Shukuchi | Custom Hero Chaos"],
    ["https://youtu.be/gCcoZDyyp8o",673, "Snapfire Pos5 20 Min Guardian Greaves Dota 2"],
    ["https://youtu.be/UmiB0_SgY_k",850, "Mirana Meets One Man Juggernaut Army"],
    ["https://youtu.be/eGEgc5JW_oE",659, "Dota 2 Pugna Support Double Tranquil Boots"],
    ["https://youtu.be/YHkdBIhrhQ0",32, "Techies Catch Me If You Can Dota 2 Jukes"],
    ["https://youtu.be/ynFai6zJSSI",938, "Learning Clinkz Safelane Dota 2"],
    ["https://youtu.be/wiAOP2MwPWY",833, "Learning Necro Saflane In Single Draft"],
    ["https://youtu.be/324wMarojio",645, "Learning Earth Spirit Support In Turbo"],
    ["https://youtu.be/p-lzC4VNoCI",85, "Lucky Tinker Ward Dota 2"],
    ["https://youtu.be/Trea0Kya7GU",743, "Pugna Support Broken Nether Ward Dota 2"],
    ["https://youtu.be/xpuzPaXpucc",808, "Support Lion Rough Game Dota 2"],
    ["https://youtu.be/Cnt316g7mHw",1140, "Mirana Support Rides Unbelievable Throwy Rollercoaster Dota 2"],
    ["https://youtu.be/Av_vecIXA5c",727, "Snapfire Support Gets Brooded Dota 2"],
    ["https://youtu.be/NF4Wv2SnAyc",841, "First Time Witch Doctor Support Dota 2"],
    ["https://youtu.be/PdYC7VVDtuM",1130, "Back In SEA Doto! 2 Team DC Leads To 3 Opponent Abandons??"],
    ["https://youtu.be/WIO9t__ztMo",50, "What Is Shadow Demon Smoking"],
    ["https://youtu.be/LhjTwWwil7w",950, "Vengeful Spirit Aghanims Build Fear Swap!"],
    ["https://youtu.be/Osq-3ZvfVPg",900, "Mirana Support Bad Arrow Game No Problem Dota 2"],
    ["https://youtu.be/naFGNf401gc",660, "Mirana Finds Toxic Throwy Opponent Dota 2"],
    ["https://youtu.be/8t1BfFY1gZQ",990, "Lich Support With The Long Gaze Dota 2"],
    ["https://youtu.be/2GnKtjwfRzQ",750, "Centa Offlane Learns Patience Is The Key To Win Dota 2"]
]

# Last entry - Centa Offlane Learns Patience Is The Key To Win Dota 2

# instantiate the browser
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
browser = webdriver.Chrome("./chromedriver", options=options)

while(True):
    # random link
    link_num = randrange(0, len(url_list))
    
    # random time buffer
    rand_refresh_time = randrange(0, 300) + url_list[link_num][1]

    #open link
    browser.get(url_list[link_num][0])

    print("Open Link: " + str(url_list[link_num][2]) + " for duration of " + str(rand_refresh_time) + " minutes")

    # refresh time before next link
    time.sleep(rand_refresh_time)

    print("Opening new link")
