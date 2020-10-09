import { writable } from 'svelte/store';

interface Auth {
	email:string,
	username:string,
	role:string,
	token:string,
}

let authData:Auth;

try{
	authData = JSON.parse(localStorage.getItem("auth"));
}catch(e){
	authData = null;
}

export const auth = writable(authData === null ? {email: null, username: null, role: null, token: null} : authData);

auth.subscribe(val => localStorage.setItem("auth", JSON.stringify(val)));