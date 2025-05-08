#include <bits/stdc++.h>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string encrypt(string plaintext, string key) {
    int col = key.length();
    int row = plaintext.length() / col;
    if (plaintext.length() % col != 0) {
        row++;
    }

    vector<vector<char>> matrix(row, vector<char>(col, ' ')); 

    for (int i = 0; i < plaintext.length(); ++i) {
        matrix[i / col][i % col] = plaintext[i];
    }

    vector<pair<char, int>> key_order;
    for (int i = 0; i < key.length(); ++i) {
        key_order.push_back(make_pair(key[i], i));
    }
    sort(key_order.begin(), key_order.end());

    string cipher = "";
    for (const auto& pair : key_order) {
        char char_val = pair.first;
        int index = pair.second;

        for (int r = 0; r < row; ++r) {
            if (matrix[r][index] != ' ') {
                cipher += matrix[r][index];
            } else {
                cipher += '_';
            }
        }
    }

    return cipher;
}

string decrypt(string cipher, string key) {
    int col = key.length();
    int row = cipher.length() / col;

    vector<pair<char, int>> key_order;
    for (int i = 0; i < key.length(); ++i) {
        
        key_order.push_back({key[i],i});
    }
    sort(key_order.begin(), key_order.end());

    vector<int> index_order;
    for (const auto& pair : key_order) {
        index_order.push_back(pair.second);
    }

    vector<vector<char>> matrix(row, vector<char>(col, ' '));

    int idx = 0;
    for (int i : index_order) {
        for (int j = 0; j < row; ++j) {
            matrix[j][i] = cipher[idx];
            idx++;
        }
    }

    string plaintext = "";
    for (int i = 0; i < row; ++i) {
        for (int j = 0; j < col; ++j) {
            plaintext += matrix[i][j];
        }
    }

    return plaintext;
}

string remove_trail_z(string plaintext){
    

    while (plaintext.back() == '_') {
        plaintext.pop_back();
    }
    return plaintext;
}

int main() {
    string plaintext, key;

    cout << "Enter plaintext: ";
    getline(cin, plaintext);
    
    
    string removed_space = "";
    for (char c : plaintext){
        if (c != ' ')
            removed_space += toupper(c);
    }
    plaintext = removed_space;
   
    cout << "Enter key: ";
    getline(cin, key);
    
    
    for (char & c : key) c = toupper(c);

    string cipher_text = encrypt(plaintext, key);
    cout<<endl << "First Encryption : " << cipher_text << endl;
    string double_cipher_text = encrypt(cipher_text,"whats");
    cout<<endl << "Double Encryption : "<< double_cipher_text <<endl;

    string single_decrypted_text = decrypt(double_cipher_text,"whats");
    string decrypted_text = decrypt(single_decrypted_text,key);
    cout<<endl<<"Single Decryption :"<<single_decrypted_text<<endl;
    cout<<endl<<"Decrypted Text : "<< decrypted_text<<endl;
    
    string final_decryption = remove_trail_z(decrypted_text);
    cout<<endl<<"Final Plain Text : "<<final_decryption<<endl;
    return 0;
}
