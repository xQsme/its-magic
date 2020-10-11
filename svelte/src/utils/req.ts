import axios from 'axios';

import { auth } from './stores';
import { get } from 'svelte/store';

export const setupReqRes = () => {
    const token = get(auth).token;
    console.log(token);
    axios.interceptors.request.use(
        reqConfig => {
            const newConfig = reqConfig;

            if (token) {
                newConfig.headers.Authorization = `Bearer ${token}`;
            }

            return newConfig;
        },
        err => Promise.reject(err),
    );
};
