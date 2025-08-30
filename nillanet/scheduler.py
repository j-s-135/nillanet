import math

class Scheduler:
    def __init__(self, lr, mode, interval=1, lowbound=1e-8, maxsteps=0, warmup=0, scaler=0):
        self.lr = lr
        self.delta = self.lr
        self.mode = mode
        self.interval = interval # epochs interval at which update applied
        self.lowbound = lowbound # lowbound for lr
        self.steps = 0 # coarser granularity than epochs
        self.maxsteps = maxsteps # units: steps
        self.warmup = warmup # units: epochs, defines a warmup period of reduced lr, set zero to disable
        self.scaler = scaler # e.g. 0.90 for linear scaling
    def step(self, epoch, epochs):
        if self.warmup > 0 and epoch <= self.warmup:
            epoch = epoch + 1
            self.delta = self.lr * (epoch / self.warmup)
            return self.delta
        elif epoch % self.interval != 0:
            return self.delta
        elif self.maxsteps > 0 and self.steps > self.maxsteps:
            return self.delta
        self.steps += 1
        if self.mode == 'inverse':
            self.delta = self.delta * (self.steps ** -0.5)
        elif self.mode == 'cosine':
            self.delta = self.lowbound + (abs(self.lr - self.lowbound) / 2) * (1 + math.cos(math.pi * epoch / epochs))
        elif self.mode == 'linear':
            if self.scaler <= 0 or self.scaler >= 1:
                raise ValueError("scaler must be greater than zero and less than one")
            self.delta = self.delta * self.scaler
        elif self.mode == 'constant':
            self.delta = self.lr
        else:
            raise ValueError(f"mode {self.mode} not recognized")
        return max(self.delta, self.lowbound)
