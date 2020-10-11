import { writable } from 'svelte/store';
import type { AuthModel } from './models';

let authData:AuthModel;

try{
	authData = JSON.parse(localStorage.getItem("auth"));
}catch(e){
	authData = null;
}

export const auth = writable(authData === null ? {email: null, username: null, role: null, token: null} : authData);

auth.subscribe(val => localStorage.setItem("auth", JSON.stringify(val)));