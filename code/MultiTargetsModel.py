import numpy as np
from pymoo.core.problem import ElementwiseProblem
from funcs import *

class MyProblem(ElementwiseProblem):
    def __init__(self, **kwargs):
        super().__init__(n_var=2, n_obj=1, n_ieq_constr=0, xl=np.array([6000, 0.11]), xu=np.array([25000, 0.12]), **kwargs)

    def _evaluate(self, x, out, *args, **kwargs):
        f1 = - (0.5*local_satisfy_function(x[0]) + 0.5*tourism_satisfy_function(x[0]))
        out["F"] = [f1]
        out["G"] = [] # [g1, g2]

problem = MyProblem()

from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.operators.crossover.sbx import SBX
from pymoo.operators.mutation.pm import PM
from pymoo.operators.sampling.rnd import FloatRandomSampling

algorithm = NSGA2(
    pop_size=40,
    n_offsprings=10,
    sampling=FloatRandomSampling(),
    crossover=SBX(prob=0.9, eta=15),
    mutation=PM(eta=20),
    eliminate_duplicates=True,
)

from pymoo.termination import get_termination
termination = get_termination("n_gen", 100)

from pymoo.optimize import minimize

res = minimize(problem,
               algorithm,
               termination,
               seed=1,
               save_history=True,
               verbose=True)

import matplotlib.pyplot as plt

# 查看优化结果
X = res.X  # 最优解
F = res.F  # 目标函数值
print(f"best solu: {X} , best obj: {F}")
# 可视化设计空间
xl, xu = problem.bounds()
plt.figure(figsize=(7, 5))
# plt.scatter(X[:, 0], np.ones_like(X[:,0]), s=30, facecolors='none', edgecolors='r')# , X[:, 1]
plt.scatter(X, np.ones_like(X), s=30, facecolors='none', edgecolors='r')
plt.xlim(xl[0], xu[0])
# plt.ylim(xl[1], xu[1])
plt.title("Design Space")
plt.show()

# 可视化目标空间
plt.figure(figsize=(7, 5))
plt.scatter(F[:, 0], F[:, 1], s=30, facecolors='none', edgecolors='blue')
plt.title("Objective Space")
plt.show()

