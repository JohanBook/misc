// Star Arrangements
// https://open.kattis.com/problems/stararrangements
// Johan Book
// 2018-03-14

#include <iostream>

int main()
{
    int S; std::cin >> S;
    
    std::cout << S << ":\n";
    
    // hackaton solution
    // start and end values can be optimized
    // when solution found break and next iteration
    for(int r = 2; r < S; r++)
        for(int s = 1; s < S; s++)
        {
            if(2*r*s == S)
                std::cout << r << "," << r << "\n";
            else if(2*r*s+s == S)
                std::cout << (r+1) << "," << r << "\n";
            else if(2*r*s+r == S)
                std::cout << r << "," << r << "\n";
            else if(2*r*s+r+s+1 == S)
                std::cout << (r+1) << "," << r << "\n";
        }
    
    return 0;
}
