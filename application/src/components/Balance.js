import React, { useContext } from 'react';
import GlobalContext from '../Reducers/GlobalState';

//Money formatter function

export const Balance = () => {
    const { transactions } = useContext(GlobalContext);

    const amounts = transactions.map(transaction => transaction.amount);

    const total = amounts.reduce((acc, item) => (acc += item), 0);

    return (
        <>
            <h4> Current Balance </h4>
            <h1>$ {total}</h1>
        </>
    )
}

export default Balance
