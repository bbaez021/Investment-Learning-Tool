import React, {useContext} from 'react';
import GlobalContext from '../Reducers/GlobalState';

export const Transaction = ({ transaction }) => {
  const { deleteTransaction } = useContext(GlobalContext);

  const sign = transaction.text === "withdraw" ? '-' : '+';

  return (
    <li className={transaction.text === "withdraw" ? 'minus' : 'plus'}>
      {transaction.text} <span>{sign}${transaction.amount}</span><button onClick={() => deleteTransaction(transaction.id)} className="delete-btn">x</button>
    </li>
  )
}