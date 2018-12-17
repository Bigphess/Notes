//
//  main.cpp
//  cppPr_ex
//
//  Created by 许若芃 on 2018/12/17.
//  Copyright © 2018 许若芃. All rights reserved.
//

#include <iostream>

int main(int argc, const char * argv[]) {
    unsigned u = 10, u2 = 42; std::cout << u2 - u << std::endl; std::cout << u - u2 << std::endl;
    int i = 10, i2 = 42;
    std::cout << i2 - i << std::endl; std::cout << i - i2 << std::endl;
    std::cout << i - u << std::endl; std::cout << u - i << std::endl;
    return 0;
}
