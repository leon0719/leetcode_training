#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

vector<int> twoSum(vector<int> &nums, int target) {
    unordered_map<int, int> map;
    vector<int> ans;
    for (int i = 0; i < nums.size(); ++i) {
        if (map.count(nums[i])) {
            ans.push_back(map[nums[i]]);
            ans.push_back(i);
            break;
        }
        map[target - nums[i]] = i;
    }
    return ans;
}

int main() {
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    vector<int> ans = twoSum(nums, target);
    cout << ans[0] << " " << ans[1] << endl;
}