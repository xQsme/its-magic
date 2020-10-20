<script lang="ts">
    import axios from 'axios';
    import { url } from '../utils/server';
    import type { UserModel } from "../utils/models";

    let newUser:UserModel = null;
    let password:string;
    let confirmPassword:string;

    function resetUser(){
      newUser = {username:'',first_name:'',last_name:'',email:'',password:''};
    }

    resetUser();

    function createUser(e) {
      e.preventDefault();
		  if(password != confirmPassword){
        alert("Password and confirm password doesnt match")
      }else{
        newUser.password = password;
        axios.post(url + 'user/', newUser).then(r => {
            resetUser();
            alert('user created')
        }).catch(e => {
            alert('post error');
        });
      }
	}
    
</script>

<div class="register-page">
    <div class="form">
        <h1>Register</h1>
      <form class="register-form" on:submit={createUser}>
        <input bind:value={newUser.first_name} type="text" placeholder="First Name" class="input-form" name="firstname" id="firstname" required/>
        <input bind:value={newUser.last_name} type="text" placeholder="Last Name" class="input-form" name="lastname" id="lastname" required/>
        <input bind:value={newUser.username} type="text" placeholder="Username" class="input-form" name="username" id="username" required/>
        <input bind:value={newUser.email} type="email" placeholder="Email Address" class="input-form" required/>
        <input bind:value={password} type="password" placeholder="Password" class="input-form" name="password" id="password" required/>
        <input bind:value={confirmPassword} type="password" placeholder="Confirm Password" class="input-form" name="confirmpassword" id="confirmpassword" required/>
        <button type="submit" class="formSubmit">create</button>
      </form>
    </div>
  </div>
<style lang="scss">
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