<script lang="ts">
    import { auth } from '../utils/stores.js';
    import axios from "axios";
    import router from 'page';
    import { url } from '../utils/server.js';
import type { AuthModel } from '../utils/models.js';

    let username:string = '';
    let password:string = '';
    let loginError = false;

    function login(e) {
        e.preventDefault();
        axios({
            method: 'post',
            url: url + 'api-token-auth/',
            headers: {
                'Content-Type' : 'application/json'
            },
            data: {
                username: username,
                password: password
            }
        }).then(response=>{
            // console.log(response);
            auth.set(response.data.user);
           
            auth.update((auth:AuthModel) =>  { 
                // copy auth and adds token
                var newAuth = Object.assign({}, auth);
                //newAuth.role = "ADMIN";
                newAuth.token = response.data.token;
                return newAuth;
            });
            router.redirect('/');
        })
        .catch(error=>{
            //console.log(error);
            loginError = true;
        });
    }
</script>

<div class="register-page">
    <div class="form" >
        <h1>Login</h1>
        <form class="login-form" on:submit={login} >
            <input bind:value={username} type="text" placeholder="Username" class="input-form" name="username" id="username" required/>
            <input bind:value={password} type="password" placeholder="Password" class="input-form" name="password" id="password" required/>
            <button class="formSubmit">Login</button>
        </form>
    </div>
</div>

<style lang="css">
    .input-form{
        display: block;
        text-align: center;
        margin-top: 1.5em;
        margin-bottom: 1.5em;
    }
    .register-page{
        text-align: center;
        margin-left: auto;
        margin-right: auto;
    }
    .formSubmit{
        text-decoration: none;
        background-color: #28a745;
        border-color: #28a745;
        color: #fff;
        text-align: center;
        border-radius: .5em;
    }
</style>