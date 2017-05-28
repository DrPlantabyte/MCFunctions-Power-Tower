import os
import random
random.seed()

def main():
	function_dir = os.path.dirname(__file__)+os.sep+"world"+os.sep+"data"+os.sep+"functions"+os.sep+"powertower"
	os.makedirs(function_dir, exist_ok=True)
	with open(function_dir+os.sep+"build.mcfunction", "w") as fout:
		#
		def out(text):
			fout.write(text)
			if not text.endswith("\n"):
				fout.write("\n")
		out("say Constructing Power Tower...")
		out("tp @p -24 70 -24")
		out("fill -24 69 -24 -24 69 -24 minecraft:dirt")
		out("fill -24 70 -24 -24 71 -24 minecraft:air")
		
		# use the summon command generator at 
		# https://www.digminecraft.com/generators/summon_mob.php
		# and then substitute the mob data like this 
		# (removing ther outer {} from the summon command):
		# setblock ~ ~1 ~ mob_spawner 0 replace {SpawnData:{id:"Zombie",%s}}
		monster_menus = []
		# levels: zombies, skeletons & arthropods, flying creepers & tnt, illagers, nether forces, guardians
		boss_rooms = [{},{},{},{},{},{}]
		### Level 1: zombies
		monster_menus.append([ \
				'{id:"Skeleton", HandItems:[{Count:1,id:"minecraft:bow"},{}], ArmorItems:[{},{},{},{Count:1,id:leather_helmet}]}',\
				'{id:"Zombie", ArmorItems:[{},{},{},{Count:1,id:leather_helmet}]}',\
		])
		boss_rooms[0]['spawner']='{SpawnData:%s}' % ('{id:zombie,HandItems:[{Count:1,id:iron_axe},{Count:1,id:shield}],ArmorItems:[{Count:1,id:leather_boots},{Count:1,id:chainmail_leggings},{Count:1,id:iron_chestplate},{}]}')
		boss_rooms[0]['boss']=('zombie', '{PersistenceRequired:1,HandItems:[{Count:1,id:diamond_sword,tag:{ench:[{id:20,lvl:1},{id:21,lvl:1}]}},{Count:1,id:shield,tag:{ench:[{id:34,lvl:2}]}}],ArmorItems:[{Count:1,id:iron_boots,tag:{ench:[{id:2,lvl:2}]}},{Count:1,id:leather_leggings,tag:{ench:[{id:1,lvl:2}]}},{Count:1,id:diamond_chestplate,tag:{ench:[{id:4,lvl:2}]}},{Count:1,id:golden_helmet,tag:{ench:[{id:5,lvl:3}]}}],CustomName:"King of the Zombies",HandDropChances:[1.0f,1.0f],ArmorDropChances:[1.0f,1.0f,1.0f,1.0f],ActiveEffects:[{Id:1,Amplifier:0,Duration:999999}]}')
		boss_rooms[0]['guard']=('chicken', '{Passengers:[{id:zombie,PersistenceRequired:1,HandItems:[{Count:1,id:golden_sword},{}],ArmorItems:[{Count:1,id:golden_boots},{},{Count:1,id:chainmail_chestplate},{Count:1,id:iron_helmet}],CustomName:"Zombie Knight",HandDropChances:[0.5f,0.0f],ArmorDropChances:[0.5f,0.0f,0.5f,0.5f],ActiveEffects:[{Id:1,Amplifier:0,Duration:999999}],IsBaby:1}]}')
		boss_rooms[0]['floor']='minecraft:mycelium'
		boss_rooms[0]['ceiling']='minecraft:planks'
		boss_rooms[0]['ring']='minecraft:planks'
		boss_rooms[0]['column']='minecraft:hay_block'
		boss_rooms[0]['wall']='minecraft:stonebrick'
		boss_rooms[0]['air']='minecraft:air'
		boss_rooms[0]['windows']='minecraft:dirt'
		boss_rooms[0]['decorations']=['minecraft:pumpkin 0','minecraft:pumpkin 1','minecraft:pumpkin 2','minecraft:pumpkin 3', 'minecraft:redstone_torch 0']
		boss_rooms[0]['treasure_blocks']=['minecraft:chest 1 replace {LootTable:"minecraft:chests/simple_dungeon"}', 'minecraft:iron_block', 'minecraft:gold_block', 'minecraft:emerald_block']
		### Level 2: skeletons & arthropods
		skulls = []
		for n in range (0,16):
			skulls.append('minecraft:skull 1 replace {SkullType:0,Rot:%s}' \
					% (n))
			skulls.append('minecraft:skull 1 replace {SkullType:1,Rot:%s}' \
					% (n))
		monster_menus.append([ \
				'{id:"Skeleton", HandItems:[{Count:1,id:"minecraft:bow"},{}], ArmorItems:[{},{},{},{Count:1,id:leather_helmet}]}',\
				'{id:"minecraft:cave_spider"}',\
				'{id:"minecraft:spider"}',\
				'{id:"minecraft:silverfish"}',\
		])
		boss_rooms[1]['spawner']='{SpawnData:%s}' % ('{id:"minecraft:cave_spider"}')
		boss_rooms[1]['boss']=('spider', '{PersistenceRequired:1,CustomName:"Horsie",ActiveEffects:[{Id:10,Amplifier:0,Duration:999999}],Passengers:[{id:skeleton,PersistenceRequired:1,HandItems:[{Count:1,id:bow,tag:{ench:[{id:51,lvl:1},{id:50,lvl:1}]}},{}],ArmorItems:[{Count:1,id:chainmail_boots,tag:{ench:[{id:7,lvl:2}]}},{Count:1,id:chainmail_leggings,tag:{ench:[{id:7,lvl:2}]}},{Count:1,id:chainmail_chestplate,tag:{ench:[{id:7,lvl:2}]}},{Count:1,id:chainmail_helmet,tag:{ench:[{id:7,lvl:2}]}}],CustomName:"Skelington McBowboy",HandDropChances:[1.0f,0.0f],ArmorDropChances:[1.0f,1.0f,1.0f,1.0f],ActiveEffects:[{Id:10,Amplifier:0,Duration:999999},{Id:12,Amplifier:0,Duration:999999},{Id:13,Amplifier:0,Duration:999999}]}]}')
		boss_rooms[1]['guard']=('spider', '{PersistenceRequired:1,ActiveEffects:[{Id:1,Amplifier:1,Duration:999999},{Id:8,Amplifier:1,Duration:999999},{Id:10,Amplifier:0,Duration:999999}], Passengers:[{id:pig,PersistenceRequired:1,CustomName:"Spider Pig",ActiveEffects:[{Id:1,Amplifier:1,Duration:999999},{Id:8,Amplifier:1,Duration:999999},{Id:10,Amplifier:0,Duration:999999}]}]}')
		boss_rooms[1]['floor']='minecraft:slime'
		boss_rooms[1]['ceiling']='minecraft:leaves 7'
		boss_rooms[1]['ring']='minecraft:web'
		boss_rooms[1]['column']='minecraft:bone_block 1'
		boss_rooms[1]['wall']='minecraft:stone 4'
		boss_rooms[1]['air']='minecraft:air'
		boss_rooms[1]['windows']='minecraft:stone 2'
		boss_rooms[1]['decorations']=skulls + ['minecraft:web']*len(skulls)
		boss_rooms[1]['treasure_blocks']=['minecraft:chest 1 replace {LootTable:"minecraft:chests/abandoned_mineshaft"}','minecraft:chest 1 replace {LootTable:"minecraft:chests/desert_pyramid"}', 'minecraft:chest 1 replace {LootTable:"minecraft:chests/abandoned_mineshaft"}', 'minecraft:chest 1 replace {LootTable:"minecraft:chests/jungle_temple"}', 'minecraft:chest 1 replace {LootTable:"minecraft:chests/stronghold_corridor"}', 'minecraft:chest 1 replace {LootTable:"minecraft:chests/stronghold_crossing"}', 'minecraft:chest 1 replace {LootTable:"minecraft:chests/stronghold_library"}', 'minecraft:gold_block', 'minecraft:iron_block', 'minecraft:diamond_block']
		### Level 3: creepers & tnt & wierd stuff
		monster_menus.append([ \
				'{id:"zombie", ActiveEffects:[{Id:6,Amplifier:10,Duration:999999}], Passengers:[{id:"bat", Passengers:[{id:creeper}]}]}',\
				'{id:"creeper"}',\
				'{id:"creeper", powered:1}'\
		])
		#boss_rooms[2]['spawner']='{id:"zombie", ActiveEffects:[{Id:6,Amplifier:10,Duration:999999}], Passengers:[{id:"bat", Passengers:[{id:creeper}]}]}'
		boss_rooms[2]['spawner']='{SpawnData:{id:"zombie", ActiveEffects:[{Id:6,Amplifier:10,Duration:999999}], Passengers:[{id:"bat", ActiveEffects:[{Id:20,Amplifier:1,Duration:999999}], Passengers:[{id:tnt, Fuse:180}]}]}, SpawnCount:2,SpawnRange:6,maxNearbyEntities:4,Delay:20,MinSpawnDelay:60,MaxSpawnDelay:120}'
		boss_rooms[2]['boss']=('creeper', '{Invulnerable:1,PersistenceRequired:1,CustomName:"Creepy McGriefer",powered:1}')
		boss_rooms[2]['guard']=('creeper', '{Invulnerable:1,ActiveEffects:[{Id:14,Amplifier:0,Duration:999999}],PersistenceRequired:1,CustomName:"Phantom Creeper"}')
		boss_rooms[2]['floor']='minecraft:obsidian'
		boss_rooms[2]['ceiling']='minecraft:obsidian'
		boss_rooms[2]['ring']='minecraft:obsidian'
		boss_rooms[2]['column']='minecraft:obsidian'
		boss_rooms[2]['wall']='minecraft:obsidian'
		boss_rooms[2]['air']='minecraft:air'
		boss_rooms[2]['windows']='minecraft:air'
		boss_rooms[2]['decorations']=['minecraft:air']
		boss_rooms[2]['treasure_blocks']=['minecraft:diamond_block']
		### Level 4: illagers
		monster_menus.append([ \
				'{id:"minecraft:illusion_illager, HandItems:[{Count:1,id:bow},{}]"}',\
				'{id:"minecraft:vindication_illager", HandItems:[{Count:1,id:iron_axe},{Count:1,id:shield}]}',\
				'{id:"minecraft:evocation_illager"}',\
				'{id:"minecraft:witch"}'\
		])
		boss_rooms[3]['spawner']='{SpawnData:%s}' % ('{id:vindication_illager, HandItems:[{Count:1,id:iron_sword,tag:{ench:[{id:16,lvl:2}]}},{}],HandDropChances:[0.1f,0.0f],ActiveEffects:[{Id:1,Amplifier:0,Duration:999999},{Id:5,Amplifier:0,Duration:999999}]}')
		boss_rooms[3]['boss']=('evocation_illager', '{PersistenceRequired:1,CustomName:"Illius the Great",ActiveEffects:[{Id:1,Amplifier:1,Duration:999999},{Id:10,Amplifier:0,Duration:999999},{Id:21,Amplifier:0,Duration:999999}]}')
		boss_rooms[3]['guard']=('illusion_illager', '{PersistenceRequired:1, HandItems:[{Count:1,id:bow},{}], CustomName:"Illager Elite Guard", ActiveEffects:[{Id:21,Amplifier:0,Duration:999999},{Id:22,Amplifier:0,Duration:999999}]}')
		boss_rooms[3]['floor']='minecraft:planks 5'
		boss_rooms[3]['ceiling']='minecraft:concrete 15'
		boss_rooms[3]['ring']='minecraft:water'
		boss_rooms[3]['column']='minecraft:log2 1'
		boss_rooms[3]['wall']='minecraft:stone 6'
		boss_rooms[3]['air']='minecraft:air'
		boss_rooms[3]['windows']='minecraft:stained_glass 14'
		boss_rooms[3]['decorations']=['minecraft:lit_pumpkin 0','minecraft:lit_pumpkin 1','minecraft:lit_pumpkin 2','lit_minecraft:pumpkin 3', 'minecraft:dark_oak_fence', 'minecraft:dark_oak_stairs 0', 'minecraft:dark_oak_stairs 1', 'minecraft:dark_oak_stairs 2', 'minecraft:dark_oak_stairs 3', 'minecraft:planks 5', 'minecraft:iron_bars']
		boss_rooms[3]['treasure_blocks']=['minecraft:chest 1 replace {LootTable:"minecraft:chests/woodland_mansion"}', 'minecraft:chest 1 replace {LootTable:"minecraft:chests/village_blacksmith"}', 'minecraft:chest 1 replace {LootTable:"minecraft:chests/stronghold_library"}', 'minecraft:chest 1 replace {LootTable:"minecraft:chests/igloo_chest"}']
		### Level 5: nether forces
		monster_menus.append([ \
				'{id:wither_skeleton, HandItems:[{Count:1,id:iron_sword,tag:{ench:[{id:16,lvl:2},{id:19,lvl:2},{id:20,lvl:2}]}},{Count:1,id:shield}], ArmorItems:[{Count:1,id:golden_boots},{Count:1,id:chainmail_leggings},{Count:1,id:iron_chestplate},{Count:1,id:diamond_helmet}] }',\
				'{id:zombie_pigman, Anger:32767, HandItems:[{Count:1,id:golden_sword},{}], ArmorItems:[{Count:1,id:golden_boots},{Count:1,id:golden_leggings},{Count:1,id:golden_chestplate},{Count:1,id:golden_helmet}] }', \
				'{id:blaze}',\
				'{id:"minecraft:magma_cube", Size:1}'
				
		])
		boss_rooms[4]['spawner']='{SpawnData:%s}' % ('{id:zombie_pigman, Anger:32767, HandItems:[{Count:1,id:golden_sword},{}], ArmorItems:[{Count:1,id:golden_boots},{Count:1,id:golden_leggings},{Count:1,id:golden_chestplate},{Count:1,id:golden_helmet}] }')
		boss_rooms[4]['boss']=('wither_skeleton', '{PersistenceRequired:1,HandItems:[{Count:1,id:diamond_axe,tag:{ench:[{id:16,lvl:5}]}},{Count:1,id:shield,tag:{ench:[{id:70,lvl:1}]}}],ArmorItems:[{Count:1,id:golden_boots,tag:{ench:[{id:2,lvl:4},{id:9,lvl:2},{id:34,lvl:3}]}},{Count:1,id:leather_leggings,tag:{ench:[{id:1,lvl:4},{id:7,lvl:3}]}},{Count:1,id:iron_chestplate,tag:{ench:[{id:3,lvl:4},{id:7,lvl:3}]}},{Count:1,id:diamond_helmet,tag:{ench:[{id:4,lvl:4},{id:5,lvl:3}]}}],CustomName:"The Prince of Darkness",HandDropChances:[1.0f,1.0f],ArmorDropChances:[1.0f,1.0f,1.0f,1.0f],ActiveEffects:[{Id:1,Amplifier:1,Duration:999999},{Id:5,Amplifier:1,Duration:999999}]}')
		boss_rooms[4]['guard']=('blaze', '{PersistenceRequired:1,CustomName:"Shadow Guard",ActiveEffects:[{Id:10,Amplifier:1,Duration:999999},{Id:14,Amplifier:0,Duration:999999},{Id:21,Amplifier:0,Duration:999999}]}')
		boss_rooms[4]['floor']='minecraft:netherrack'
		boss_rooms[4]['ceiling']='minecraft:planks'
		boss_rooms[4]['ring']='minecraft:lava'
		boss_rooms[4]['column']='minecraft:quartz_block 2'
		boss_rooms[4]['wall']='minecraft:nether_brick'
		boss_rooms[4]['air']='minecraft:air'
		boss_rooms[4]['windows']='minecraft:nether_brick_fence'
		boss_rooms[4]['decorations']=['minecraft:fire 0']
		boss_rooms[4]['treasure_blocks']=['minecraft:chest 1 replace {LootTable:"minecraft:chests/nether_bridge"}', 'minecraft:iron_block', 'minecraft:gold_block', 'minecraft:emerald_block', 'minecraft:diamond_block']
		### Level 1: water guardians
		monster_menus.append([ \
				'{id:skeleton, HandItems:[{Count:1,id:bow,tag:{ench:[{id:48,lvl:5},{id:49,lvl:2}]}},{}], ArmorItems:[{Count:1,id:leather_boots,tag:{ench:[{id:0,lvl:4}]}},{Count:1,id:chainmail_leggings,tag:{ench:[{id:0,lvl:4}]}},{Count:1,id:chainmail_chestplate,tag:{ench:[{id:0,lvl:4}]}},{Count:1,id:diamond_helmet,tag:{ench:[{id:0,lvl:4}]}}] }',\
				'{id:creeper, Invulnerable:1, powered:1}', \
				'{id:spider, ActiveEffects:[{Id:5,Amplifier:1,Duration:999999}, {Id:14,Amplifier:0,Duration:999999}] }',\
				'{id:zombie, HandItems:[{Count:1,id:diamond_sword,tag:{ench:[{id:16,lvl:5}]}},{Count:1,id:shield}], ArmorItems:[{Count:1,id:iron_boots,tag:{ench:[{id:0,lvl:4}]}},{Count:1,id:chainmail_leggings,tag:{ench:[{id:0,lvl:4}]}},{Count:1,id:chainmail_chestplate,tag:{ench:[{id:0,lvl:4}]}},{Count:1,id:diamond_helmet,tag:{ench:[{id:0,lvl:4}]}}] }'
		])
		boss_rooms[5]['spawner']='{SpawnData:%s}' % ('{id:guardian, ActiveEffects:[{Id:7,Amplifier:10,Duration:999999}], Passengers:[{id:skeleton, HandItems:[{Count:1,id:bow,tag:{ench:[{id:48,lvl:3}]}},{}], ArmorItems:[{},{},{},{Count:1,id:golden_helmet,tag:{ench:[{id:5,lvl:3},{id:34,lvl:3}]}}], ArmorDropChances:[0.0f,0.0f,0.0f,0.1f], ActiveEffects:[{Id:13,Amplifier:0,Duration:999999}]}]}')
		#boss_rooms[5]['boss']=('elder_guardian', '{id:elder_guardian, PersistenceRequired:1,CustomName:"Eye of Cthulhu", ActiveEffects:[{Id:10,Amplifier:1,Duration:999999}]}') # super hard mode
		boss_rooms[5]['boss']=('guardian', '{PersistenceRequired:1,CustomName:"Prime Guardian",ActiveEffects:[{Id:1,Amplifier:1,Duration:999999},{Id:3,Amplifier:0,Duration:999999},{Id:5,Amplifier:1,Duration:999999},{Id:10,Amplifier:1,Duration:999999},{Id:11,Amplifier:0,Duration:999999},{Id:12,Amplifier:0,Duration:999999},{Id:13,Amplifier:0,Duration:999999},{Id:16,Amplifier:0,Duration:999999},{Id:21,Amplifier:0,Duration:999999},{Id:22,Amplifier:0,Duration:999999}]}')
		boss_rooms[5]['guard']=('guardian', '{id:guardian, PersistenceRequired:1, CustomName:"Guardian of the Eye", ActiveEffects:[{Id:1,Amplifier:1,Duration:999999}, {Id:5,Amplifier:1,Duration:999999}, {Id:10,Amplifier:1,Duration:999999}, {Id:12,Amplifier:0,Duration:999999}, {Id:21,Amplifier:0,Duration:999999}, {Id:22,Amplifier:0,Duration:999999}]}')
		boss_rooms[5]['floor']='minecraft:prismarine 2'
		boss_rooms[5]['ceiling']='minecraft:glass'
		boss_rooms[5]['ring']='minecraft:sea_lantern'
		boss_rooms[5]['column']='minecraft:sponge 1'
		boss_rooms[5]['wall']='minecraft:glass'
		boss_rooms[5]['air']='minecraft:water'
		boss_rooms[5]['windows']='minecraft:prismarine 1'
		boss_rooms[5]['decorations']=['minecraft:sponge 1', 'minecraft:sponge 1', 'minecraft:sponge 1', 'minecraft:prismarine 0', 'minecraft:gravel']
		boss_rooms[5]['treasure_blocks']=['minecraft:chest 1 replace {LootTable:"minecraft:chests/end_city_treasure"}', 'minecraft:gold_block', 'minecraft:diamond_block']
		###
		base = 64
		out(f(fillCylinder((0, base - 32, 0), 12, 32, "minecraft:cobblestone")))
		#
		later_commands = ""
		middle_commands = ""
		early_commands = ""
		for tier in range(0,6):
			tier_base = base + tier * 32
			monsters = monster_menus[tier]
			if(tier >= 5):
				top_tier = True
			else:
				top_tier = False
			for level in range(0,4):
				h = tier_base + level*8
				early_commands += towerShaft(h)
				if(level < 2):
					middle_commands += addStairs(h)
					middle_commands += addMurderHoles(h,monster_menus[tier])
					middle_commands += addTraps(h)
			later_commands += createBossRoom(tier_base + 16, \
					spawner=boss_rooms[tier]['spawner'], \
					boss=boss_rooms[tier]['boss'], \
					guard=boss_rooms[tier]['guard'], \
					floor=boss_rooms[tier]['floor'], \
					ceiling=boss_rooms[tier]['ceiling'], \
					ring=boss_rooms[tier]['ring'], \
					column=boss_rooms[tier]['column'], \
					wall=boss_rooms[tier]['wall'], \
					air=boss_rooms[tier]['air'], \
					windows=boss_rooms[tier]['windows'], \
					decorations=boss_rooms[tier]['decorations'], \
					treasure_blocks=boss_rooms[tier]['treasure_blocks'], \
					top=top_tier\
			)
		#
		out(early_commands)
		out(middle_commands)
		out(later_commands)
		out("say ...construction complete!")
	
def towerShaft(base_height):
	commands = ""
	# shaft
	commands += f(fillCylinder((0, base_height, 0), 12, 8, "minecraft:air"))
	commands += f(fillCylinder((0, base_height, 0), 9, 8, "minecraft:stonebrick"))
	commands += f(fillCylinder((0, base_height, 0), 8, 8, "minecraft:obsidian"))
	return commands

def addStairs(base_height):
	commands = ""
	# stairway
	path_xz_ref = [(0,-10,0),(1,-10,0),(2,-10,0),(2, -9,0),(3, -9,1),(4, -9,0),(5, -9,0),(6, -9,1),(6, -8,0),(7, -8,0),(7, -7,0),(8, -7,0),(8, -6,0),(9, -6,0),(9, -5,1),(9, -4,0),(9, -3,0),(9, -2,1),(10, -2,0),(10, -1,0)]
	path_xz = []
	for pt in path_xz_ref:
		path_xz.append(pt)
	for pt in path_xz_ref:
		path_xz.append( (-1*pt[1], pt[0], pt[2]) )
	for pt in path_xz_ref:
		path_xz.append( (-1*pt[0], -1*pt[1], pt[2]) )
	for pt in path_xz_ref:
		path_xz.append( (pt[1], -1*pt[0], pt[2]) )
	h = base_height
	dh = 0
	for pt in path_xz:
		dh += pt[2]
		if( dh % 2 == 0):
			material = "minecraft:wooden_slab 8"
			commands += f("setblock %s %s %s %s", pt[0], int(dh/2 + h)-1, pt[1], material)
			material = "minecraft:wooden_slab 0"
		else:
			material = "minecraft:planks 0"
		commands += f("setblock %s %s %s %s", pt[0], int(dh/2 + h), pt[1], material)
	
	# return command
	return commands
	
def addMurderHoles(base_height, spawner_options):
	commands = ""
	# murder holes
	commands += f("fill %s %s %s %s %s %s minecraft:air", \
			-1, base_height+1, -9, 1, base_height+3, -3 )
	commands += f("setblock %s %s %s minecraft:mob_spawner 0 replace {SpawnData:%s,SpawnCount:2,SpawnRange:2,maxNearbyEntities:4,Delay:20,MinSpawnDelay:60,MaxSpawnDelay:120}", \
			0, base_height+1, -4, pick(spawner_options))
	commands += f("fill %s %s %s %s %s %s minecraft:air", \
			9, base_height+3, -1, 3, base_height+5, 1 )
	commands += f("setblock %s %s %s minecraft:mob_spawner 0 replace {SpawnData:%s,SpawnCount:2,SpawnRange:2,maxNearbyEntities:4,Delay:20,MinSpawnDelay:60,MaxSpawnDelay:120}", \
			4, base_height+3, 0, pick(spawner_options))
	commands += f("fill %s %s %s %s %s %s minecraft:air", \
			-1, base_height+5, 9, 1, base_height+7, 3 )
	commands += f("setblock %s %s %s minecraft:mob_spawner 0 replace {SpawnData:%s,SpawnCount:2,SpawnRange:2,maxNearbyEntities:4,Delay:20,MinSpawnDelay:60,MaxSpawnDelay:120}", \
			0, base_height+5, 4, pick(spawner_options))
	commands += f("fill %s %s %s %s %s %s minecraft:air", \
			-9, base_height+7, -1, -3, base_height+9, 1 )
	commands += f("setblock %s %s %s minecraft:mob_spawner 0 replace {SpawnData:%s,SpawnCount:2,SpawnRange:2,maxNearbyEntities:4,Delay:20,MinSpawnDelay:60,MaxSpawnDelay:120}", \
			-4, base_height+7, 0, pick(spawner_options))
	archer = '{SpawnData:{id:"Skeleton",%s},SpawnCount:1,SpawnRange:2,maxNearbyEntities:4,Delay:20,MinSpawnDelay:60,MaxSpawnDelay:120}' %  ('HandItems:[{Count:1,id:bow,tag:{ench:[{id:49,lvl:2}]}},{}],ArmorItems:[{Count:1,id:leather_boots},{Count:1,id:chainmail_leggings},{Count:1,id:leather_chestplate},{Count:1,id:iron_helmet}],HandDropChances:[0.1f,0.0f],ArmorDropChances:[0.1f,0.1f,0.1f,0.1f]')
	#
	commands += f("fill %s %s %s %s %s %s minecraft:air", \
			7, base_height+3, -7, 3, base_height+3+2, -3 )
	commands += f("setblock %s %s %s minecraft:mob_spawner 0 replace %s", \
			 5, base_height+3, -5, archer)
	commands += f("setblock %s %s %s minecraft:stonebrick 0 replace", \
			 6, base_height+3, -7)
	commands += f("setblock %s %s %s minecraft:stonebrick 0 replace", \
			 6, base_height+3+2, -7)
	commands += f("setblock %s %s %s minecraft:stonebrick 0 replace", \
			 7, base_height+3, -6)
	commands += f("setblock %s %s %s minecraft:stonebrick 0 replace", \
			 7, base_height+3+2, -6)
	#
	commands += f("fill %s %s %s %s %s %s minecraft:air", \
			7, base_height+5, 7, 3, base_height+5+2, 3 )
	commands += f("setblock %s %s %s minecraft:mob_spawner 0 replace %s", \
			 5, base_height+5, 5, archer)
	commands += f("setblock %s %s %s minecraft:stonebrick 0 replace", \
			 6, base_height+5, 7)
	commands += f("setblock %s %s %s minecraft:stonebrick 0 replace", \
			 6, base_height+5+2, 7)
	commands += f("setblock %s %s %s minecraft:stonebrick 0 replace", \
			 7, base_height+5, 6)
	commands += f("setblock %s %s %s minecraft:stonebrick 0 replace", \
			 7, base_height+5+2, 6)
	#
	commands += f("fill %s %s %s %s %s %s minecraft:air", \
			-7, base_height+7, 7, -3, base_height+7+2, 3 )
	commands += f("setblock %s %s %s minecraft:mob_spawner 0 replace %s", \
			 -5, base_height+7, 5, archer)
	commands += f("setblock %s %s %s minecraft:stonebrick 0 replace", \
			 -6, base_height+7, 7)
	commands += f("setblock %s %s %s minecraft:stonebrick 0 replace", \
			 -6, base_height+7+2, 7)
	commands += f("setblock %s %s %s minecraft:stonebrick 0 replace", \
			 -7, base_height+7, 6)
	commands += f("setblock %s %s %s minecraft:stonebrick 0 replace", \
			 -7, base_height+7+2, 6)
	#
	commands += f("fill %s %s %s %s %s %s minecraft:air", \
			-7, base_height+9, -7, -3, base_height+9+2, -3 )
	commands += f("setblock %s %s %s minecraft:mob_spawner 0 replace %s", \
			 -5, base_height+9, -5, archer)
	commands += f("setblock %s %s %s minecraft:stonebrick 0 replace", \
			 -6, base_height+9, -7)
	commands += f("setblock %s %s %s minecraft:stonebrick 0 replace", \
			 -6, base_height+9+2, -7)
	commands += f("setblock %s %s %s minecraft:stonebrick 0 replace", \
			 -7, base_height+9, -6)
	commands += f("setblock %s %s %s minecraft:stonebrick 0 replace", \
			 -7, base_height+9+2, -6)
	
	return commands

def createBossRoom(base_height=64, \
				spawner='{SpawnData:%s}' % ('{id:zombie,HandItems:[{Count:1,id:iron_axe},{Count:1,id:shield}],ArmorItems:[{Count:1,id:leather_boots},{Count:1,id:chainmail_leggings},{Count:1,id:iron_chestplate},{}]}'), \
				boss=('zombie', '{PersistenceRequired:1,HandItems:[{Count:1,id:diamond_sword,tag:{ench:[{id:20,lvl:1},{id:21,lvl:1}]}},{Count:1,id:shield,tag:{ench:[{id:34,lvl:2}]}}],ArmorItems:[{Count:1,id:iron_boots,tag:{ench:[{id:2,lvl:2}]}},{Count:1,id:leather_leggings,tag:{ench:[{id:1,lvl:2}]}},{Count:1,id:diamond_chestplate,tag:{ench:[{id:4,lvl:2}]}},{Count:1,id:golden_helmet,tag:{ench:[{id:5,lvl:3}]}}],CustomName:"King of the Zombies",HandDropChances:[1.0f,1.0f],ArmorDropChances:[1.0f,1.0f,1.0f,1.0f],ActiveEffects:[{Id:1,Amplifier:0,Duration:999999}]}'), \
				guard=('chicken', '{Passengers:[{id:zombie,PersistenceRequired:1,HandItems:[{Count:1,id:golden_sword},{}],ArmorItems:[{Count:1,id:golden_boots},{},{Count:1,id:chainmail_chestplate},{Count:1,id:iron_helmet}],CustomName:"Zombie Knight",HandDropChances:[0.5f,0.0f],ArmorDropChances:[0.5f,0.0f,0.5f,0.5f],ActiveEffects:[{Id:1,Amplifier:0,Duration:999999}],IsBaby:1}]}'), \
				floor='minecraft:mycelium', \
				ceiling='minecraft:planks', \
				ring='minecraft:planks', \
				column='minecraft:hay_block', \
				wall='minecraft:stonebrick', \
				air='minecraft:air', \
				windows='minecraft:air', \
				decorations=['minecraft:pumpkin 0','minecraft:pumpkin 1','minecraft:pumpkin 2','minecraft:pumpkin 3'], \
				treasure_blocks=['minecraft:chest 1 replace {LootTable:"minecraft:chests/simple_dungeon"}'], \
				top=False\
	):
	commands = ""
	floor_alt = base_height + 6
	ciel_alt = base_height + 16 - 2
	room_height = ciel_alt - floor_alt
	
	#clear space
	commands += f(fillCylinder((0, base_height, 0), 9, 16, "minecraft:air"))
	commands += f(fillCylinder((0, base_height+1, 0), 12, 15, "minecraft:air"))
	
	# collars
	commands += f(fillCylinder((0, base_height, 0), 9, (floor_alt - base_height), "minecraft:stonebrick"))
	
	commands += f(fillCylinder((0, floor_alt-3, 0), 10, 1, "minecraft:stonebrick"))
	commands += f(fillCylinder((0, floor_alt-2, 0), 11, 1, "minecraft:stonebrick"))
	commands += f(fillCylinder((0, floor_alt-1, 0), 12, 1, "minecraft:stonebrick"))
	# 
	if top == False:
		commands += f(fillCylinder((0, ciel_alt, 0), 12, 1, "minecraft:stonebrick"))
		commands += f(fillCylinder((0, ciel_alt, 0), 11, 2, "minecraft:stonebrick"))
		commands += f(fillCylinder((0, ciel_alt, 0), 10, 3, "minecraft:stonebrick"))
		commands += f(fillCylinder((0, ciel_alt, 0), 9, (base_height + 16 - ciel_alt), "minecraft:stonebrick"))
	#
	commands += f(fillCylinder((0, base_height, 0), 8, 7, "minecraft:obsidian"))
	# room
	commands += f(fillCylinder((0, floor_alt, 0), \
			12, (ciel_alt - floor_alt), wall))
	commands += f("fill %s %s %s %s %s %s %s", \
			0, floor_alt+2, -12,   0, ciel_alt-2, 12, windows)
	commands += f("fill %s %s %s %s %s %s %s", \
			-12, floor_alt+2, 0,   12, ciel_alt-2, 0, windows)
	commands += f("fill %s %s %s %s %s %s %s", \
			-4, floor_alt+2, -11,   -4, ciel_alt-2, 11, windows)
	commands += f("fill %s %s %s %s %s %s %s", \
			4, floor_alt+2, -11,     4, ciel_alt-2, 11, windows)
	commands += f("fill %s %s %s %s %s %s %s", \
			-11, floor_alt+2, -4,   11, ciel_alt-2, -4, windows)
	commands += f("fill %s %s %s %s %s %s %s", \
			-11, floor_alt+2, 4,    11, ciel_alt-2, 4, windows)
	commands += f("fill %s %s %s %s %s %s %s", \
			-7, floor_alt+2, -10,   7, ciel_alt-2, 10, windows)
	commands += f("fill %s %s %s %s %s %s %s", \
			-10, floor_alt+2, -7,   10, ciel_alt-2, 7, windows)
	commands += f(fillCylinder((0, floor_alt, 0), \
			11, (ciel_alt - floor_alt), floor))
	commands += f(fillCylinder((0, floor_alt, 0), \
			5, (ciel_alt - floor_alt), ring))
	commands += f(fillCylinder((0, floor_alt, 0), \
			2, (ciel_alt - floor_alt), floor))
	commands += f(fillCylinder((0, floor_alt+1, 0), \
			11, room_height, air))
	commands += f(fillCylinder((0, ciel_alt, 0), \
			11, 1, ceiling))
	# decorations
	decoration_rarity = 20
	for dx in range(-8,9):
		for dz in range(-8,9):
			if(random.randrange(0,decoration_rarity) == 0):
				commands += f("setblock %s %s %s %s", \
					dx, floor_alt+1, dz, pick(decorations))
	# columns
	commands += f(plusColumn((5, floor_alt+1, 5), \
			(ciel_alt - floor_alt), column))
	commands += f(plusColumn((-5, floor_alt+1, 5), \
			(ciel_alt - floor_alt), column))
	commands += f(plusColumn((5, floor_alt+1, -5), \
			(ciel_alt - floor_alt), column))
	commands += f(plusColumn((-5, floor_alt+1, -5), \
			(ciel_alt - floor_alt), column))
	# treasure
	commands += f("setblock %s %s %s %s", \
			1, floor_alt+1, 1, pick(treasure_blocks))
	commands += f("setblock %s %s %s %s", \
			-1, floor_alt+1, 1, pick(treasure_blocks))
	commands += f("setblock %s %s %s %s", \
			1, floor_alt+1, -1, pick(treasure_blocks))
	commands += f("setblock %s %s %s %s", \
			-1, floor_alt+1, -1, pick(treasure_blocks))
	commands += f("setblock %s %s %s %s", \
			0, floor_alt+1, -2, pick(treasure_blocks))
	commands += f("setblock %s %s %s %s", \
			0, floor_alt+1, 2, pick(treasure_blocks))
	commands += f("setblock %s %s %s %s", \
			-2, floor_alt+1, 0, pick(treasure_blocks))
	commands += f("setblock %s %s %s %s", \
			2, floor_alt+1, 0, pick(treasure_blocks))
	# ladder up
	commands += f("fill %s %s %s %s %s %s minecraft:stonebrick", \
			-1, base_height, -10, 1, base_height, -11)
	commands += f("fill %s %s %s %s %s %s minecraft:ladder 1", \
			-1, base_height+1, -10, 1, floor_alt, -10)
	commands += f("fill %s %s %s %s %s %s minecraft:trapdoor 1", \
			-1, floor_alt+1, -10, 1, floor_alt+1, -10)
	commands += f("fill %s %s %s %s %s %s %s", \
			-1, floor_alt, -11, 1, floor_alt+1, -11, wall)
	#
	if top == False:
		commands += f("fill %s %s %s %s %s %s %s", \
				-1, ciel_alt+3, 1, 1, ciel_alt+5, -11, 'Minecraft:air')
		commands += f("fill %s %s %s %s %s %s %s", \
				-1, ciel_alt+3, -7, 1, ciel_alt+5, -7, 'minecraft:iron_bars')
		commands += f("fill %s %s %s %s %s %s %s", \
				0, floor_alt+1, 0, 0, ciel_alt+2, 0, column)
		commands += f("fill %s %s %s %s %s %s minecraft:ladder 3", \
				0, floor_alt+1, 1, 0, ciel_alt+2, 1)
	commands += f(plusColumn((0, floor_alt+1, 0), \
			1, column))
	# enemies
	commands += f("setblock %s %s %s minecraft:mob_spawner 0 replace %s", \
			5, floor_alt+1, 5, spawner)
	commands += f("setblock %s %s %s minecraft:mob_spawner 0 replace %s", \
			5, floor_alt+1, -5, spawner)
	commands += f("setblock %s %s %s minecraft:mob_spawner 0 replace %s", \
			-5, floor_alt+1, 5, spawner)
	commands += f("setblock %s %s %s minecraft:mob_spawner 0 replace %s", \
			-5, floor_alt+1, -5, spawner)
	commands += f("setblock %s %s %s minecraft:beacon ", \
			0, floor_alt+2, -1)
	commands += f("summon %s %s %s %s %s ", \
			boss[0], 0, floor_alt+3, -2, boss[1])
	commands += f("summon %s %s %s %s %s ", \
			guard[0], 3, floor_alt+2, -7, guard[1])
	commands += f("summon %s %s %s %s %s ", \
			guard[0], -3, floor_alt+2, -7, guard[1])
	commands += f("summon %s %s %s %s %s ", \
			guard[0], 7, floor_alt+2, 2, guard[1])
	commands += f("summon %s %s %s %s %s ", \
			guard[0], -7, floor_alt+2, 2, guard[1])
	# finally, clean-up mess that was made of one of the murder holes
	commands += f("fill %s %s %s %s %s %s %s", \
			-9, base_height, -1, -2, base_height+1, 1, 'Minecraft:air')
	#
	return commands
	

def addTraps(base_height):
	h = base_height
	commands = ""
	trap_rarity = 8
	trap_pts = [(3,h+1,-9, "north"),(4,h+1,-9, "north"),(5,h+1,-9, "north"), \
			(9,h+2,-5, "east"),(9,h+2,-4, "east"),(9,h+2,-3, "east"),\
			(9,h+3,3, "east"),(9,h+3,4, "east"),(9,h+3,5, "east"),\
			(5,h+4,9, "south"),(4,h+4,9, "south"),(3,h+4,9, "south"), \
			(-3,h+5,9, "south"),(-4,h+5,9, "south"),(-5,h+5,9, "south"), \
			(-9,h+6,5, "west"),(-9,h+6,4, "west"),(-9,h+6,3, "west"),\
			(-9,h+7,-3, "west"),(-9,h+7,-4, "west"),(-9,h+7,-5, "west"),\
			(-5,h+8,-9, "north"),(-4,h+8,-9, "north"),(-3,h+8,-9, "north")
	]
	trapMenu = [addTrickWall, addTrickFloor, addTrickWall, addTrickFloor, addTrickWall, addTrickFloor, addTrickFloor, addCaptiveCreeper, addWebFloor, addWebWall, addFallingAnvil, addTNTTrap, addSilverFishWall, addSilverFishWall, addIceFloor, addSlowFloor, addMagmaFloor, addBouncyFloor]
	for pt in trap_pts:
		if(random.randrange(0,trap_rarity) == 0):
			trap_function = pick(trapMenu)
			commands += trap_function(pt,pt[3])
	return commands

def addTrickWall(pt, direction):
	commands = ""
	torch_meta2 = 0
	if(direction == "north"):
		dx = 0
		dz = 1
		piston_meta = 2
		torch_meta1 = 3
	elif(direction == "south"):
		dx = 0
		dz = -1
		piston_meta = 3
		torch_meta1 = 4
	elif(direction == "west"):
		dx = 1
		dz = 0
		piston_meta = 4
		torch_meta1 = 1
	elif(direction == "east"):
		dx = -1
		dz = 0
		piston_meta = 5
		torch_meta1 = 2
	# note: piston a little glitchy (not sticky) when placed
	commands += f("setblock %s %s %s %s 0 replace", pt[0]+dx, pt[1]-1, pt[2]+dz, "minecraft:redstone_wire")
	commands += f("setblock %s %s %s %s %s replace", pt[0]+dx*3, pt[1]-1, pt[2]+dz*3, "minecraft:redstone_torch", torch_meta1)
	commands += f("setblock %s %s %s %s %s replace", pt[0]+dx*3, pt[1]+1, pt[2]+dz*3, "minecraft:redstone_torch", torch_meta2)
	commands += f("setblock %s %s %s %s 0 replace", pt[0], pt[1]-1, pt[2], "minecraft:planks")
	commands += f("setblock %s %s %s %s 0 replace", pt[0], pt[1], pt[2], "minecraft:wooden_pressure_plate")
	commands += f("setblock %s %s %s %s %s replace", pt[0]+dx*2, pt[1]+1, pt[2]+dz*2, "minecraft:sticky_piston", piston_meta)
	commands += "summon Item "+str(pt[0])+" "+str(pt[1]+0.25)+" "+str(pt[2])+"  {Item:{id:\"minecraft:gold_nugget\",Count:1},Age:10}\n"
	return commands
	
def addTrickFloor(pt, direction):
	commands = ""
	if(direction == "north"):
		dx = 0
		dz = 1
		piston_meta = 2
	elif(direction == "south"):
		dx = 0
		dz = -1
		piston_meta = 3
	elif(direction == "west"):
		dx = 1
		dz = 0
		piston_meta = 4
	elif(direction == "east"):
		dx = -1
		dz = 0
		piston_meta = 5
	commands += f("setblock %s %s %s %s 0 replace", pt[0], pt[1]-1, pt[2], "minecraft:planks")
	commands += f("setblock %s %s %s %s 0 replace", pt[0], pt[1], pt[2], "minecraft:wooden_pressure_plate")
	commands += f("setblock %s %s %s %s %s replace", pt[0]+dx, pt[1]-1, pt[2]+dz, "minecraft:piston", piston_meta)
	return commands
	
def addCaptiveCreeper(pt, direction):
	commands = ""
	if(direction == "north"):
		dx = 0
		dz = 1
	elif(direction == "south"):
		dx = 0
		dz = -1
	elif(direction == "west"):
		dx = 1
		dz = 0
	elif(direction == "east"):
		dx = -1
		dz = 0
	commands += f("setblock %s %s %s %s 0 replace", pt[0]+dx, pt[1]-1, pt[2]+dz, "minecraft:air")
	commands += f("setblock %s %s %s %s 0 replace", pt[0]+dx, pt[1], pt[2]+dz, "minecraft:air")
	commands += "summon Creeper "+str(pt[0]+dx)+" "+str(pt[1]-1)+" "+str(pt[2]+dz)+"  {PersistenceRequired:1,powered:1,CustomName:\"Surprise!\"}\n"
	return commands

def addWebFloor(pt, direction):
	commands = ""
	commands += f("setblock %s %s %s %s 0 replace", pt[0], pt[1]-1, pt[2], "minecraft:web")
	return commands

def addIceFloor(pt, direction):
	commands = ""
	commands += f("setblock %s %s %s %s 0 replace", pt[0], pt[1]-1, pt[2], "minecraft:packed_ice")
	return commands
	
def addSlowFloor(pt, direction):
	commands = ""
	commands += f("setblock %s %s %s %s 0 replace", pt[0], pt[1]-1, pt[2], "minecraft:soul_sand")
	return commands
	
def addMagmaFloor(pt, direction):
	commands = ""
	commands += f("setblock %s %s %s %s 0 replace", pt[0], pt[1]-1, pt[2], "minecraft:magma")
	return commands
	
def addBouncyFloor(pt, direction):
	commands = ""
	commands += f("setblock %s %s %s %s 0 replace", pt[0], pt[1]-1, pt[2], "minecraft:slime")
	return commands

def addWebWall(pt, direction):
	commands = ""
	commands += f("setblock %s %s %s %s 0 replace", pt[0], pt[1], pt[2], "minecraft:web")
	commands += f("setblock %s %s %s %s 0 replace", pt[0], pt[1]+1, pt[2], "minecraft:web")
	return commands

def addFallingAnvil(pt, direction):
	commands = ""
	commands += f("setblock %s %s %s %s 0 replace", pt[0], pt[1], pt[2], "minecraft:anvil")
	commands += f("setblock %s %s %s %s 8 replace", pt[0], pt[1]-1, pt[2], "minecraft:leaves")
	commands += f("setblock %s %s %s %s 8 replace", pt[0], pt[1]-2, pt[2], "minecraft:leaves")
	return commands
	
def addTNTTrap(pt, direction):
	commands = ""
	if(direction == "north"):
		dx = 0
		dz = 1
	elif(direction == "south"):
		dx = 0
		dz = -1
	elif(direction == "west"):
		dx = 1
		dz = 0
	elif(direction == "east"):
		dx = -1
		dz = 0
	commands += f("setblock %s %s %s %s 0 replace", pt[0], pt[1], pt[2], "minecraft:wooden_pressure_plate")
	commands += f("setblock %s %s %s %s 0 replace", pt[0]+dx, pt[1]-1, pt[2]+dz, "minecraft:tnt")
	commands += f("setblock %s %s %s %s 0 replace", pt[0]+dx*2, pt[1]-1, pt[2]+dz*2, "minecraft:tnt")
	commands += f("setblock %s %s %s %s 0 replace", pt[0]+dx*2, pt[1], pt[2]+dz*2, "minecraft:tnt")
	commands += f("setblock %s %s %s %s 0 replace", pt[0]+dx*2, pt[1]+1, pt[2]+dz*2, "minecraft:tnt")
	return commands

def addSilverFishWall(pt, direction):
	commands = ""
	if(direction == "north"):
		dx = 0
		dz = 1
	elif(direction == "south"):
		dx = 0
		dz = -1
	elif(direction == "west"):
		dx = 1
		dz = 0
	elif(direction == "east"):
		dx = -1
		dz = 0
	commands += f("setblock %s %s %s %s 2 replace", pt[0]+dx, pt[1]+0, pt[2]+dz, "minecraft:monster_egg")
	commands += f("setblock %s %s %s %s 2 replace", pt[0]+dx, pt[1]+1, pt[2]+dz, "minecraft:monster_egg")
	commands += f("setblock %s %s %s %s 2 replace", pt[0]+dx, pt[1]+2, pt[2]+dz, "minecraft:monster_egg")
	commands += f("setblock %s %s %s %s 2 replace", pt[0]+dx, pt[1]+3, pt[2]+dz, "minecraft:monster_egg")
	commands += f("setblock %s %s %s %s 2 replace", pt[0]+dx, pt[1]+4, pt[2]+dz, "minecraft:monster_egg")
	return commands

def fillCylinder(base_pt, radius, height, material):
	commands = {}
	r = radius
	for tz in range(0,int(radius)):
		z = radius - tz
		for x in range(0,int(radius)):
			if((x*x+z*z) > r*r):
				dx = x
				dz = z
				c=(f("fill %s %s %s %s %s %s %s", \
						base_pt[0]-dx, base_pt[1], base_pt[2]-dz, \
						base_pt[0]+dx, base_pt[1]+height-1, base_pt[2]+dz, \
						material))
				commands[c]=c
				c=(f("fill %s %s %s %s %s %s %s", \
						base_pt[0]-dz, base_pt[1], base_pt[2]-dx, \
						base_pt[0]+dz, base_pt[1]+height-1, base_pt[2]+dx, \
						material))
				commands[c]=c
				break;
	return "".join(commands)
def plusColumn(base_pt, height, material):
	commands = {}
	c=(f("fill %s %s %s %s %s %s %s", \
			base_pt[0]-1, base_pt[1], base_pt[2], \
			base_pt[0]+1, base_pt[1]+height-1, base_pt[2], \
			material))
	commands[c]=c
	c=(f("fill %s %s %s %s %s %s %s", \
			base_pt[0], base_pt[1], base_pt[2]-1, \
			base_pt[0], base_pt[1]+height-1, base_pt[2]+1, \
			material))
	commands[c]=c
	return "".join(commands)


def f(text, *substitutions):
	return (text % substitutions) + "\n"
def pick(list_of_something):
	size = len(list_of_something)
	return list_of_something[random.randrange(0,size)]

main()