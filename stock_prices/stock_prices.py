#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # given an array of stock prices, we want to find the max profit if we bought
  # on one day and sold at another day. 
  # could itterate thru the list and subtract the first element from each of the following elements.
  # All of those would be added to an list (possible profits). 
  # Take the maximum of that list.
  possible_profit = []

  for i in range(len(prices[:-1]) - 1):
      for j in range(i, len(prices[:-1])):
          possible_profit.append(prices[j+1] - prices[i])

  return max(possible_profit)

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))