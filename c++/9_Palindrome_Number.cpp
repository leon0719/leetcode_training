#include <iostream>
#include <string>
using namespace std;



bool isPalindrome(int x) {
    if (x < 0){
        return false;
    }
    string s = to_string(x);
    int left = 0;
    int right = s.size() - 1;
    while (left < right){
        if (s[left] != s[right]){
            return false;
        }
        left++;
        right--;
    }
    return true;

}
int main(){
    // unit test isPalindrome function
    int x = 121;
    cout << isPalindrome(x) << endl;
}