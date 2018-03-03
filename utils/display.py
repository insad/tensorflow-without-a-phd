import numpy as np
from matplotlib import pyplot as plt
from utils import pretty_matplotlib_style

def picture_this_1(data, datalen):
    plt.subplot(211)
    plt.plot(data[datalen-512:datalen+512])
    plt.axvspan(0, 512, color='black', alpha=0.06)
    plt.axvspan(512, 1024, color='grey', alpha=0.04)
    plt.subplot(212)
    plt.plot(data[3*datalen-512:3*datalen+512])
    plt.axvspan(0, 512, color='grey', alpha=0.04)
    plt.axvspan(512, 1024, color='black', alpha=0.06)
    plt.show()
    
def picture_this_2(data, batchsize, seqlen):
    samples = np.reshape(data, [-1, batchsize, seqlen])
    rndsample = samples[np.random.choice(samples.shape[0], 8, replace=False)]
    print("Tensor shape of a batch of training sequences: " + str(rndsample[0].shape))
    print("Random excerpt:")
    subplot = 241
    for i in range(8):
        plt.subplot(subplot)
        plt.plot(rndsample[i, 0]) # first sequence in random batch
        subplot += 1
    plt.show()
    
def picture_this_3(Yout_, evaldata, evallabels, seqlen):
    subplot = 241
    colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
    for i in range(8):
        plt.subplot(subplot)
        k = int(np.random.rand() * evaldata.shape[0])
        l0, = plt.plot(evaldata[k, 1:], label="data")
        plt.plot([seqlen-2, seqlen-1], evallabels[k, -2:])
        l1, = plt.plot([seqlen-1], [Yout_[k]], "o", color="red", label='Predicted')
        l2, = plt.plot([seqlen-1], [evallabels[k][-1]], "o", color=colors[1], label='Ground Truth')
        if i==0:
            plt.legend(handles=[l0, l1, l2])
        subplot += 1
    plt.show()
    
