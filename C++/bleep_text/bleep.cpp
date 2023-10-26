#include<iostream>
#include<string>
#include"functions.h"
int main(){

    std::string word1 ="broccoli";
    std::string text1 ="I have heard a song from lil Yachty called broccoli, and I think this is the only song "
                       "I heard that includes the word broccoli.";

    //test1
    std::cout << text1 << "\n";

    bleep(text1,word1);

    std::cout << text1 << "\n";

    //test2
    std::string word2 ="fuck";
    std::string text2 ="you are a fucking idiot, fuck yourself and your momma, motherfucker!";
    std::cout << text2 << "\n";

    bleep(text2,word2);

    std::cout << text2 << "\n";

}
