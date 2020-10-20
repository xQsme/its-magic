<script lang="ts">
    import axios from 'axios';
    import { url } from '../utils/server';

    let firstName:string;
    let lastName:string;
    let username:string;
    let email:string;
    let password:string;
    let confirmPassword:string;

    function resetUser(){
      firstName = '';
      lastName = '';
      username = '';
      email = '';
      password = '';
      confirmPassword = '';
    }

    function createUser(e) {
      e.preventDefault();
      const data = new FormData();
      data.append("first_name", firstName);
      data.append("last_name", lastName);
      data.append("username", username);
      data.append("email", email);
      data.append("password", password);
		  if(password != confirmPassword){
        alert("Password and confirm password doesnt match")
      }else{
        axios.post(url + 'user/', data).then(r => {
            resetUser();
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
        <input bind:value={firstName} type="text" placeholder="First Name" class="input-form" name="firstname" id="firstname" required/>
        <input bind:value={lastName} type="text" placeholder="Last Name" class="input-form" name="lastname" id="lastname" required/>
        <input bind:value={username} type="text" placeholder="Username" class="input-form" name="username" id="username" required/>
        <input bind:value={email} type="email" placeholder="Email Address" class="input-form" required/>
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