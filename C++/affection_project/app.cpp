#include <iostream>
#include<vector>
#include "profile.h"

//affection app that allow user to enter the info to profile
//use initializing attributes
//includes member with type: string, int,and vector
//with function can view profile and add hobbies
int main() {
    Profile Sam("Sam Drakkila", 30, "New York",
                "USA", "he/him");
    std::cout << Sam.view_profile();
    Sam.add_hobby("jerk off");
    Sam.change_name("Sam Smith");
    Sam.add_hobby("hit from the back");
    std::cout << Sam.view_profile();
}
