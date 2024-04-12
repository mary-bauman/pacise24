https://lightoj.com/contest/pacise-2024/arena/problem/5516

A tree is a well-known data structure that is either empty (null, void, nothing) or is a set of one or more nodes connected by directed edges between nodes satisfying the following properties.

There is exactly one node, called the root, to which no directed edges point
Every node except the root has exactly one edge pointing to it.
There is a unique sequence of directed edges from the root to each node.
For example, consider the illustrations below, in which nodes are represented by circles and edges are represented by lines with arrowheads. The first two of these are trees, but the last is not.

A collection of graphs representing trees. The first 2 graphs (left and center) are trees. The last (right) is not.

**Input**

The input will consist of multiple lines, each representing a single graph. Each lines consists of any number of space-separated pairs of numbers separated by commas. For each pair of numbers representing an edge, the first number represents the origin node and the second number represents the destination node. Node numbers are greater than zero, but might not be sequential. (a graph could include a node 15 but lack a node 14)

**Output**

For each test case display the line "Case k is a tree." or the line "Case k is not a tree.", where k corresponds to the test case number (they are sequentially numbered starting with 1).

**Sample**

**Input**

6 8, 5 3, 5 2, 6 4, 5 6

8 1, 7 3, 6 2, 8 9, 7 5, 7 4, 7 8, 7 6

3 8, 6 8, 6 4, 5 3, 5 6, 5 2

1 2, 2 1

**Output**

Case 1 is a tree.

Case 2 is a tree.

Case 3 is not a tree.

Case 4 is not a tree.
