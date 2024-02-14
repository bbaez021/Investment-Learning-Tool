import React, { useState } from "react";
import "./ExpenseForm.css";
import PropTypes from "prop-types";

const ExpenseForm = (props) => {
  const [enteredTitle, setEnteredTitle] = useState(props.tickers[0]);
  const [enteredAmount, setEnteredAmount] = useState("");
  const [enteredDate, setEnteredDate] = useState("");

  //   const [userInput, setUserInput] = useState({
  //     enteredTitle: "",
  //     enteredAmount: "",
  //     enteredDate: "",
  //   });

  /*const titleChangeHandler = (event) => {
    setEnteredTitle(event.target.value);

    // setUserInput({
    //   ...userInput,
    //   enteredTitle: event.target.value,
    // })

    //this ensures the latest state snapshot
    //when depending on the previous state
    // setUserInput((prevState) => {
    //     return {...prevState, enteredTitle: event.target.value};
    // });
  };*/

  const dropdownChangeHandler = (event) => {
    setEnteredTitle(event.target.value);
  };
  const amountChangeHandler = (event) => {
    setEnteredAmount(event.target.value);
    // setUserInput({
    //   ...userInput,
    //   enteredAmount: event.target.value,
    // });
  };

  const dateChangeHandler = (event) => {
    setEnteredDate(event.target.value);
    // setUserInput({
    //   ...userInput,
    //   enteredDate: event.target.value,
    // });
  };

  const submitHandler = (event) => {
    event.preventDefault();
    const val = 700.0;
    const expenseData = {
      // When we get the data of share values from backend,
      // we can set share_val based on the title
      share_val: val,
      title: enteredTitle,
      amount: +(val * enteredAmount),
      date: new Date(enteredDate),
    };

    props.onSaveExpenseData(expenseData);
    setEnteredTitle("");
    setEnteredAmount("");
    setEnteredDate("");
  };

  return (
    <form onSubmit={submitHandler}>
      <div className="new-expense__controls">
        <div className="new-expense__control">
          <label>Buy Existing Stock</label>

          <select value={enteredTitle} onChange={dropdownChangeHandler}>
            {props.tickers.map((ticker) => {
              console.log(ticker);
              return (
                <option key={ticker} value={ticker}>
                  {ticker}
                </option>
              );
            })}
          </select>

          {/*<input
            type="text"
            value={enteredTitle}
            onChange={titleChangeHandler}
  />*/}
        </div>
        <div className="new-expense__control">
          <label>Shares</label>
          <input
            type="number"
            min="0.01"
            step="0.01"
            value={enteredAmount}
            onChange={amountChangeHandler}
          />
        </div>
        <div className="new-expense__control">
          <label>Date</label>
          <input
            type="date"
            min="2019-01-01"
            max="2022-12-31"
            value={enteredDate}
            onChange={dateChangeHandler}
          />
        </div>
      </div>
      <div className="new-expense__actions">
        <button type="button" onClick={props.onCancel}>
          Cancel
        </button>
        <button type="submit">BUY STOCK</button>
      </div>
    </form>
  );
};

ExpenseForm.propTypes = {
  tickers: PropTypes.array,
  onSaveExpenseData: PropTypes.func,
  onCancel: PropTypes.func,
};

export default ExpenseForm;
