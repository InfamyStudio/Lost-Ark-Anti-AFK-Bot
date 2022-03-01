pyminify "Lost Ark Anti AFK "Bot.py > Minified.py
pyminify "Lost Ark Anti AFK "Bot.py > "Lost Ark Anti AFK "Bot_Minified_Test.py
fc "Lost Ark Anti AFK "Bot_Minified.py "Lost Ark Anti AFK "Bot_Minified_Test.py
del "Lost Ark Anti AFK "Bot_Minified_Test.py
pyarmor obfuscate "Lost Ark Anti AFK "Bot_Minified.py
del Minified.spec
move /Y dist\Minified.py Obfuscated.py
rmdir /s /q dist
