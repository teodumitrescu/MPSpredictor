#pragma once

#include <vector>
#include <string>

#define TRAIN_VALUES 9
#define VALID_VALUES 4
#define TEST_VALUES 2
#define EXPECTED_VALUE 0
#define COMMA 44
#define SPACE 32
using namespace std;

class file_information {
    public:
        double expectedValue;
        vector<double> trainValues;
        vector<double> validationValues;
        vector<double> testValues;
        vector<double> fmeans;
};

class tree_steps {
    public:
        vector<int> randomIndexes;
        int function_index;
};

void split_line_by_commas(vector<double> &values, string &line);
void split_line_by_space(vector<int> &values, string &line);
void read_input_files_path(vector<string> &files_path);
void read_files_data(vector<string> paths_to_files, vector<file_information> &files_info);
void read_tree_info(vector<tree_steps> &tree_info);

double mean(vector<double> values, vector<int> indexes);
double geo_mean(vector<double>values, vector<int> indexes);
double median(vector<double> values);
double harmonic_mean(vector<double> values, vector<int> indexes);
double square_mean(vector<double> values, vector<int> indexes);
double minimum_value(vector<double> values, vector<int> indexes);
double maximum_value(vector<double> values, vector<int> indexes);

double calculate_score(vector<tree_steps> tree_info, vector<file_information> files_info);