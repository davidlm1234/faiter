function done_check()
  if data.health == -1 then
    return true
  elseif data.timer == 0 then
  	return true
  end
  return false
end

function delta_health()
	delta = data.health - data.enemy_health
	--delta = (data.health - data.enemy_health + 20*data.enemy_block - data.dist)*(100/(100-data.timer)) 
	--delta = (data.health - data.enemy_health + 20*data.block + data.dist)*(100/(data.timer + 1)) 

	return delta
end