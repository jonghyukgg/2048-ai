from agent.SimpleAgent import RandomAgent
from agent.SimpleAgent import MaxMerge
from agent.MonteCarlo import SimpleMC
from agent.vl import ntuple
from agent.vl_light import ntuple_light
from agent.environment.Simple2048 import Simple2048

import time
import numpy as np

def test(agent):
    env = Simple2048()
    env.init_board()
    score = 0
    movecount = 0
    while True:
        #env.printState()
        moves = env.legal_moves()
        if len(moves) == 0: break
        board = env.getBoard_plane()
        move = agent.get_move(board)
        r = env.do_move(move)
        movecount = movecount + 1
        score = score + r
    maxval = env.maxVal()
    return score, maxval, movecount

def testAgent(N, agent):
    print "Test ", agent.__class__.__name__
    res = np.zeros([N, 4])
    for i in range(N):
        start = time.time()
        score, v, movecount = test(agent)
        res[i,0] = time.time()-start
        res[i,1] = movecount
        res[i,2] = score
        res[i,3] = v
        print i+1, ":", res[i]
    print "Results:", sum(res[:,2]) / float(N), max(res[:,3])
    for i in range(8,14):
        cnt = 0
        for j in range(N):
            if res[j,3] >= 2**i:
                cnt = cnt + 1
        print 2**i, ":", cnt / float(N)
    print ""

if __name__ == '__main__':
    #testAgent(100, RandomAgent())
    #testAgent(100, MaxMerge())
    #testAgent(100, SimpleMC())
    #testAgent(100, ntuple(filename = 'models/vl_0518110412_200000'))
    #testAgent(100, ntuple_light(filename = 'models/vl_light_0613040556_90000'))
    #testAgent(100, ntuple_light(filename = 'models/vl_light_mean_0613205412_30000', xtype='meanquad'))
    #testAgent(100, ntuple(filename = 'models/vl_0518110412_50000', depth = 2))
    #testAgent(100, ntuple_light(filename = 'models/vl_light_mean_0613205412_30000', xtype='meanquad', depth = 2, show_arg = False))
    print "model_500000"
    #testAgent(100, ntuple_light(filename = 'C_impl/model_500000', xtype='meandiffquad'))
    testAgent(20, ntuple_light(filename = 'C_impl/model_500000', xtype='meandiffquad', depth = 2))


'''
model_250000
Test  ntuple_light
Results: 24164.48 4096.0
256 : 1.0
512 : 1.0
1024 : 0.97
2048 : 0.54
4096 : 0.05
8192 : 0.0

model_500000
Test  ntuple_light
Results: 24168.28 4096.0
256 : 1.0
512 : 0.99
1024 : 0.9
2048 : 0.51
4096 : 0.07
8192 : 0.0
'''
