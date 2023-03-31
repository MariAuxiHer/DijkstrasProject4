/********************************************************************************************************************************************************
    Maria Hernandez 
    Austin Gilbert
    COSC302
    03/31/2023
    Project4
    dijkstras.cpp
    This program uses an adjacency list to represent a graph that symbolizes all possible steps a runner can take to go from 
    a given starting coordinate to a destination coordinates. 
    The program implements a Dijkstras algorithm to find the path with the lowest overall cost. 
***********************************************************************************************************************************************************/

#include <iostream> 
#include <vector> 
#include <map>
#include <list>

using namespace std; 

/*
    The following function performs dijkstras algorithm on the graph passed (adjacency_list) to find the shortest path between starting vertex
    and destination vertex.
*/
void dijkstras (map<int, int> &marked, map<int, int>::iterator &marked_it, int &vertex_to_target, int &accumulated_cost_to_target, 
                int &col, int &start_row, int &start_col, int &end_row, int &end_col, vector <map <int, int> > &adjacency_list) {
    
    /*
        Creating a multimap that will represent our frontier, our frontier would store first the cumulative weight up till that vertex, 
        then source vertex, and then destination vertex.
    */
    multimap <int, vector<int> > frontier; 
    multimap <int, vector<int> >::iterator frontier_it;
    int accumulated_cost;
    int current_vertex = start_row*col + start_col; 
    map <int, int>::iterator adjacent_edges_it; 

    /* 
        Adding the first elements to the frontier, which would be vertices adjacent to the current vertex (starting vertex) with their respective weights 
        from the starting vertex.
    */
    for (adjacent_edges_it = adjacency_list.at(current_vertex).begin(); adjacent_edges_it != adjacency_list.at(current_vertex).end(); adjacent_edges_it++) {
        vector<int> edge; 
        edge.push_back(current_vertex); 
        edge.push_back(adjacent_edges_it->first);
        accumulated_cost = adjacent_edges_it->second;
        frontier.insert(make_pair(accumulated_cost, edge));
    }

    // Mark starting vertex as visited. 
    marked.insert(make_pair(current_vertex, current_vertex));

    // This loop will allow us to loop through our graph until reaching our destination vertex. 
    bool loop = true;
    while (loop) {

        /* 
            We set the frontier_it to point to the beginning of the multimap, then our current vertex would be the 'destination vertex' in this 
            first element of our frontier (the destination vertex is the second element in the vector representing the value in the multimap, 
            such vector stores an edge {source vertex, destination vertex}). Then, the total cost accumulated up until this destionation vertex 
            will be stored in 'value_so_far'. We then erase this element from our frontier. 
        */
        frontier_it = frontier.begin(); 
        current_vertex = frontier_it->second[1];
        int value_so_far = frontier_it->first;
        int source_vertex = frontier_it->second[0];
        frontier.erase(frontier_it);

        // If the current vertex has not been visited, we loop through the vertices adjacent to the current vertex and add them to our frontier.
        marked_it = marked.find(current_vertex);
        if (marked_it == marked.end()) {
            for (adjacent_edges_it = adjacency_list.at(current_vertex).begin(); adjacent_edges_it != adjacency_list.at(current_vertex).end(); adjacent_edges_it++) {
                
                // If we find our destination vertex, we set our flag "loop" to false to finish the while loop and stop adding more elements to our frontier. 
                if (adjacent_edges_it->first == (end_row*col+end_col)) loop = false;  

                // If the vertex adjacent to the current vertex has not been visited, we proceed to add this edge with its respective cumulative weight to our frontier.
                marked_it = marked.find(adjacent_edges_it->first); 
                if (marked_it == marked.end()) { 
                    vector<int> edge; 
                    edge.push_back(current_vertex); 
                    edge.push_back(adjacent_edges_it->first);
                    accumulated_cost = value_so_far + adjacent_edges_it->second;
                    frontier.insert(make_pair(accumulated_cost, edge));

                    /*
                        If we find our destination vertex, we store the vertex from which we reach the destination vertex (which is current vertex) into vertex_to_target, 
                        and the cumulative cost till this vertex in 'accumulated_cost_to_target'. 
                    */
                    if (adjacent_edges_it->first == (end_row*col+end_col)) { 
                        vertex_to_target = current_vertex; 
                        accumulated_cost_to_target = accumulated_cost;
                    }

                    // Mark the current vertex as visited. 
                    marked.insert(make_pair(current_vertex, source_vertex));
                }
            }
        }
    }
}

/* Main Execution */
int main(int argc, char *argv[]) {

    /*
        'tiles_n' stores the number of tiles, 'tiles_cost' stores the cost of each tile, 'tiles_costs' stores pairs containing each tile with their cost, and
        'tile' stores each tile that we will store in our tiles_costs map. 
    */
    int tiles_n; 
    int col, row, tile_cost;
    char tile;
    map<char, int> tiles_costs; 
    map<char, int>::iterator tiles_costs_it; 

    //  Extracting the number of tiles. Then, extracting each tile with its cost and inserting them in the 'tile_costs' map.
    cin >> tiles_n;
    for (int i = 0; i < tiles_n; i++) {
        cin >> tile >> tile_cost;
        tiles_costs.insert(make_pair(tile, tile_cost));
    }

    /*
        Extracting row and col which will give us the size of the matrix (row*col). Then, creating an array of chars representing the 
        map the runner needs to traverse from starting vertex to destination vertex, and an adjacency list that will represent a graph containing all 
        possible steps the runner can take until making it to the destination vertex. 
    */
    cin >> row >> col; 
    char tiles_matrix[row][col];
    vector <map <int, int> > adjacency_list (row*col);

    //  Creating the map the runner will traverse. 
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            cin >> tile;
            tiles_matrix[i][j] = tile;
        }
    }

    //  Extracting starting and destination coordinates. 
    int start_row, start_col, end_row, end_col; 
    cin >> start_row >> start_col;
    cin >> end_row >> end_col;

    //  Creating the adjacency list. 
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            tiles_costs_it = tiles_costs.find(tiles_matrix[i][j]);
    
            //  Creating an edge from current vertex to the next vertex to the right (if it exists).
            if (j < (col-1)) {
                adjacency_list.at((col*i + j)).insert(make_pair((col*i + (j+1)), tiles_costs_it->second));
            }
            
            //  Creating an edge from current vertex to the next vertex to the left (if it exists).
            if (j > 0) {
                adjacency_list.at((col*i + j)).insert(make_pair((col*i + (j-1)), tiles_costs_it->second));
            }
            
            //  Creating an edge from current vertex to the next vertex below (if it exists).
            if (i < (row-1)) {
                adjacency_list.at((col*i + j)).insert(make_pair((col*(i+1) + j), tiles_costs_it->second));
            }
            
            //  Creating an edge from current vertex to the next vertex up (if it exists).
            if (i > 0) {
                adjacency_list.at((col*i + j)).insert(make_pair((col*(i-1) + j), tiles_costs_it->second));
            }
        }
    }

    /*
        Creating a 'marked_it' map that will store our visited vertices, each pair of this map will be {destination vertex (vertex visited), 
        source vertex}. Then, creating the variable 'vertex_to_target', which represents the vertex in the path that connects to the target 
        vertex and 'accumulated_cost_to_target', which stores the total cost up until reaching the destination vertex.
    */
    map<int, int> marked; 
    map<int, int>::iterator marked_it; 
    int vertex_to_target; 
    int accumulated_cost_to_target;

    // Call dijkstras function.
    dijkstras(marked, marked_it, vertex_to_target, accumulated_cost_to_target, col, start_row, start_col, end_row, end_col, adjacency_list);

    // Creating a list that will have the shortest path from source vertex to destination vertex. 
    list<int> path; 
    list<int>::iterator path_it;
    marked_it = marked.find(vertex_to_target);

    // Push front the destination vertex and the vertex that points to this vertex to the list.
    path.push_front(end_row*col+end_col);
    path.push_front(marked_it->first);

    // While we have not found the starting vertex, we use our 'marked' map to backtrack the shortest path till the destination vertex.
    while (true) {
        marked_it = marked.find(marked_it->second);
        path.push_front(marked_it->first);
        if (marked_it->first == start_row*col+start_col) break;
    }

    // Finally, we print the total cost till the destination vertex and the coordinates of the shortest path from starting vertex to destination vertex. 
    cout << accumulated_cost_to_target << endl; 
    for (path_it = path.begin(); path_it != path.end(); path_it++) {
        cout << *path_it/col << " " << *path_it%col << endl; 
    } 
    return 0;
}