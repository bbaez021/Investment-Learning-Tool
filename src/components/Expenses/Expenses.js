import ExpensesList from "./ExpensesList";
import Card from "../UI/Card";
import "./Expenses.css";
import ExpensesFilter from "./ExpensesFilter";
import ExpensesChart from "./ExpensesChart";
import PropTypes from "prop-types";

import React, { useState } from "react";
const Expenses = (props) => {
  const [filteredYear, setFilteredYear] = useState("2020");

  const filterChangeHandler = (selectedYear) => {
    setFilteredYear(selectedYear);
  };

  let filteredExpenses = props.items.filter((expense) => {
    if (filteredYear === "current" || filteredYear === "total") {
      return true;
    }
    return expense.date.getFullYear().toString() === filteredYear;
  });
  console.log("original_filteredExpenses", filteredExpenses);
  if (filteredYear === "current") {
    const aggregationMap = new Map();
    filteredExpenses.forEach((expense) => {
      if (aggregationMap.has(expense.title)) {
        const item = aggregationMap.get(expense.title);
        item.amount += expense.amount;
      } else {
        aggregationMap.set(expense.title, {
          share_val: 700.0,
          title: expense.title,
          amount: expense.amount,
          date: expense.date,
        });
      }
    });

    filteredExpenses = Array.from(aggregationMap.values());
    /*filteredExpenses = filteredExpenses.reduce((prev, { title, amount }) => {
      prev[title] = prev[title] ? prev[title] + amount : amount;
      return prev;
    }, {});*/
    console.log("filteredExpenses", filteredExpenses);
  }

  if (filteredYear === "total") {
    let dummy_total = [
      {
        share_val: 700.0,
        title: "Total value of everything you invested",
        amount: 0,
        date: new Date(),
      },
    ];
    filteredExpenses.forEach((expense) => {
      dummy_total[0].amount += expense.amount;
    });
    console.log(dummy_total.amount);
    filteredExpenses = dummy_total;
  }

  return (
    <div>
      <Card className="expenses">
        <ExpensesFilter
          selected={filteredYear}
          onChangeFilter={filterChangeHandler}
          balance={props.balance}
        />
        <ExpensesChart expenses={filteredExpenses} />
        <ExpensesList items={filteredExpenses} />
      </Card>
    </div>
  );
};

Expenses.propTypes = {
  items: PropTypes.Array,
  balance: PropTypes.number,
};

export default Expenses;
