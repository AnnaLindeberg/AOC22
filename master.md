### Purpose
Modular Decomposition is a common technique to decompose a given graph G into its key features, namely, it modules.
Modules are subsets of vertices that cannot be distinguished from the outside. In particular, the set of strong modules
forms a hierarchy and thus, can be represented by a unique rooted tree. This tree T is equipped with a unique labeling
t reflecting the internal structure of the particular modules represented by the vertices in T. For each vertex v in T the
label t(v) is one of the following: 0 (parallel), 1 (series) and p (prime). In this way, T together with the labeling t
provides at least to some extent structural information about G. To be more precise, consider the least common ancestor
v=lca(x,y) of two leaves x and y. If t(v) = 0, then x and y do not form an edge in G and if t(v) = 1, then x and y form an
edge in G. Hence, some of the non-edges and edges of G are determined by the labeling t. However, this structural
information gets lost as soon as t(v)=p. In fact, there are non-isomorphic graphs that may have the same modular
decomposition tree as soon as p-vertices are involved. Vertices with label p, thus, behave like a quite secure box that
hide the structural information of G. Hence, the question arises as whether one can open this box and resolve the
p-vertices to obtain a labeled rooted network that can explain the give graph G, i.e., t(lca(x,y)) = 1 if and only if x and y
are linked by an edge. The later idea has been attacked and to some extend been solved by resolving p-vertices by simple
rooted 0/1-labeled cycles or by half-grids which leads to the concept of gatex graphs as well as rooted labeled median graphs.

The aim of Anna's work is to work on generalizations of some of these concepts.
This may go hand-in-hand with the design of algorithms to solve underlying problems.
Generalizations MIGHT be as follows:

1) Edge-colored graphs explained by such networks
2) Directed graphs explained by such networks
3) Set systems or hypergraphs explained by such networks
4) Resolving p-vertices by more general structures than rooted cycles.
### First steps
* Get familiar with the concept of modular decomposition and clustering systems
  of level-1 networks or median graphs, which includes surveying existing
  literature that cover these concepts.
* Possible implementation of existing algorithms.
* Derive conjectures for selected generalizations as discussed above.


### Literature
Depending on the chosen topic, the following papers can be used:

Clustering Systems of Phylogenetic Networks
M. Hellmuth, D. Schaller, P.F. Stadler,
Theory in Biosciences, (to appear), 2023

From Modular Decomposition Trees to Rooted Median Graphs
C. Bruckmann, P.F. Stadler, M. Hellmuth
Discr. Appl. Math, 310, 1-9, 2022

From Modular Decomposition Trees to Level-1 networks: Pseudo-Cographs,
Polar-Cats and Prime Polar-Cats
M. Hellmuth, G.E. Scholz
Discr. Appl. Math, 321, 179-219, 2022

The Mathematics of Xenology: Di-cographs, Symbolic Ultrametrics, 2-structures
and Tree-representable Systems of Binary Relations
M. Hellmuth, P.F. Stadler, N. Wieseke
J. Math. Biology, 75, 1, 199-237, 2017