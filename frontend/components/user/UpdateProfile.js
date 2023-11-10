import React, { useState, useContext, useEffect } from 'react'
import Image from 'next/image'
import AuthContext from '../../context/AuthContext'

import { toast } from 'react-toastify'
import { useRouter } from 'next/router'

const UpdateProfile = ({access_token}) => {

    const [firstName, setFirstName] = useState('')
    const [lastName, setLastName] = useState('')
    const [email, setEmail] = useState('')
    const [mobile, setMobile] = useState('')
    const [password, setPassword] = useState('')
    const router = useRouter();
    const { updated, loading, error, user, clearErrors, UpdateProfile, setUpdated } = useContext(AuthContext)
    useEffect(() => {

        if (user === null) {
            router.push('/login');
        }
        if (user) {
            setFirstName(user.first_name)
            setLastName(user.last_name)
            setMobile(user.mobile)
            setEmail(user.email)
        }

        if (error) {
            console.log(error)
            for (const i in error) {
                toast.error(error[i][0]);
                clearErrors();
            }
        }

        if(updated) {
            setUpdated(false);
            router.push('/me')
        }


    }, [error, user, updated])

    const submitHandler = async (e) => {
        e.preventDefault();
        UpdateProfile({ first_name:firstName, last_name:lastName, email, mobile, password }, access_token);
    };

    return (
        <div className="modalMask">
            <div className="modalWrapper">
                <div className="left">
                    <div style={{ width: "100%", height: "100%", position: "relative" }}>
                        <Image
                            src={"/images/Profile.svg"}
                            alt="register"
                            layout='fill'
                        />
                    </div>
                </div>
                <div className="right">
                    <div className="rightContentWrapper">
                        <div className="headerWrapper">
                            <h2>Profile </h2>
                        </div>
                        <form className="form" onSubmit={submitHandler}>
                            <div className="inputWrapper">
                                <div className="inputBox">
                                    <i aria-hidden className="fas fa-user"></i>
                                    <input
                                        type="text"
                                        placeholder="Enter First Name"
                                        value={firstName}
                                        onChange={
                                            (e) => setFirstName(e.target.value)
                                        }
                                        required
                                    />
                                </div>

                                <div className="inputBox">
                                    <i aria-hidden className="fas fa-user-tie"></i>
                                    <input
                                        type="text"
                                        placeholder="Enter Last name"
                                        value={lastName}
                                        onChange={
                                            (e) => setLastName(e.target.value)
                                        }
                                        required
                                    />
                                </div>

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
                                    <i aria-hidden className="fas fa-mobile"></i>
                                    <input
                                        type="number"
                                        placeholder="Enter mobile"
                                        value={mobile}
                                        onChange={
                                            (e) => setMobile(e.target.value)
                                        }
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
                                        minLength={6}
                                    />
                                </div>
                            </div>
                            <div className="registerButtonWrapper">
                                <button type="submit" className="registerButton">
                                    {loading ? 'Updating...' : 'Update'}
                                </button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default UpdateProfile;
