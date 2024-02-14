import React from "react";
import ExpenseDate from "./ExpenseDate";
import Card from "../UI/Card";
import "./Expenseitem.css";
import PropTypes from "prop-types";

const Expenseitem = (props) => {
  // function clickHandler() {}
  return (
    <li>
      <Card className="expense-item">
        <ExpenseDate date={props.date} />
        <div className="expense-item__description">
          <h2>{props.title}</h2>
          <div className="expense-item__price">
            # of shares: {props.share_val}
          </div>
          <div className="expense-item__price">
            Total shares value: ${props.amount}
          </div>
        </div>
      </Card>
    </li>
  );
};

Expenseitem.propTypes = {
  date: PropTypes.date,
  title: PropTypes.string,
  amount: PropTypes.number,
  share_val: PropTypes.number,
};

export default Expenseitem;
