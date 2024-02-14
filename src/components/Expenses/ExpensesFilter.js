import React from "react";

import "./ExpensesFilter.css";
import PropTypes from "prop-types";

const ExpensesFilter = (props) => {
  const dropdownChangeHandler = (event) => {
    props.onChangeFilter(event.target.value);
  };
  // add array of options instead of duplicating
  return (
    <div className="expenses-filter">
      <div className="expenses-filter__control">
        <div className="balance">BALANCE LEFT: ${props.balance}</div>
        <label>Filter by year:</label>
        <select value={props.selected} onChange={dropdownChangeHandler}>
          <option value="total">Total deposit</option>
          <option value="current">Current Summation of each Stock</option>
          <option value="2022">Transaction History: 2022</option>
          <option value="2021">Transaction History: 2021</option>
          <option value="2020">Transaction History: 2020</option>
          <option value="2019">Transaction History: 2019</option>
        </select>
      </div>
    </div>
  );
};

ExpensesFilter.propTypes = {
  onChangeFilter: PropTypes.func,
  selected: PropTypes.string,
  balance: PropTypes.number,
};

export default ExpensesFilter;
