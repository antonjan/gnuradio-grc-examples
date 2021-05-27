# this module will be imported in the into your flowgraph
f1 = 88000000
f2 = 108000000

f =f1
step = 10000

def sweeper(prob_lvl):
	if prob_lvl:
		f +=step
	if f>= f2:f=f1
	
	return f
