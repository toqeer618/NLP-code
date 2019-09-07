import random
import numpy as np
import sys
class TSPGA:
    population = []
    population_size = 4
    area_map = (
        (0,   66,  21,   3,    500,  26,   77,   69,   125,  650),
        (66,  0,   35,   115,  36,   65,   85,   90,   44,   54),
        (21,  35,  0,    450,  448,  846,  910,  47,   11,   145),
        (3,   115, 450,  0,    65,   478,  432,  214,  356,  251),
        (500, 36,  448,  65,   0,    258,  143,  325,  125,  39),
        (26,  65,  846,  478,  258,  0,    369,  256,  345,  110),
        (77,  85,  910,  432,  143,  369,  0,    45,   120,  289 ),
        (69,  90,  47,   214,  325,  256,  45,   0,    325,  981 ),
        (125, 44,  11,   356,  125,  345,  120,  325,  0,    326 ),
        (650, 54,  145,  251,  39,   110,  289,  981,  326,  0 )
    )

    def __init__(self, population_size = 4):
        self.population_size = population_size
        self.population = []
        self.init_population()

    def get_random_population(self):
        size = len(self.area_map)
        
        random.seed()
        output = random.sample(range(size), size)
        
        output = ''.join([str(val) for val in output])
       
        return [output, self.fitness(output)]

    def sorted_insert(self, population, new_population):
        pos = 0
        size = len(population)
        for i in range(size):
            if population[i][1] > new_population[1]:
                pos = i
                break
            elif i == size - 1:
                pos = i + 1

        population.insert(pos, new_population)

    def init_population(self):    
        while len(self.population) != self.population_size:
            # Added unique population in list
            new_population = self.get_random_population()
            if new_population not in self.population:
                self.sorted_insert(self.population, new_population)

        return True

    def crossover(self, x, y):
        n = len(x)
        random.seed()
        c = random.randint(1, n-2)

        child1 = y[0:c]
        for i in range(0, len(x)):
            if x[i] not in child1:
                child1 += x[i];
        
        child2 = x[0:c]
        for i in range(0, len(y)):
            if y[i] not in child2:
                child2 += y[i];
        
        return child1, child2

    def random_selection(self):
        """
        n = len(self.population)
        c = random.randint(0, n-1);
        return self.population[c]

        """
        total = 0
        n = len(self.population)

        total_prob = 0
        for i in range(n):
            total += self.population[i][1]
            total_prob += (1.0/self.population[i][1])
        
        random.seed()
        c = random.random()
        prob = 0
        for i in range(n):    
            prob += ((1.0/self.population[i][1]) / total_prob)
            if c < prob:
                return self.population[i];
        
        return self.population[-1]
        
    def swap_string(self, s, a, b):
        i = s.find(a)
        j = s.find(b)
        lst = list(s);
        lst[i], lst[j] = lst[j], lst[i]
        return ''.join(lst)

    def random_prob(self, prob):
        prob = int(1 / prob)
        pin = int(prob/2)
        random.seed()
        if random.randint(0, prob) == pin:
            return True
        return False

    def mutate(self, state, mut_prob):
        size = len(state)
        for i in range(size):
            if self.random_prob(mut_prob):
                while True:
                    random.seed()
                    x = random.randint(0, size-1)
                    random.seed()
                    y = random.randint(0, size-1)
                    if x != y:
                        break

                a = state[x]
                b = state[y]

                state = self.swap_string(state, a, b)
        return state

    def ga(self, gen = 3, mut_prob = 0.01):
        count = 1
        while count <= gen:
            size_population = len(self.population)
            if size_population == 1:
                return self.population[0]

            new_population = []
            for a in range( size_population//2):
                iterCheck = 0
                
                while True:
                    x = self.random_selection()
                    y = self.random_selection()
                    if x != y:
                        break
                    if iterCheck > 10:
                        print ("NOTICE: No good selection available.")
                        return self.population[0]
                    iterCheck += 1

                child1, child2 = self.crossover(x[0], y[0])
                
                child1 = self.mutate(child1, mut_prob)
                child2 = self.mutate(child2, mut_prob)
                
                child1 = [child1, self.fitness(child1)]
                child2 = [child2, self.fitness(child2)]

                if child1 not in self.population:
                    new_population.append(child1)

                if child2 not in self.population:
                    new_population.append(child2)

            for new_child in new_population:
            	self.population.pop();
            	self.sorted_insert(self.population, new_child)
            
            print ("Current Best: " + str(self.population[0]) + "\t\t"               \
                        + "Generation: " + str(count) + "\t\t"                       \
                        + " New Population: " + str(len(new_population)) + "\t\t"    \
                        + " Total Population: " + str(len(self.population)) )
            count += 1
        print ("NOTICE: Generation exceeds")        
        return self.population[0]

    def fitness(self, state):
        total = 0
        for i in range(1, len(state)):
            x = int(state[i-1])
            y = int(state[i])
            total += self.area_map[x][y]
        return total

# Actual answer 334
tsp = TSPGA(population_size=100)
result = tsp.ga(gen=100, mut_prob=0.01)
print (result)