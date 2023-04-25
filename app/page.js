'use client'
import { useState } from 'react';


export default function Page() {
    const [Grados, setGrados] = useState('');
    const [resultado, setResultado] = useState('');

    const handleConversion = async (event) => {
        event.preventDefault();
        const response = await fetch(`http://localhost:5000/api/transform/${Grados}`,{
            method: 'GET',
            headers: {
                "Content-Type": "application/json"
            }
        })
        const data = await response.json();
        setResultado(data.resultado);
    }


        return (
            <>
                <div className="App">
                    <form onSubmit={handleConversion}>
                        <label htmlFor="Grados">Grados Celsius</label>
                        <input type="text" className="" placeholder="Convierte de Celsius a Fahrenheit" value={Grados} onChange={(e) => setGrados(e.target.value)} />
                        <button type="submit">Celsius To Fahrenheit</button>
                    </form>

                    <div className="result">
                        Resultado: <span>{resultado}</span>
                    </div>
                </div>
            </>
        )
    }
