import matplotlib.pyplot as plt

def plt_hist(values):
    cm = plt.cm.tab20b
    n, bins, patches = plt.hist(values, color = 'green')
    bin_centers = 0.5 * (bins[:-1] + bins[1:])
    
    # scale values to interval [0,1]
    col = bin_centers - min(bin_centers)
    col /= max(col)
    for c, p in zip(col, patches):
        plt.setp(p, 'facecolor', cm(c))
    plt.show()