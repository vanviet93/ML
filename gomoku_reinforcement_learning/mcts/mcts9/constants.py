RANDOM_SEED = 1234

# board constants
BOARD_WIDTH = 6
BOARD_HEIGHT = 6
N_IN_ROW = 4
P_X = 1
P_O = -1
P_E = 0

# train constants
LEARN_RATE = 2e-3
LR_MULTIPLIER = 1.0
TEMPERATURE = 1.0
NUM_PLAYOUT = 500
C_PUCT = 5.0
BUFFER_SIZE = 10000
BATCH_SIZE = 512

KL_TARGET = 0.02
CHECK_FREQ = 50
GAME_BATCH_NUM = 300
BEST_WIN_RATIO = 0.0
NUM_PURE_MCTS_PLAYOUT = 1000
PLAY_BATCH_SIZE = 1
EPOCHS = 5

# tree node
VIRTUAL_LOSS = 0.05
NUM_INSTANCE = 10