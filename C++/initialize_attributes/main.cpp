//basic class constructor with initializing attributes
//with members of string type
//only get function
#include <iostream>
#include "Songclass.h"

int main() {
    Song back_to_black("Back to Black","Amy Winehouse");
    std::cout << back_to_black.get_artist() << "\n";
}