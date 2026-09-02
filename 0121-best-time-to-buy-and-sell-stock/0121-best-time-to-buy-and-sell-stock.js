/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let max_profit = 0
    let min_price = prices[0]

    for (let i = 1; i < prices.length; ++i){
       if (min_price > prices[i]){
            min_price = prices[i]
       }
       max_profit = Math.max(max_profit, prices[i] - min_price)
    }

    return max_profit
};