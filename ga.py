import numpy as np
import random
def initiate_population(no_of_solu_value,sol_value):
    population_size=(no_of_solu_value,sol_value)
    new_population=np.random.uniform(low=-6,high=6,size=population_size)
    return new_population
#print(initiate_population(8,6))
def cal_fitness(letter_1,letter_2):
    fitness_score=np.zeros((1,len(letter_1)))
    loss=0
    for j in range(len(letter_1)):
        for i in range(len(letter_1[0])):
            loss=+letter_1[j][i]-letter_2[0][i]
        fitness_score[0][j]=1/loss
    #print(fitness_score)
    #fitness=1/loss
    #fitness_score.append(fitness)
    #print(fitness_score)

    return fitness_score
def selection_parents(fit,parent_population):
    parent=np.zeros((2,4))#put this in funtion as num
    pa_prob=np.zeros((1,len(parent[0])))
    k=0
    for i in range(len(fit[0])):
        k=k+abs(fit[0][i])
    for i in range(len(fit[0])):
        pa_prob[0][i]=abs(fit[0][i])/k
    s_in=[0,1,2,3]
    #print(pa_prob)
    index_1,index_2=np.random.choice(s_in,2,replace=False,p=pa_prob[0])
    parent_1=parent_population[index_1]
    parent_2=parent_population[index_2]
    parent[0]=parent_1
    parent[1]=parent_2

    return parent
def crossover(parent):
    child=np.zeros((2,4))
    cross_i=(len(parent[0])//2)
    
    child1=list(parent[0][:cross_i])+list(parent[1][cross_i:])
    child2=list(parent[1][:cross_i])+list(parent[0][cross_i:])
    child[0]=child1
    child[1]=child2
    return child
def mutation(children,mutation_rate):
    for i in range(len(children)):
        for j in range(len(children[0])):
            if np.random.random()<mutation_rate:
                children[i][j]=np.random.uniform(low=-6,high=6,size=1)
    return children

 
