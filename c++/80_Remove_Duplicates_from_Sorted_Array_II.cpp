#include <iostream>
#include <vector>
using namespace std;

/*
函式的目的是從列表中移除連續重複出現三次以上的元素，僅保留重複元素最多兩次。

1.這個函式使用 for 迴圈來掃描整個列表。從索引 len(nums) - 2 開始向前遍歷列表，
因為我們要檢查每個元素與前後兩個元素是否相同，以避免超出索引範圍。

2.如果發現目前的元素(nums[i])和它的下一個元素(nums[i+1])以及前一個元素(nums[i-1])都相同，
那麼這代表有三個連續相同的元素，我們需要將第三個相同元素(nums[i+1])從列表中移除。

*/


int removeDuplicates(vector<int>& nums) {
    for (int i = nums.size() -2; i >= 0; i--){
        if (nums[i] == nums[i+1] and nums[i] == nums[i-1]){
            nums.erase(nums.begin() + i + 1);
        }
    }
    return nums.size();
    };


int main(){
    int a ;
    vector<int> nums = {1, 1, 1, 2};
    a = removeDuplicates(nums);
    cout << a;
}
