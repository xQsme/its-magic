import axios from 'axios';

import { auth } from './stores';
import { get } from 'svelte/store';

export const setupReqRes = () => {
    axios.interceptors.request.use(
        reqConfig => {
            const newConfig = reqConfig;
            const token = get(auth).token;
            if (token) {
                newConfig.headers.Authorization = `Bearer ${token}`;
            }

            return newConfig;
        },
        err => Promise.reject(err),
    );
};
