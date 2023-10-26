#include <iostream>
#include<vector>
#include "profile.h"

Profile::Profile(std::string new_name, int new_age, std::string new_city, std::string new_country,std::string
new_pronouns) : name(new_name), age(new_age), city(new_city), country(new_country),pronouns(new_pronouns){}


std::string Profile::view_profile(){

    std::string hobby_list = "";

    for (int i=0;i < hobbies.size(); i++){
        if(i>0){
            hobby_list=hobby_list + ", " + hobbies[i];
        }
        else{
            hobby_list=hobby_list+hobbies[i];
        }

    }

    std::string profile_info = "User name: " + name + "\nUser age: "+ std::to_string(age) +
            " \nUser from " + city + ", " + country + "\nUser pronouns: " + pronouns + "\nUser hobbies: " +
            hobby_list + "\n";

    return profile_info;
}

    void Profile::add_hobby(std::string new_hobby) {
        hobbies.push_back(new_hobby);
    }
    void Profile::change_name(std::string name_to){
        name = name_to;
    }
