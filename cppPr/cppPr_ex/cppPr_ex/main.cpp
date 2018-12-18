//
//  main.cpp
//  cppPr_ex
//
//  Created by 许若芃 on 2018/12/17.
//  Copyright © 2018 许若芃. All rights reserved.
//

#include <iostream>

int main(int argc, const char * argv[]) {
    int i = 100, sum = 0;
    for (int i = 0; i != 10; ++i)
        sum += i;
    std::cout << i << " " << sum << std::endl;
    return 0;
}
