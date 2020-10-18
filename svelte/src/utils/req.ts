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
            if (token) {
                newConfig.headers.Authorization = `JWT ${token}`;
            }

            return newConfig;
        },
        err => Promise.reject(err),
    );

    axios.interceptors.response.use(response => {
        return response;
    }, err => {
        console.log(err.response);
        if (err.response && err.response.status === 401 && err.response.data.detail === 'Signature has expired.') {
            auth.set(null);
        }
        return Promise.reject(err);
    });
};
