import axios from 'axios';

import { auth } from './stores';
import { get } from 'svelte/store';
import type { AuthModel } from './models';

export const setupReqRes = () => {
    axios.interceptors.request.use(
        reqConfig => {
            const newConfig = reqConfig;
            const authObject:AuthModel = get(auth);
            const token = authObject ? authObject.token : null;
            console.log(token);
            if (token) {
                newConfig.headers.Authorization = `Bearer ${token}`;
            }

            return newConfig;
        },
        err => Promise.reject(err),
    );
};
