import React, {useState, useContext, useEffect} from 'react'
import Image from 'next/image'
import { useRouter } from 'next/router'
import AuthContext from '../../context/AuthContext'

import { toast } from 'react-toastify'

const Login = () => {

    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')

    const router = useRouter();

    const {loading, error, isAuthenticated, login} = useContext(AuthContext)
    useEffect(() => {
        if(error) {
            toast.error(error);
        }

        if(isAuthenticated && !loading) {
            router.push('/');
        }
    }, [isAuthenticated, error, loading])

    const submitHandler = async (e) => {
        e.preventDefault();
        login({email, password})

    };

  return (
    <div className="modalMask">
      <div className="modalWrapper">
        <div className="left">
          <div style={{ width: "100%", height: "100%", position: "relative" }}>
            <Image src="/images/login.svg" alt="login" layout='fill' />
          </div>
        </div>
        <div className="right">
          <div className="rightContentWrapper">
            <div className="headerWrapper">
              <h2> LOGIN</h2>
            </div>
            <form className="form" onSubmit={submitHandler}>
              <div className="inputWrapper">
                <div className="inputBox">
                  <i aria-hidden className="fas fa-envelope"></i>
                  <input
                  type="email"
                  placeholder="Enter Your Email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  pattern='\S+@\S+\.\S+'
                  title='Your email is invalid'
                  required
                  />
                </div>
                <div className="inputBox">
                  <i aria-hidden className="fas fa-key"></i>
                  <input
                    type="password"
                    placeholder="Enter Your Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                  />
                </div>
              </div>
              <div className="loginButtonWrapper">
                <button type="submit" className="loginButton">
                  {loading ? 'Authenticating...' : 'Login'}
                </button>
              </div>
              <p style={{ textDecoration: "none" }} className="signup">
                New to Jobbee? <a href="/register">Create an account</a>
              </p>
            </form>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Login