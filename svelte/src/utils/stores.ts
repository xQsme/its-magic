import { writable } from 'svelte/store';
import type { AuthModel } from './models';
import { get } from 'svelte/store';

let authData:AuthModel;

try{
	authData = JSON.parse(localStorage.getItem("auth"));
}catch(e){
	authData = null;
}

export const auth = writable(authData === null ? null : authData);

auth.subscribe(val => localStorage.setItem("auth", JSON.stringify(val)));