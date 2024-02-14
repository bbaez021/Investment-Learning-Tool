import Expenses from "./components/Expenses/Expenses";

import NewExpense from "./components/NewExpense/NewExpense";
import React, { useState } from "react";

const initial_ticker_list = ["AAPL", "GOOGL", "AMZN", "TSLA"];

const initial_balance = 10000.0;

const DUMMY_EXPENSES = [
  {
    share_val: 700.0,
    title: "TSLA",
    amount: 94.12,
    date: new Date(2020, 7, 14),
  },
  {
    share_val: 700.0,
    title: "AAPL",
    amount: 799.49,
    date: new Date(2021, 2, 12),
  },
  {
    share_val: 700.0,
    title: "GOOGL",
    amount: 294.67,
    date: new Date(2021, 2, 28),
  },
  {
    share_val: 700.0,
    title: "AMZN",
    amount: 450,
    date: new Date(2021, 5, 12),
  },
];
const Investor = () => {
  const [expenses, setExpenses] = useState(DUMMY_EXPENSES);
  const [tickers, setTickers] = useState(initial_ticker_list);
  const [balance, setBalance] = useState(initial_balance);

  const addExpenseHandler = (expense) => {
    setExpenses((prevExpenses) => {
      /*for (let i = 0; i < prevExpenses.length; i++) {
        if (expense.title === prevExpenses[i].title) {
          prevExpenses[i].amount += expense.amount;
          // dont add [] for returning single array
          console.log(prevExpenses[i].amount);
          return [...prevExpenses];
        }
      }*/

      // this is for modifying tickers array, but we dont need it rn
      // MAY USE THIS HOOK LATER SO ONLY COMMENTING IT OUT
      // This has been the cause of option duplicates after adding
      // new expense.
      /*setTickers((prevTickers) => {
        return [expense.title, ...prevTickers];
      });*/

      if (balance - expense.amount < 0) {
        return [...prevExpenses];
      } else {
        setBalance((prevBalance) => {
          return prevBalance - expense.amount;
        });
        return [expense, ...prevExpenses];
      }
    });
  };

  return (
    <div>
      <NewExpense onAddExpense={addExpenseHandler} tickers={tickers} />
      <Expenses items={expenses} balance={balance} />
    </div>
  );
};

export default Investor;
