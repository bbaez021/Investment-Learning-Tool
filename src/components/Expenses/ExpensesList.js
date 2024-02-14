import React from "react";

import Expenseitem from "./Expenseitem";
import "./ExpensesList.css";
import PropTypes from "prop-types";

const ExpensesList = (props) => {
  if (props.items.length === 0) {
    return <h2 className="expenses-list__fallback">Found no expenses.</h2>;
  }

  return (
    <ul className="expenses-list">
      {props.items.map((expense) => (
        <Expenseitem
          key={expense.title}
          share_val={expense.share_val}
          title={expense.title}
          amount={expense.amount}
          date={expense.date}
        />
      ))}
    </ul>
  );
};

ExpensesList.propTypes = {
  items: PropTypes.array,
};

export default ExpensesList;
