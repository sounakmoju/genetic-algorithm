import numpy as np
import ga
target=np.random.uniform(low=-4,high=4,size=(1,4))
#print(target)
#print(target)
generations=1000
new_population=ga.initiate_population(4,4)
#print(new_population)


    
               
#print(ini_population[1,:])
for i in range(generations):
    noveau_popu=np.zeros((4,4))
    #noveau_popu=[]
    fit1=ga.cal_fitness(new_population,target)
   # #print(fit1)
    selected_parents=ga.selection_parents(fit1,new_population)
    crosschild=ga.crossover(selected_parents)
    noveau_popu[0]=crosschild[0]
    noveau_popu[1]=crosschild[1]
    #print(crosschild)
    mutatedchild=ga.mutation(crosschild,0.3)
    noveau_popu[2]=mutatedchild[0]
    noveau_popu[3]=mutatedchild[1]
    new_population=noveau_popu
print(fit1)
    
