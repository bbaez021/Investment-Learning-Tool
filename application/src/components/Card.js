import React, { useState } from 'react';
import Cards from 'react-credit-cards'
import 'react-credit-cards/es/styles-compiled.css'

const CardForm = () => {
    const [number, setNumber] = useState('')
    const [name, setName] = useState('')
    const [expiration, setExpiration] = useState('')
    const [cvc, setCvc] = useState('')
    const [focus, setFocus] = useState('')

  return (
    <div className='Card'>
        <Cards
            number={number}
            name={name}
            xpiry={expiration}
            cvc={cvc}
            focused={focus}
            amount={amount}
        />
        <form>
              <input
                  name='text'
                  placeholder='Name'
                  value={name}
                  onChange={e => setName(e.target.value)}
                  onFocus={e => setFocus(e.target.name)}
              />
            <input
                type='tel'
                name='number'
                placeholder='Card Number'
                value={number}
                onChange={e => setNumber(e.target.value)}
                onFocus={e => setFocus(e.target.name)}
            />
            <input
                type='text'
                name='expiration'
                placeholder='MM/YY'
                value={expiration}
                onChange={e => setExpiration(e.target.value)}
                onFocus={e => setFocus(e.target.name)}
            />
              <input
                  type='text'
                  name='cvc'
                  placeholder='CVC'
                  value={cvc}
                  cvc={e => setCvc(e.target.value)}
                  onFocus={e => setFocus(e.target.name)}
              />
        </form>
    </div>
  );
};

export default CardForm;