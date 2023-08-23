import React from 'react'
import { Link } from 'react-router-dom'
import '/Users/moudipajana/Desktop/ibmhack/client/src/components/Navbar/Navbar.css'
import SearchIcon from "@material-ui/icons/Search";
import Avatar from '../../components/Avatar/Avatar'
const Navbar =() => {
  var User = null
  return (
    <nav>
      <div className='navbar'>
        <Link to="/" className='nav-item nav-logo' >
        <img
              src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Stack_Overflow_logo.svg/220px-Stack_Overflow_logo.svg.png"
              alt="logo"
            />
        </Link>
        <Link to="/" className='nav-item nav-btn'>About</Link>
        <Link to="/" className='nav-item nav-btn'>Products</Link>
        <Link to="/" className='nav-item nav-btn'>For Teams</Link>
        <form>
          <input type='text' placeholder='Search...'/>
          <SearchIcon className='search-icon'/>
        </form>
        {User === null ?
          <Link to='/Auth' className='nav-item nav-links'>Log in</Link> :
          <>
             <Avatar backgroundColor='#009dff' px='10px' py='7px' borderRadius='50%'color='white'><Link to='/User' style={{color:"white", textDecoration:"none"}}>M</Link></Avatar>
             <button className='nav-item nav-links'>Log out</button>
          </>
        }
      </div>
    </nav>
  )

}

export default Navbar
