import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.colors as mcolors

# Definição dos estados
EMPTY = 0  # Célula vazia (sem bactéria)
BACTERIA = 1  # Célula com bactéria
LIMITED_RESOURCE = 2  # Área onde o crescimento é mais difícil
DEAD = 3  # Célula morta (bactéria que não sobreviveu)
IMMUNE = 4  # Bactéria que desenvolveu resistência
BARRIER = 5  # Barreira natural ou artificial

# Parâmetros da simulação
GRID_SIZE = 50  # Tamanho da grade (50x50)
STEPS = 50  # Número de passos da simulação
GROWTH_PROB = 0.3  # Probabilidade de crescimento para células vizinhas
LIMITED_GROWTH_PROB = 0.1  # Probabilidade reduzida em áreas com recursos limitados
NUM_INITIAL_POINTS = 5  # Número de pontos iniciais de infecção
MORTALITY_RATE = 0.1  # Probabilidade de uma bactéria morrer em cada iteração
IMMUNITY_RATE = 0.05  # Probabilidade de uma bactéria se tornar imune (reduzida)
VACCINATION_RATE = 0.03  # Probabilidade de que bactérias sejam vacinadas
ANTIBIOTIC_EFFECTIVENESS = 0.8  # Probabilidade de antibióticos eliminarem bactérias não imunes (aumentada)
REINFECTION_RATE = 0.02  # Probabilidade de uma bactéria recuperada ser reinfectada
ANTIBIOTIC_DURATION = 50  # Número de iterações em que antibióticos continuam matando bactérias
RESISTANCE_LIFETIME = 20  # Número de iterações antes de bactérias resistentes morrerem

# Inicializa a grade com todas as células vazias
grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)

# Define múltiplos pontos iniciais para a colônia bacteriana
initial_positions = np.random.randint(0, GRID_SIZE, size=(NUM_INITIAL_POINTS, 2))
for x, y in initial_positions:
    grid[x, y] = BACTERIA

# Define áreas com recursos limitados (dificultando crescimento)
num_limited_areas = 3  # Número de áreas com recursos escassos
for _ in range(num_limited_areas):
    x, y = np.random.randint(0, GRID_SIZE, size=2)
    grid[max(0, x-3):min(GRID_SIZE, x+3), max(0, y-3):min(GRID_SIZE, y+3)] = LIMITED_RESOURCE

# Define barreiras naturais/artificiales que impedem o crescimento
num_barriers = 2  # Número de barreiras
for _ in range(num_barriers):
    x, y = np.random.randint(0, GRID_SIZE, size=2)
    grid[max(0, x-5):min(GRID_SIZE, x+5), max(0, y-1):min(GRID_SIZE, y+1)] = BARRIER

# Matriz de contagem para tempo de resistência
time_resistant = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)

def update(frame):
    global grid, time_resistant
    new_grid = grid.copy()
    
    for x in range(1, GRID_SIZE - 1):
        for y in range(1, GRID_SIZE - 1):
            if grid[x, y] == EMPTY:
                # Verifica vizinhos e decide se cresce
                neighbors = [grid[x-1, y], grid[x+1, y], grid[x, y-1], grid[x, y+1]]
                if any(n == BACTERIA for n in neighbors):
                    growth_prob = LIMITED_GROWTH_PROB if grid[x, y] == LIMITED_RESOURCE else GROWTH_PROB
                    if np.random.rand() < growth_prob:
                        new_grid[x, y] = BACTERIA
            elif grid[x, y] == BACTERIA:
                # Aplicando mortalidade, imunidade e antibióticos
                if np.random.rand() < MORTALITY_RATE:
                    if np.random.rand() > IMMUNITY_RATE:
                        new_grid[x, y] = DEAD  # Bactéria morre
                    else:
                        new_grid[x, y] = IMMUNE  # Bactéria se torna resistente
                elif np.random.rand() < VACCINATION_RATE:
                    new_grid[x, y] = IMMUNE  # Algumas bactérias são vacinadas e tornam-se resistentes
                elif frame < ANTIBIOTIC_DURATION and np.random.rand() < ANTIBIOTIC_EFFECTIVENESS and new_grid[x, y] != IMMUNE:
                    new_grid[x, y] = DEAD  # Antibiótico elimina bactéria não imune
            elif grid[x, y] == IMMUNE:
                time_resistant[x, y] += 1  # Aumenta o tempo da bactéria resistente
                if time_resistant[x, y] >= RESISTANCE_LIFETIME:
                    new_grid[x, y] = DEAD  # Após um tempo, a bactéria resistente morre
            elif grid[x, y] == DEAD:
                # Possibilidade de reinfecção
                if np.random.rand() < REINFECTION_RATE:
                    new_grid[x, y] = BACTERIA
    
    grid = new_grid
    mat.set_data(grid)
    return [mat]

# Definição de um colormap personalizado
cmap = mcolors.ListedColormap(["white", "green", "yellow", "red", "blue", "gray"])
norm = mcolors.BoundaryNorm([0, 1, 2, 3, 4, 5, 6], cmap.N)

# Configuração da animação
fig, ax = plt.subplots()
mat = ax.matshow(grid, cmap=cmap, norm=norm)
ani = animation.FuncAnimation(fig, update, frames=STEPS, interval=200, blit=True)
plt.show()
