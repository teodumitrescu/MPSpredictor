#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <bits/stdc++.h>
#include <cmath>
#include <limits>

#include "utils.h"

using namespace std;

void split_line(vector<double> &values, string &line, int separator) {
    string str_value;
    for (int i = 0; i < line.size(); i++) {
        if (int(line[i]) != separator) {
            str_value += line[i]; 
        } else {
            values.push_back(stod(str_value));
            str_value.clear();
        }
    }

    if (str_value.size() > 0) { //it means it has a character, we will check if the first one is number...
        if (int(str_value[0] >= 48 && int(str_value[0] <= 57)))
            values.push_back(stod(str_value));
    }

    return;
}

void read_input_files_path(vector<string> &files_path) {
    fstream input_files_path("input_files.txt");

    string path;
    while (getline(input_files_path, path)) {
        files_path.push_back(path);   
    }

    input_files_path.close();
}

void read_files_data(vector<string> paths_to_files, vector<file_information> &files_info) {
    for (int index = 0; index < paths_to_files.size(); index++) {
        fstream file_info(paths_to_files[index].c_str());
        // fstream file_info("input/[AVE_INT] 2_1-g0.5.CSV");
        string line;
        file_information new_file_info;
        vector<double> values;

        while (getline(file_info, line)) {
            split_line(values, line, COMMA);
        }   

        new_file_info.expectedValue = values[EXPECTED_VALUE];

        int v_index = 1;
        int train_index = TRAIN_VALUES;
        int valid_index = VALID_VALUES;
        int test_index = TEST_VALUES;

        while (train_index > 0) {
            new_file_info.trainValues.push_back(values[v_index]);
            train_index--;
            v_index++;
        }

        while (valid_index > 0) {
            new_file_info.validationValues.push_back(values[v_index]);
            valid_index--;
            v_index++;
        }
        
        while (test_index > 0) {
            new_file_info.validationValues.push_back(values[v_index]);
            test_index--;
            v_index++;
        }

        for (int i = v_index; i < values.size(); i++) {
            new_file_info.fmeans.push_back(values[i]);
        }

        files_info.push_back(new_file_info);
        file_info.close();
    }
}

void read_tree_info(vector<tree_steps> &tree_info) {
    fstream tree_file("output/tree-output.out");

    string line;
    while (getline(tree_file, line)) {
        vector<double> values;
        split_line(values, line, SPACE);
        tree_steps new_tree_step;

        int index = 1;
        int randomValues = int(values[0]);
        while(randomValues > 0) {
            new_tree_step.randomIndexes.push_back(int(values[index]));
            index++;
            randomValues--;
        }
        new_tree_step.function_index = int(values[index]);

        tree_info.push_back(new_tree_step);
    }
}

double mean(vector<double> values, vector<int> indexes) {
    double sum = 0;
    for (int i = 0; i < indexes.size(); i++) {
        sum += values[indexes[i]];
    }

    return sum / indexes.size();
}

double geo_mean(vector<double>values, vector<int> indexes) {
    double sum = 0;
 
    for (int i = 0; i < indexes.size(); i++)
        sum = sum + log(values[indexes[i]]);
 
    sum = sum / indexes.size();
 
    return exp(sum);
}

double median(vector<double> values) {
    vector<double> sorted_vector;

    for (int i = 0; i < values.size(); i++) {
        sorted_vector.push_back(values[i]);
    }

    int size = values.size();
    sort(sorted_vector.begin(), sorted_vector.end());

    if (size % 2 == 0)
       return (sorted_vector[size / 2 - 1] + sorted_vector[size / 2]) / 2;

    return sorted_vector[size / 2];
}

double harmonic_mean(vector<double> values, vector<int> indexes) {
    double sum = 0;
    for (int i = 0; i < indexes.size(); i++)
        sum = sum + (float)1 / values[indexes[i]];
    return (float)indexes.size() / sum;
}

double square_mean(vector<double> values, vector<int> indexes) {
    double sum = 0;

    for (int i = 0; i < indexes.size(); i++)
        sum += values[indexes[i]] * values[indexes[i]];
        
    return sqrt(sum / indexes.size());
}

double minimum_value(vector<double> values, vector<int> indexes) {
    double minimum = numeric_limits<double>::max();

    for (int i = 0; i < indexes.size(); i++) {
        if (values[indexes[i]] < minimum)
            minimum = values[indexes[i]];
    }

    return minimum;
}

double maximum_value(vector<double> values, vector<int> indexes) {
    double maximum = numeric_limits<double>::min();

    for (int i = 0; i < indexes.size(); i++) {
        if (values[indexes[i]] > maximum)
            maximum = values[indexes[i]];
    }

    return maximum;
}

double apply_function(vector<double> values, vector<int> indexes, int functionNumber) {
    if (functionNumber == 0) {
        // cout << "Applying mean..." << endl;
        return mean(values, indexes);

    } else if (functionNumber == 1) {
        // cout << "Applying geo_mean..." << endl;
        return geo_mean(values, indexes);

    } else if (functionNumber == 2) {
        // cout << "Applying harmonic_mean..." << endl;
        return harmonic_mean(values, indexes);

    } else if (functionNumber == 3) {
        // cout << "Applying square_mean..." << endl;
        return square_mean(values, indexes);

    } else if (functionNumber == 4) {
        // cout << "Applying minimum_value..." << endl;
        return minimum_value(values, indexes);

    } else if (functionNumber == 5) {
        // cout << "Applying maximum_value..." << endl;
        return maximum_value(values, indexes);

    }

    // cout << "Applying median..." << endl;
    return median(values);
}

double calculate_score(vector<tree_steps> tree_info, vector<file_information> files_info) {
    double score;
    for (int i = 0; i < tree_info.size(); i++) {
        score = 0;
        for (int j = 0; j < files_info.size(); j++) {
            double value = apply_function(files_info[j].trainValues, 
                                          tree_info[i].randomIndexes, 
                                          tree_info[i].function_index);

            files_info[j].trainValues.push_back(value);

            int score_index = round(255 * value);
            score += files_info[j].fmeans[score_index];        
        } 
        score = score / files_info.size(); 
    }

    return score;
}