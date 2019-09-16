import retro

env = retro.make('StreetFighterIISpecialChampionEdition-Genesis', 'Champion.Level1.Ken')

env.reset()
done = False
rtotal = 0

while not done:
	env.render()

	#ob, rew, done, info = env.step(env.action_space.sample())
	#env.step(action2)
	#env.step(action3)

	env.step([0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0])
	env.step([0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0])
	env.step([0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1])
	for x in range(1,40):
		env.step([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

	#rtotal = rew + rtotal 
	
	#print("Reward", rew)
	#print(info.get("dist"))