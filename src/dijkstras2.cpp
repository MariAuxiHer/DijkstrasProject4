// #include <iostream> 
// #include <vector> 
// #include <map>
// #include <list>

// using namespace std; 

// // dijsktras.cpp

// // Main Execution

// int main(int argc, char *argv[]) {

//     // So I want a list of lists..
//     int titles_n; 
//     cin >> titles_n;
//     int col, row, title_cost;
//     char title;
//     map<char, int> titles_costs; // insert values as i go.. This will make the first number pretty much unnecesary I think..
//     map<char, int>::iterator titles_costs_it; 

//     for (int i = 0; i < titles_n; i++) {
//         cin >> title >> title_cost;
//         titles_costs.insert(make_pair(title, title_cost));
//     }
//     cin >> row >> col; 
//     // cout << "row " << row << " col " << col; 
//     char titles_matrix[row][col];

//     vector <map <int, int> > adjacency_list (row*col);
//     map <int, int>::iterator adjacent_edges_it; 

//     for (int i = 0; i < row; i++) {
//         for (int j = 0; j < col; j++) {
//             cin >> title;
//             titles_matrix[i][j] = title;
//         }
//     }

//     int start_row, start_col, end_row, end_col; 
//     cin >> start_row >> start_col;
//     cin >> end_row >> end_col;

//     //cout << "start_row, start_col, end_row, end_col;  " << start_row << " " << start_col << " " << end_row << " " << end_col << endl; 
//     /*
//         0 0
//         3 3
//     */
    
   
//     // cout << "titles_costs " << endl;
//     // for (titles_costs_it = titles_costs.begin(); titles_costs_it != titles_costs.end(); titles_costs_it++) {
//     //     cout << titles_costs_it->first << " " << titles_costs_it->second << endl;
//     // }

//     // cout << "titles_matrix " << endl;
//     // for (int i = 0; i < row; i++) {
//     //     for (int j = 0; j < col; j++) {
//     //         cout << titles_matrix[i][j] << " ";
//     //     }
//     //     cout << endl;
//     // }

//     // To create the adjacency list, we visit left and down... 
//     // map <int, int> temp;
//     // temp.insert(make_pair(0,3));

//     // adjacency_list.at(0) = temp;
//     // adjacency_list.at(0).insert(make_pair(0,3));
//     // adjacency_list.at(0).insert(make_pair(1,1));

//     // Look for the value of the element at 0 0.. we will add an extra edge for the node 0 kinda like if that node has a path to itself 
//     // See if that's gonna work, worst case scenario just add that weight... 
//     /*
//     (edge,val)
//     0->(0,3)->(1,1)->(5,3)
//     */

//     // Creating the graph

//     /*
//     h 4
//     m 7
//     r 5
//     */
//     for (int i = 0; i < row; i++) {
//         for (int j = 0; j < col; j++) {
//             // cout << titles_matrix[i][j] << " ";
//             titles_costs_it = titles_costs.find(titles_matrix[i][j]);
//             if (j < (col-1)) {
//                 // titles_costs_it = titles_costs.find(titles_matrix[i][j]);
//                 // insert at element i (0 - row-col)
//                 adjacency_list.at((col*i + j)).insert(make_pair((col*i + (j+1)), titles_costs_it->second));

//                 // in the other direction to make it undirected.. 
//                 //adjacency_list.at((col*i + (j+1))).insert(make_pair((col*i + j), titles_costs_it->second));
//             }

//             if (i < (row-1)) {
//                 // titles_costs_it = titles_costs.find(titles_matrix[i+1][j]);
//                 // insert at element i (0 - row-col)
//                 adjacency_list.at((col*i + j)).insert(make_pair((col*(i+1) + j), titles_costs_it->second));

//                 // in the other direction to make it undirected.. 
//                 //adjacency_list.at((col*(i+1) + j)).insert(make_pair((col*i + j), titles_costs_it->second));
//             }
//         }
//         // cout << endl;
//     }

//     // Print to verify it's working... 
//     // cout << "ADJACENCY LIST " << endl;
//     // for (int i = 0; i < adjacency_list.size(); i++) {
//     //     cout << "i " << i << "->";
//     //     for (adjacent_edges_it = adjacency_list.at(i).begin(); adjacent_edges_it != adjacency_list.at(i).end(); adjacent_edges_it++) {
//     //         cout << "(" << adjacent_edges_it->first << " " << adjacent_edges_it->second << ") ";
//     //     }
//     //     cout << endl;
//     // }



//     multimap <int, vector<int> > frontier; 
//     multimap <int, vector<int> >::iterator frontier_it; 
//     map<int, int> marked; // DESTINATION SOURCE
//     map<int, int>::iterator marked_it; 
//     int accumulated_cost;




//     int current_node = start_row*col + start_col; // give another name to this later... ???????????????????????
//    // for (int i = 0; i < adjacency_list.size(); i++) {
//         //cout << "i " << i << "->";
//         for (adjacent_edges_it = adjacency_list.at(current_node).begin(); adjacent_edges_it != adjacency_list.at(current_node).end(); adjacent_edges_it++) {
//             vector<int> edge; 
//             edge.push_back(current_node); // 0 ??????? name...
//             edge.push_back(adjacent_edges_it->first);
//             //titles_costs_it = titles_costs.find(titles_matrix[start_row][start_col]);
//             accumulated_cost = adjacent_edges_it->second;
//             //accumulated_cost = 0;/*titles_costs_it->second + adjacent_edges_it->second;*/
//             frontier.insert(make_pair(accumulated_cost, edge));
//         }

//         marked.insert(make_pair(current_node, current_node));
//    // }

//     //  multimap <int, vector<int> > frontier; 
// //     cout << "\nFRONTIER\n\n";
// //     for (frontier_it = frontier.begin(); frontier_it != frontier.end(); frontier_it++) {
// //         cout << "(" << frontier_it->first;
// //         for (int i = 0; i < frontier_it->second.size(); i++) {
// //             cout << " " << frontier_it->second.at(i);
// //         }
// //         cout << ") ";
// //     }

// //   cout << "\nMARKEEEED.... hey \n\n";
// //     for (marked_it = marked.begin(); marked_it != marked.end(); marked_it++) {
// //             cout << "{" << marked_it->first;
// //                 cout << " : " << marked_it->second;
// //                 cout << "} ";
// //         }




//     // while......???!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

//     // It's like getting stop in an infinite loop... but Im close, I feel.. 
// bool loop = true;
// //multimap <int, vector<int> >::iterator target_it; 
// int node_to_target; 
// int accumulated_cost_to_target;
// while (loop) {
//     frontier_it = frontier.begin(); 
//     // current node is destination node in the first element of the frontier
//     current_node = frontier_it->second[1];
//     int value_so_far = frontier_it->first;
//     //cout << "\n\nVALUEEEEE SO FARRR " << value_so_far << endl;
//     int source_node = frontier_it->second[0];
//     frontier.erase(frontier_it);
//     //int current_node = 0; // give another name to this later... ???????????????????????

//    // for (int i = 0; i < adjacency_list.size(); i++) {
//         //cout << "i " << i << "->";

//         marked_it = marked.find(current_node);
//   if (marked_it == marked.end()) {
//     //cout << "\n\n CURREEEEEENT NODDDEEE " << current_node << endl;
//    ////////////////////////////////// // vector <map <int, int> > adjacency_list (row*col);
//         for (adjacent_edges_it = adjacency_list.at(current_node).begin(); adjacent_edges_it != adjacency_list.at(current_node).end(); adjacent_edges_it++) {

//             if (adjacent_edges_it->first == (end_row*col+end_col)) {
//                 loop = false;  // HARD CODEEEEEE. CHANGEEEEE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
//             }
//             // marked_it = marked.find(adjacent_edges_it->first); ????????????????????????????**********************************
//             // if not marked....
//             // if (marked_it == marked.end()) { ????????????????????????????**********************************
//                 vector<int> edge; 
//                 edge.push_back(current_node); // 0 ??????? name...
//                 edge.push_back(adjacent_edges_it->first);
//                 accumulated_cost = value_so_far + adjacent_edges_it->second;
//                 frontier.insert(make_pair(accumulated_cost, edge));
//                 if (adjacent_edges_it->first == (end_row*col+end_col)) { // HARD CODEEEEEE. CHANGEEEEE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
//                     // titles_costs_it = titles_costs.find(titles_matrix[end_row][end_col]);
//                     //cout << "\n\nFOUUUUUNDDDDDDDDDDDDDDD " << end_row << " " << end_col << endl; 
//                     node_to_target = current_node; 
//                     accumulated_cost_to_target = accumulated_cost;
//                     // accumulated_cost_to_target = accumulated_cost - titles_costs_it->second;
//                     //cout << " !!!!!!!node_to_target " << node_to_target << " accumulated_cost_to_target " << accumulated_cost_to_target;
//                 }
//         //cout << "TOTAAAAAAL COSTTT " << accumulated_cost << endl;
//                 marked.insert(make_pair(current_node, source_node));
//             // }
//         }



//     }
//     // else {
//     //     cout << "\n\nALREADY VISTED \n\n" << endl;
//     // }
//     //     cout << "\nFRONTIER \n\n";
//     //     for (frontier_it = frontier.begin(); frontier_it != frontier.end(); frontier_it++) {
//     //         cout << "(" << frontier_it->first;
//     //         for (int i = 0; i < frontier_it->second.size(); i++) {
//     //             cout << " " << frontier_it->second.at(i);
//     //         }
//     //         cout << ") ";
//     //     }


//     //     cout << "\nMARKEEEED \n\n";
//     // for (marked_it = marked.begin(); marked_it != marked.end(); marked_it++) {
//     //         cout << "{" << marked_it->first;
//     //             cout << " : " << marked_it->second;
//     //             cout << "} ";
//     //     }

//        // if (adjacent_edges_it->first == (end_row*col+end_col)) break;
// }


// //cout << " !!!!!!!node_to_target " << node_to_target << " accumulated_cost_to_target " << accumulated_cost_to_target;

// list<int> path; 
// list<int>::iterator path_it;

// marked_it = marked.find(node_to_target);

// // HARD CODEEEEEE. CHANGEEEEE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
// path.push_front (end_row*col+end_col);
// path.push_front(marked_it->first);
// while (true) {
//     marked_it = marked.find(marked_it->second);
//     path.push_front(marked_it->first);
//     if (marked_it->first == start_row*col+start_col) {
//         // cout << "wepaa " << marked_it->first << endl; 
//         break;
//     }
// }

// // cout << "LISSSSSSSTTTTTT PATH " << endl;
// // for (path_it = path.begin(); path_it != path.end(); path_it++) {
// //     cout << *path_it << " ";
// // }

// cout << accumulated_cost_to_target << endl; 
// for (path_it = path.begin(); path_it != path.end(); path_it++) {
//     cout << *path_it/col << " " << *path_it%col << endl; 
// }

// // map<int, int>::iterator marked_it; 




// // int min_cost_till_target
// //  target_it = frontier.find(accumulated_cost);

//     // Then add the pair.. I can literally just male two pairs for these two.. 


// //cout << "wepusss" << endl; 




// // at the end.....
//     //    for (marked_it = marked.begin(); marked_it != marked.end(); marked_it++) {
//     //         cout << "{" << marked_it->first;
//     //             cout << " : " << marked_it->second;
//     //             cout << "} ";
//     //     }


   

//     /*
//     (edge,val)
//     0->(0,3)->(1,1)->(5,3)
//     */

//     return 0;
// }