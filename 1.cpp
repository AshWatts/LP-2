#include <iostream>
#include <vector>
#include <queue>
#include <set>
using namespace std;

class Graph
{
    int V;                   // Number of vertices
    vector<vector<int>> adj; // Adjacency list

public:
    Graph(int V) : V(V), adj(V) {}

    void addEdge(int u, int v)
    {
        adj[u].push_back(v);
        adj[v].push_back(u); // Since it's an undirected graph
    }

    void dfsUtil(int node, vector<bool> &visited)
    {
        visited[node] = true;
        cout << node << " ";

        for (int neighbor : adj[node])
        {
            if (!visited[neighbor])
            {
                dfsUtil(neighbor, visited);
            }
        }
    }

    void dfs(int start)
    {
        vector<bool> visited(V, false);
        dfsUtil(start, visited);
    }

    void bfs(int start)
    {
        vector<bool> visited(V, false);
        queue<int> q;

        visited[start] = true;
        q.push(start);

        while (!q.empty())
        {
            int node = q.front();
            q.pop();
            cout << node << " ";

            for (int neighbor : adj[node])
            {
                if (!visited[neighbor])
                {
                    visited[neighbor] = true;
                    q.push(neighbor);
                }
            }
        }
    }
};

int main()
{
    Graph g(7); // Create a graph with 7 nodes (0 to 6)

    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 3);
    g.addEdge(1, 4);
    g.addEdge(2, 5);
    g.addEdge(2, 6);

    cout << "DFS Traversal:\n";
    g.dfs(0);

    cout << "\nBFS Traversal:\n";
    g.bfs(0);

    cout << endl;

    return 0;
}