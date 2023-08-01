#include <iostream>
#include <vector>
using namespace std;


int maxProfit(vector<int>& prices){
    int max_profit = 0;
    for (int i = 1; i< prices.size(); i++){
        if (prices[i] > prices[i-1]){
            max_profit += prices[i] - prices[i-1];
        }
    }
    return max_profit;
}


int main(){
    vector<int> prices = {7,1,5,3,6,4};

    cout << maxProfit(prices);
    return 0;
    }
