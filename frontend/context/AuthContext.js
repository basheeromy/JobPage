import axios from "axios";
import { useState, useEffect, createContext } from "react";

import { useRouter } from "next/router";

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
    const [loading, setLoading] = useState(false);
    const [user, setUser] = useState(null)
    const [isAuthenticated, setIsAuthenticated] = useState(false)
    const [error, setError] = useState(null);

    const router = useRouter();

    useEffect(() => {

        if (!user) {
            loadUser();
        }
    },
        [user]
    );

    // Login user

    const login = async ({ email, password }) => {
        try {

            setLoading(true)

            const res = await axios.post('/api/auth/login', {
                email,
                password
            })

            if (res.data.success) {
                loadUser();
                setIsAuthenticated(true);
                setLoading(false);
                router.push('/')
            }

        } catch (error) {
            setLoading(false);
            setError(
                error.response &&
                (error.response.data.detail || error.response.data.error)
            )
        }
    }

    // Register user

    const register = async ({ firstName, lastName, email,mobile, password }) => {
        try {

            setLoading(true)

            const res = await axios.post('http://127.0.0.1:8001/api/user/', {
                first_name: firstName,
                last_name: lastName,
                email,
                mobile,
                password
            });

            if (res.data) {
                console.log(res.data)
                console.log("this works")
                setLoading(false);
                router.push('/login')
            }

        } catch (error) {
            setLoading(false);
            setError(
                error.response &&
                (error.response.data)
            )
        }
    }

     // Clear Errors
  const clearErrors = () => {
    setError(null);
  };

    // Load user

    const loadUser = async () => {
        try {

            setLoading(true)

            const res = await axios.get('/api/auth/user')

            if (res.data.user) {
                setIsAuthenticated(true);
                setLoading(false);
                setUser(res.data.user)
            }

        } catch (error) {
            setLoading(false);
            setIsAuthenticated(false);
            setUser(null);
            setError(
                error.response &&
                (error.response.data.detail || error.response.data.error)
            );
        }
    }

    // Logout user

    const logout = async () => {
        try {

            const res = await axios.post('/api/auth/logout')

            if (res.data.success) {
                setIsAuthenticated(false);
                setUser(null)
            }

        } catch (error) {
            setLoading(false);
            setIsAuthenticated(false);
            setUser(null);
            setError(
                error.response &&
                (error.response.data.detail || error.response.data.error)
            );
        }
    }

    return (
        <AuthContext.Provider
            value={{
                loading,
                user,
                error,
                isAuthenticated,
                register,
                login,
                logout,
                clearErrors,

            }}
        >
            {children}
        </AuthContext.Provider>
    )
}
export default AuthContext;
