
import React, { useState } from "react";
import LoginPresenter from "./LoginPresenter";
import api from 'api'


export const Login = () => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [errorType, setErrorType] = useState("")
    const [error, setError] = useState("");

    const isFormValid = () => {
        if (email === "" || password === "") {
            alert("All fields are required.");
            return false;
        }

        return true;
    };
    const handleSubmit = async () => {
        if (!isFormValid()) {
            return;
        }
        const formData = { email, password }
        try {
            const { status, data } = await api.login(formData);
            if (status === 200) {
                const { refresh } = data;
                localStorage.setItem('token', refresh);
            }
        } catch (e) {
            const status_code = e.response.status;
            if (status_code === 401) {
                setErrorType('invalid')
                setError('유효하지않은 이메일 또는 패스워드입니다')
            } else {
                alert('API Connect Failed')
            }
        } finally {
            //setLoading(false);
        }

    };

    return (
        <LoginPresenter
            email={email}
            setEmail={setEmail}
            password={password}
            setPassword={setPassword}
            error={error}
            setError={setError}
            errorType={errorType}
            setErrorType={setErrorType}
            handleSubmit={handleSubmit}
        />

    )
}

export default Login