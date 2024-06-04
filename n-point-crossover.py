import random as rn 

# Initialize Parent Chromosomes
parent1 = [3, 4, 1, 2, 3, 4, 1, 2]
parent2 = [1, 2, 1, 4, 1, 2, 1, 4]

# Function to generate crossover points
def generate_crossover_points(num_points, chromosome_length):
    if num_points < chromosome_length:
        crossover_points = sorted(rn.sample(range(1, 
                                            chromosome_length),
                                            num_points))
        crossover_points.insert(0, 0)  # Insert start point
        crossover_points.append(chromosome_length)  # Insert end point
        return crossover_points
    
chromosome_length = len(parent1)  
num_crossover_points = 3

crossover_points = generate_crossover_points(num_crossover_points,
                                             chromosome_length)
print("Crossover Points:", crossover_points)

# Split the parent chromosomes at the crossover points
parent1_segments = []
parent2_segments = []

for i in range(len(crossover_points) - 1):
    start = crossover_points[i]
    end = crossover_points[i + 1]
    parent1_segments.append(parent1[start:end])
    parent2_segments.append(parent2[start:end])

print("Segments from Parent 1:", parent1_segments)
print("Segments from Parent 2:", parent2_segments)

# Swap segments to create new children
for i in range(1, len(parent1_segments), 2):
    parent1_segments[i], parent2_segments[i] = parent2_segments[i], parent1_segments[i]


# Combine the segments back into full chromosomes
child1 = [gene for segment in parent1_segments for gene in segment]
child2 = [gene for segment in parent2_segments for gene in segment]

print("Parent 1:", parent1)
print("Parent 2:", parent2)

print("New Child 1:", child1)
print("New Child 2:", child2)