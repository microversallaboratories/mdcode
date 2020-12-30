
'''
This package is used to interface with pyemma runner functions to simplify analyses.
'''


'''
IMPORTS
'''

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
#import mdshare
import pyemma
from pyemma.util.contexts import settings

'''
FUNCTIONS
'''

def featurize(pdb: str) -> tuple:
    '''
    Performs featurizations for MSM construction.
    '''

    torsions_feat = pyemma.coordinates.featurizer(pdb)
    torsions_feat.add_backbone_torsions(cossin=True, periodic=False)
    torsions_data = pyemma.coordinates.load(files, features=torsions_feat)
    labels = ['backbone\ntorsions']

    positions_feat = pyemma.coordinates.featurizer(pdb)
    positions_feat.add_selection(positions_feat.select_Backbone())
    positions_data = pyemma.coordinates.load(files, features=positions_feat)
    labels += ['backbone atom\npositions']

    distances_feat = pyemma.coordinates.featurizer(pdb)
    distances_feat.add_distances(
        distances_feat.pairs(distances_feat.select_Backbone(), excluded_neighbors=2), periodic=False)
    distances_data = pyemma.coordinates.load(files, features=distances_feat)
    labels += ['backbone atom\ndistances']

    return (labels, torsions_feat, torsions_data, positions_feat, positions_data, distances_feat, distances_data)

def score_cv(data, dim, lag, number_of_splits=10, validation_fraction=0.5):
    """Compute a cross-validated VAMP2 score.
    
    We randomly split the list of independent trajectories into
    a training and a validation set, compute the VAMP2 score,
    and repeat this process several times.
    
    Parameters
    ----------
    data : list of numpy.ndarrays
        The input data.
    dim : int
        Number of processes to score; equivalent to the dimension
        after projecting the data with VAMP2.
    lag : int
        Lag time for the VAMP2 scoring.
    number_of_splits : int, optional, default=10
        How often do we repeat the splitting and score calculation.
    validation_fraction : int, optional, default=0.5
        Fraction of trajectories which should go into the validation
        set during a split.
    """
    # we temporarily suppress very short-lived progress bars
    with pyemma.util.contexts.settings(show_progress_bars=False):
        nval = int(len(data) * validation_fraction)
        scores = np.zeros(number_of_splits)
        for n in range(number_of_splits):
            ival = np.random.choice(len(data), size=nval, replace=False)
            vamp = pyemma.coordinates.vamp(
                [d for i, d in enumerate(data) if i not in ival], lag=lag, dim=dim)
            scores[n] = vamp.score([d for i, d in enumerate(data) if i in ival])
    return scores

def figVAMP2(torsions_data, positions_data, distances_data, dim):
    fig, axes = plt.subplots(1, 3, figsize=(12, 3), sharey=True)
    for ax, lag in zip(axes.flat, [5, 10, 20]):
        torsions_scores = score_cv(torsions_data, lag=lag, dim=dim)
        scores = [torsions_scores.mean()]
        errors = [torsions_scores.std()]
        positions_scores = score_cv(positions_data, lag=lag, dim=dim)
        scores += [positions_scores.mean()]
        errors += [positions_scores.std()]
        distances_scores = score_cv(distances_data, lag=lag, dim=dim)
        scores += [distances_scores.mean()]
        errors += [distances_scores.std()]
        ax.bar(labels, scores, yerr=errors, color=['C0', 'C1', 'C2'])
        ax.set_title(r'lag time $\tau$={:.1f}ns'.format(lag * 0.1))
        if lag == 5:
            # save for later
            vamp_bars_plot = dict(
                labels=labels, scores=scores, errors=errors, dim=dim, lag=lag)
    axes[0].set_ylabel('VAMP2 score')
    fig.tight_layout()
    fig.savefig("VAMP2.png")
    return

def scoringVAMP2(torsions_data, dims, lags):
    fig, ax = plt.subplots()
    for i, lag in enumerate(lags):
        scores_ = np.array([score_cv(torsions_data, dim, lag)
                            for dim in dims])
        scores = np.mean(scores_, axis=1)
        errors = np.std(scores_, axis=1, ddof=1)
        color = 'C{}'.format(i)
        ax.fill_between(dims, scores - errors, scores + errors, alpha=0.3, facecolor=color)
        ax.plot(dims, scores, '--o', color=color, label='lag={:.1f}ns'.format(lag * 0.1))
    ax.legend()
    ax.set_xlabel('number of dimensions')
    ax.set_ylabel('VAMP2 score')
    fig.tight_layout()

    fig.savefig("VAMP2_2.png")
    return

def metastability(tica_output):
    fig, axes = plt.subplots(4, 1, figsize=(12, 5), sharex=True)
    x = 0.1 * np.arange(tica_output[0].shape[0])
    for i, (ax, tic) in enumerate(zip(axes.flat, tica_output[0].T)):
        ax.plot(x, tic)
        ax.set_ylabel('IC {}'.format(i + 1))
    axes[-1].set_xlabel('time / ns')
    fig.tight_layout()

    fig.savefig("metastability.png")
    return

def discretization(tica_output, n_clustercenters):
    scores = np.zeros((len(n_clustercenters), 5))
    for n, k in enumerate(n_clustercenters):
        for m in range(5):
            with pyemma.util.contexts.settings(show_progress_bars=False):
                _cl = pyemma.coordinates.cluster_kmeans(
                    tica_output, k=k, max_iter=50, stride=50)
                _msm = pyemma.msm.estimate_markov_model(_cl.dtrajs, 5)
                scores[n, m] = _msm.score_cv(
                    _cl.dtrajs, n=1, score_method='VAMP2', score_k=min(10, k))

    fig, ax = plt.subplots()
    lower, upper = pyemma.util.statistics.confidence_interval(scores.T.tolist(), conf=0.9)
    ax.fill_between(n_clustercenters, lower, upper, alpha=0.3)
    ax.plot(n_clustercenters, np.mean(scores, axis=1), '-o')
    ax.semilogx()
    ax.set_xlabel('number of cluster centers')
    ax.set_ylabel('VAMP-2 score')
    fig.tight_layout()

    fig.savefig("discretization.png")
    return

def findk(tica_output, k): 
    cluster = pyemma.coordinates.cluster_kmeans(
    tica_output, k=k, max_iter=50, stride=10)
    dtrajs_concatenated = np.concatenate(cluster.dtrajs)
    return cluster

def findTICA2(tica_concatenated, cluster):
    ig, ax = plt.subplots(figsize=(4, 4))
    pyemma.plots.plot_density(
        *tica_concatenated[:, :2].T, ax=ax, cbar=False, alpha=0.3)
    ax.scatter(*cluster.clustercenters[:, :2].T, s=5, c='C1')
    ax.set_xlabel('IC 1')
    ax.set_ylabel('IC 2')
    fig.tight_layout()

    fig.savefig("TICA_2.png")
    return 
