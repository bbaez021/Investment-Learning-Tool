import React, { useState, useContext } from 'react'
import GlobalContext from '../Reducers/GlobalState';
import nextId from "react-id-generator";
import CardForm from './Card';
import Toggle from './Toggle';

export const AddTransaction = () => {
    const [text, setText] = useState('');
    const [amount, setAmount] = useState('')

    const { addTransaction } = useContext(GlobalContext);

    const onSubmit = e => {
        e.preventDefault();

        const newTransaction = {
            id: nextId(),
            text,
            amount: text === "withdraw" ? -amount : +amount,
        }

        addTransaction(newTransaction);
    }

    

    return (
        <>
            <h3>Add new transaction</h3>
            <form onSubmit={onSubmit}>
                <div className="form-control">
                    <label htmlFor="Transaction">Transaction Type</label>
                    <select name="selectList" id="selectList" onChange={(e) => setText(e.target.value) }>
                            <option value="deposit">Deposit</option>
                            <option value="withdraw">Withdraw</option>
                        </select> 
                    
                </div>
                <div className="form-control">
                    <label htmlFor="amount"
                    >Amount <br />
                    </label
                    >
                    <input type="number" value={amount} onChange={(e) => setAmount(e.target.value)} placeholder="Enter amount..." />
                </div>
                <CardForm/>
                <button className="btn">Add transaction</button>
            </form>
        </>
    )
}

export default AddTransaction