#include <iostream>
#include <fstream>
#include <sys/stat.h>
#include <list>
#include <vector>
#include "utils.h"

using namespace std;

int main()
{
    vector<string> paths_to_files;
    vector<file_information> files_info;
    vector<tree_steps> tree_info;

    read_input_files_path(paths_to_files);
    read_files_data(paths_to_files, files_info);
    read_tree_info(tree_info);

    double score = calculate_score(tree_info, files_info);

    cout << "Score is: " << score << endl;
    
    return 0;
}