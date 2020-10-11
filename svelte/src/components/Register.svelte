<script lang="ts">
    let firstName:string[];
    let lastName:string[];
    let username:string[];
    let email:string[];
    let password:string[];
    let confirmPassword:string[];

    function createUser() {
		if(password != confirmPassword){
            alert("Password and confirm password doesnt match")
        }else{
            //TODO
            //register
        }
	}
    
</script>

<div class="register-page">
    <div class="form">
        <h1>Register</h1>
      <form class="register-form">
        <input bind:value={firstName} type="text" placeholder="First Name" class="input-form" name="firstname" id="firstname" required/>
        <input bind:value={lastName} type="text" placeholder="Last Name" class="input-form" name="lastname" id="lastname" required/>
        <input bind:value={username} type="text" placeholder="Username" class="input-form" name="username" id="username" required/>
        <input bind:value={email} type="email" placeholder="Email Address" class="input-form" required/>
        <input bind:value={password} type="password" placeholder="Password" class="input-form" name="password" id="password" required/>
        <input bind:value={confirmPassword} type="password" placeholder="Confirm Password" class="input-form" name="confirmpassword" id="confirmpassword" required/>
        <button on:click={createUser} class="formSubmit">create</button>
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