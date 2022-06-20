import random 
print("\nPokemon Calculator")
print("\nCharizard VS. Feraligatr")  
print("\nCharizard LVL = 90, SAtt = 205")     
print("\nFeraligatr LVL = 95, SDef = 188 \nCharizard uses Fire Blast to Feraligatr but its not very effective" )

level = 90
SAtt = 205
SDef = 188
Power = 110
Targets = 1
Weather = 1
Badge = 1
critical = 1,2
crit =random.choice(critical)
r =.85,1
ran = random.choice(r)
Stab = 1
Type = 1
Burn = 1
Other = 1
Modifier = Targets * Weather * Badge * crit * ran * Stab * Type * Burn * Other

if crit == 2:
    print( " \n              WASAK!!!!!         ")

Damage = (((((2*level/5)+2 )*Power*SAtt/SDef)/50)+2)* Modifier

print("\nCharizard's Damage tp Feraligatr is",Damage,"\n")