MASTER_SEED = 1

def reset():
    """Put *all* RNGs back to the same, known state."""
    import random, numpy as np
    random.seed(MASTER_SEED)
    np.random.seed(MASTER_SEED)           # legacy RNG used by many libs
    return np.random.default_rng(MASTER_SEED)   # modern Generator