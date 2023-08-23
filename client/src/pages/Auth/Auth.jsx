import React, { useState } from 'react'
import './Auth.css'
import icon from '../../assets/stack-overflow.png'

const Auth = () => {
    const [isSignup, setIsSignup] = useState(false)
  return (
    <section className='auth-section'>
        <div className='auth-container'>
            {!isSignup && <img src={icon} alt='stack overflow' className='login-logo'/>}

        </div>
    </section>
  )
}

export default Auth
