import { useState, useEffect, createContext } from "react";

const AuthContext = createContext();

export const AuthProvider = ({children}) => {
    const [loading, setLoading] = useState(true);
    const [user, setUser] = useState(null)
    const [isAuthenticated, setIsAuthenticated] = useState(false)
    const [error, setError] = useState(null);

    return (
        <AuthContext.Provider
            value={{
                loading,
                user,
                error,
                isAuthenticated,
            }}
        >
            {children}
        </AuthContext.Provider>
    )
}
