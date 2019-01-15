//
//  main.cpp
//  cppPr_ex
//
//  Created by 许若芃 on 2018/12/17.
//  Copyright © 2018 许若芃. All rights reserved.
//

#include <iostream>
using namespace std;


int main(int argc, const char * argv[])
{
    string line;
//    while(getline(cin, line)){
//        for (int i =0; i < line.size(); ++i){
//            if(line[i] != ' ')
//                cout << line[i];
//            else cout << endl;
//        }
//    }
    while (cin >> line)
        for (int i = 0; i < line.size(); ++i){
             cout << "x";
        }
    
    
//    string s1 = "gaigechunfengchuimandi";
//    string s2 = "cao";
//    string s3 = "cao";
//    if (s3 == s2)
//        cout << "equal" << endl;
//    else
//        if(s3 > s2)
//            cout << s3 << endl;
//        else cout << s2 << endl;
    return 0;
    
}
