#include <iostream>
#include <vector>
using namespace std;


int maxArea(vector<int>& height) {
        int max_area = 0;
        int left = 0;
        int right = height.size() - 1;

        while (left < right){
            int area = (right - left) * min(height[left], height[right]);
            max_area = max(max_area, area);
            if (height[left] < height[right]){
                left++;
            }
            else{
                right--;

            }
        }

        return max_area;
    };


int main(){
    vector<int> heights = {1, 8, 6, 2, 5, 4, 8, 3, 7};
    cout << maxArea(heights) << endl;
};
