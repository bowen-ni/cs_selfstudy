#include<iostream>
#include<string>
#include"functions.h"
void bleep(std::string &original_text,std::string bleep_word){
    std::string asterisks = "";
    for (int q=0 ; q < bleep_word.size(); q++){
        asterisks = asterisks + "*";
    }
    std::cout << asterisks << "\n";

    for (int i=0 ; i<=original_text.size()-bleep_word.size() ; i++){
        std::string word_checked = "";
        for (int x=0 ; x<bleep_word.size() ; x++){
            word_checked = word_checked + original_text[i+x];
        }
        if(word_checked == bleep_word){
            original_text.replace(i,bleep_word.size(),asterisks);
        }
    }
}
